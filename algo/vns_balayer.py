# -*- coding: utf-8 -*-
"""TP 30/11/2020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hB7-ENYYWe63C---M99FNKGxx72WeiB1

#XML EDITING
"""

# import xml.dom.minidom as ET

# input=open("E-n101-k14.xml","r")
# input=ET.parse(input)
# nodes=input.getElementsByTagName("node")
# cx=input.getElementsByTagName("cx")
# cy=input.getElementsByTagName("cy")
# tpe=[i.getAttribute("type") for i in nodes]
# node=[i.getAttribute("id") for i in nodes]
# coord_x=[float(i.firstChild.wholeText) for i in cx]
# coord_y=[float(i.firstChild.wholeText) for i in cy]
# output=open("xml2csv_nodes.csv","w")
# output.write("id,cx,cy\n")
# for i in range(len(node)):
#   output.write(str(node[i])+","+str(coord_x[i])+","+str(coord_y[i])+"\n")
# output.close()

# requests=input.getElementsByTagName("request")
# quantity=input.getElementsByTagName("quantity")
# id=[i.getAttribute("id") for i in requests]
# node=[i.getAttribute("node") for i in requests]
# quantities=[float(i.firstChild.wholeText) for i in quantity]
# output=open("xml2csv_requests.csv","w")
# output.write("id,node,quantity\n")
# for i in range(len(id)):
#   output.write(str(id[i])+","+str(node[i])+","+str(quantities[i])+"\n")
# output.close()

# departure=int(input.getElementsByTagName("departure_node")[0].firstChild.wholeText)
# arrival=int(input.getElementsByTagName("arrival_node")[0].firstChild.wholeText)
# capacity=float(input.getElementsByTagName("capacity")[0].firstChild.wholeText)

# print("departure :",departure,"arrival",arrival,"capacity",capacity)

## USEFUL VARIAABLES 
## a generated csv file for nodes and coords : xml2csv_nodes.csv \\ format : id,cx,cy
## a enerated csv file for requests and quantities : xml2csv_requests.csv zz format : id,node,quantity
## departure node : departure
## arrival node : arrival
## capacity of the vehicle : capacity

"""#VNS BEGINS HERE"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:25:32 2020

@author: noamane & ZAZA Zakaria(balayage)
"""

# Required Libraries
import pandas as pd
import numpy as np
import random
import copy

class VNS_Optimizer:
    
    # Attributes
    optimum=["Calculating..."]
    optimum_dist=0.0
    
    # Instantiating
    def __init__(self, dataset_coordinates, max_attempts=25, neighbourhood_size=5, iterations=100):
        
        self.dataset_coordinates=dataset_coordinates
        self.max_attempts=max_attempts
        self.neighbourhood_size=neighbourhood_size
        self.iterations=iterations
        try :
            data = pd.read_csv(dataset_coordinates, sep = ',')
            data = data.values
            self.names=[str(i[0]) for i in data]
            self.Y = np.asarray([[i[1], i[2]] for i in data])
        except:
            data =dataset_coordinates
            self.names = dataset_coordinates[0]
            self.Y = np.asarray(dataset_coordinates[1])
        # self.names=[i[0] for i in data]
        # Y = np.asarray([[i[1], i[2]] for i in data])
        
        #in case we provided the quantities
        try: 
            self.quantity = [i[3] for i in data]
        except IndexError:
            print("quantity not provided")
        # Build the Distance Matrix
        self.X = self.build_distance_matrix(self.Y)
        
        # Start a Random Seed
        seed = self.seed_function(self.X)
        
        # Call the Function
        optimum_temp = self.variable_neighborhood_search(self.X, seed, self.max_attempts, self.neighbourhood_size, self.iterations)
        self.optimum = optimum_temp[0][optimum_temp[0].index(1):] + optimum_temp[0][:optimum_temp[0].index(1)]+[1]
        self.optimum = [self.names[i-1] for i in self.optimum]
        self.optimum_dist = optimum_temp[1]
        print("The best solution is: ", self.optimum, "\nWith a total distance of: ",self.optimum_dist)

    def set_quantities_input(self):
        self.quantity = [int(input()) for i in range(1,len(self.names))]

    def set_quantities_csv(self, dataset_coordinates):
        data = pd.read_csv(dataset_coordinates, sep = ',')
        data = data.values
        self.quantity = np.asarray([[i[1], i[2]] for i in data])
        return self.quantity
    def set_capacity(self, capacity):
        self.capacity = float(capacity)
    # def balayage(self, capacity=self.capacity, quantities=self.quantity, check=False):
    def balayage(self, capacity, quantitie, check=False,view=False):

        # this checks if there is a client who's demand exeeds the max capacity of the camions
        if check:
            for q in quantitie:
                if q>capacity:
                    quantitie.remove(q)
                    print("this client:",q," exeeds the max capacity, will not be treated")
        
        camions = []
        camions_detaills = []
        sum = 0
        camion = [] 
        detaills = []   
        for sol in self.optimum[1:-1]:
            #                                                                                                   print("client: ",str(sol),"index: ",self.names.index(str(sol))-2)
            quan = quantitie[self.names.index(str(sol))-2]
            sum+= float(quan)
            if sum > capacity:
                camions.append(camion)
                camions_detaills.append(detaills)
                camion=[]
                detaills=[]
                camion.append(sol)
                detaills.append(self.names.index(str(sol))-2 )
                sum = float(quan)
            elif sum <= capacity:
                camion.append(sol)
        self.camions = camions
        #if you want to use this part pass view=True
        if view:
            i=0
            for ca in camions:
                print("camion N",i," will deliver to these client in the folowing order: ",end="")
                [print(c,end=" ") for  c in ca]
                print(" ")
                i +=1
    
    def tour_per_camion(self):
        i=1
        for camion in self.camions:
            y = [self.Y[self.names.index(client)-1] for client in ["1.0"]+camion]
            names = [_ for _ in ["1.0"]+camion]
            print("Camion N",i)
            print("-----------------------------------------------------")
            i+=1
            self.camion_tour=VNS_Optimizer([names,y],25,5,100)
        
    # Total distance of a tour
    def distance_calc(self, Xdata, city_tour):
        distance = 0
        for k in range(0, len(city_tour[0])-1):
            m = k + 1
            distance = distance + Xdata[city_tour[0][k]-1, city_tour[0][m]-1]            
        return distance
    
    # Euclidean Distance 
    def euclidean_distance(self, x, y):       
        distance = 0
        for j in range(0, len(x)):
            distance = (x[j] - y[j])**2 + distance   
        return distance**(1/2) 
    
    # Initial Seed
    def seed_function(self, Xdata):
        seed = [[],float("inf")]
        sequence = random.sample(list(range(1,Xdata.shape[0]+1)), Xdata.shape[0])
        sequence.append(sequence[0])
        seed[0] = sequence
        seed[1] = self.distance_calc(Xdata, seed)
        return seed
    
    # Build Distance Matrix
    def build_distance_matrix(self, coordinates):
       a = coordinates
       b = a.reshape(np.prod(a.shape[:-1]), 1, a.shape[-1])
       return np.sqrt(np.einsum('ijk,ijk->ij',  b - a,  b - a)).squeeze()
    
    # Stochastic 3_opt
    def stochastic_3_opt(self, Xdata, city_tour):
        best_route = copy.deepcopy(city_tour)      
        i, j, k  = random.sample(range(0, len(city_tour[0])-1), 3)
        elts=[i,j,k]
        i=min(elts)
        elts.remove(i)
        k=max(elts)
        elts.remove(k)
        j=elts[0]
        best_route[0][i:j+1] = list(reversed(best_route[0][i:j+1]))
        best_route[0][j:k+1] = list(reversed(best_route[0][j:k+1]))
        best_route[0][-1]  = best_route[0][0]
        best_route[1] = self.distance_calc(Xdata, best_route)
        return best_route

    # Stochastic 2_opt
    def stochastic_2_opt(self, Xdata, city_tour):
        best_route = copy.deepcopy(city_tour)      
        i, j  = random.sample(range(0, len(city_tour[0])-1), 2)
        if (i > j):
            i, j = j, i
        best_route[0][i:j+1] = list(reversed(best_route[0][i:j+1]))           
        best_route[0][-1]  = best_route[0][0]              
        best_route[1] = self.distance_calc(Xdata, best_route)                     
        return best_route
    
    # Local Search
    def local_search(self, Xdata, city_tour, max_attempts = 50, neighbourhood_size = 5):
        count = 0
        solution = copy.deepcopy(city_tour)
        while (count < max_attempts):
            for i in range(0, neighbourhood_size):
                candidate = self.stochastic_3_opt(Xdata, city_tour = solution)
            if candidate[1] < solution[1]:
                solution  = copy.deepcopy(candidate)
                count = 0
            else:
                count = count + 1
        count = 0
        while (count < max_attempts):
            for i in range(0, neighbourhood_size):
                candidate = self.stochastic_2_opt(Xdata, city_tour = solution)
            if candidate[1] < solution[1]:
                solution  = copy.deepcopy(candidate)
                count = 0
            else:
                count = count + 1
        return solution
    
    # Variable Neighborhood Search
    def variable_neighborhood_search(self, Xdata, city_tour, max_attempts = 20, neighbourhood_size = 5, iterations = 50):
        count = 0
        solution = copy.deepcopy(city_tour)
        best_solution = copy.deepcopy(city_tour)
        while (count < iterations):
            if count == 0:
                print("Iteration = ", count, "-> Distance ", best_solution[1])
            for i in range(0, neighbourhood_size):
                solution = self.local_search(Xdata, city_tour = solution, max_attempts = max_attempts, neighbourhood_size = neighbourhood_size )
                if (solution[1] < best_solution[1]):
                    best_solution = copy.deepcopy(solution) 
                    break
            count = count + 1
            if count%10==0:
                # print("Iteration = ", count, "-> Distance ", best_solution[1])
                print("-",end="")
        print("\nIteration = ", count, "-> Distance ", best_solution[1])
        return best_solution

# Link for data file https://drive.google.com/file/d/13K0ubdPm7mHtRSAWmAw7IxMGm-5JDmKR/view?usp=sharing
# Link for data_280 file http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/a280.tsp

## How to use
# test=VNS_Optimizer("xml2csv_nodes.csv",25,5,100)
# test.set_quantities_csv("xml2csv_requests.csv")
# test.set_capacity(capacity)
# test.balayage(test.capacity,test.quantity)

# test.tour_per_camion()

# camions_test = test.camions

# camions_test

# test.set_capacity(capacity)

# print(test.quantity)

# test.balayage(test.capacity,test.quantity,view=True)