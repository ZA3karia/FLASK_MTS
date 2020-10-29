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
        
        # data = pd.read_csv(dataset_coordinates, sep = '\t')
        data = dataset_coordinates
        names=[i[0] for i in data]
        Y = np.asarray([[i[1], i[2]] for i in data])

        # Build the Distance Matrix
        X = self.build_distance_matrix(Y)
        
        # Start a Random Seed
        seed = self.seed_function(X)
        
        # Call the Function
        optimum_temp = self.variable_neighborhood_search(X, seed, self.max_attempts, self.neighbourhood_size, self.iterations)
        self.optimum = optimum_temp[0][optimum_temp[0].index(1):] + optimum_temp[0][:optimum_temp[0].index(1)]+[1]
        self.best_coords = [Y[i-1] for i in self.optimum]
        self.optimum = [names[i-1] for i in self.optimum]
        
        self.optimum_dist = optimum_temp[1]
        # print("The best solution is: ", self.optimum, "\nWith a total distance of: ",self.optimum_dist)
    def get_otp(self):
        return self.optimum
    def get_otp_coords(self):
        return self.best_coords
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
                for j in range(0, neighbourhood_size):
                    solution = self.stochastic_2_opt(Xdata, city_tour = best_solution)
                solution = self.local_search(Xdata, city_tour = solution, max_attempts = max_attempts, neighbourhood_size = neighbourhood_size )
                if (solution[1] < best_solution[1]):
                    best_solution = copy.deepcopy(solution) 
                    break
            count = count + 1
            if count%10==0:
              print("-",end="")
        print("\nIteration = ", count, "-> Distance ", best_solution[1])
        return best_solution

#test=VNS_Optimizer("data.txt",25,5,150)