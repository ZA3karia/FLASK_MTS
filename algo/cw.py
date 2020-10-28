from IPython.display import display
import numpy as np
import pandas as pd



import haversine as hs
from haversine import Unit
#To calculate distance in meters 
#TEST
#dis_m = hs.haversine((Entropot[1],Entropot[2]),(Client[0][1],Client[0][2]),unit=Unit.METERS)
#dis_m

class Input():
    # requirement:
    #       import haversine as hs
    #       from haversine import Unit
    #Definition:
    #       this object represent onle line in the INPUT we are aiming to treat.
    def __init__(self, id, origin, to, origin_lat, origin_lon, to_lat,to_lon, cost ):
        self.id = id
        self.origin = origin
        self.to = to
        self.origin_lat = origin_lat
        self.origin_lon = origin_lon
        self.to_lat = to_lat
        self.to_lon = to_lon
        self.cost = cost
    def dist(self, other_input):
        return hs.haversine((self.origin_lat,self.origin_lon),(other_input.origin_lon,other_input.origin_lon),unit=Unit.METERS)
    def is_origin(self):
        return False
    def display(self):
        print("commande id:",self.id,"from:",self.origin,self.origin_lat, self.origin_lon, "  to:", self.to, self.to_lat, self.to_lon)
    def getname(self):
        return self.to
    def getcoords(self):
        return (self.to_lat, self.to_lon)
    def showinfo(self,X):
        print(self.to, self.to_lat, self.to_lon)
        if X == 0:
            pass
        else:
            print("distance :",hs.haversine(self.getcoords(),X.getcoords(),unit=Unit.METERS)," m")

def node_dis(n1,n2):
    a, b = (n1.lat, n1.lon) if n1.is_origin() else (n1.to_lat ,n1.to_lon)
    c, d = (n2.lat, n2.lon) if n2.is_origin() else (n2.to_lat ,n2.to_lon)
    return hs.haversine((a,b),(c,d),unit=Unit.METERS)

class Entropot():
    def __init__(self,id, lat,lon):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.type = Entropot
    def is_origin(self):
        return True
    def display(self):
        print("entropot id:",self.id, "at :", self.lat, self.lon)
    def getname(self):
        return self.id
    def showinfo(self,X):
        print(self.id, self.lat, self.lon)
        if X == 0:
            pass
        else:
            print("distance :",hs.haversine(self.getcoords(),X.getcoords(),unit=Unit.METERS)," m")
    def getcoords(self):
        return (self.lat, self.lon)


def check_1_valid(e1,v1,v2):
    if e1.getname() == v1.getname():
        return 1
    if e1.getname() == v2.getname():
        return -1
    return 0

class Distance_matrice():
    def __init__(self,INPUT):
        self.origin = Entropot(INPUT[0][1],INPUT[0][3],INPUT[0][4] )
        self.to = [I[2] for I in INPUT]
        self.full_cost = sum([I[7] for I in INPUT])
        self.nodes = [Input(I[0],I[1],I[2],I[3],I[4],I[5],I[6],I[7]) for I in INPUT]
        self.list = INPUT
        self.len = len(INPUT)
    def display(self):
        display(pd.DataFrame(self.list))
    def preprocess(self, show=False):
        Dist_matrix = np.zeros((self.len+1,self.len+1),dtype=float)
        _nodes = self.nodes
        _nodes.insert(0,self.origin)
        for i in range(self.len+1): 
            for j in range(self.len+1):
                Dist_matrix[i][j] = node_dis(_nodes[i],_nodes[j])
        self.Dist_matrix = Dist_matrix
        if show:
            display(pd.DataFrame(self.Dist_matrix))
        return self.Dist_matrix
    def count_saving(self, show=False):
        dim = self.len+1
        Tab = self.Dist_matrix
        for i in range(dim):
            for j in range(dim):
                if i > j:
                    Tab[j,i] = Tab[j,0] + Tab[i,0] - Tab[i,j]
        self.Dist_matrix = Tab
        if show:
            display(pd.DataFrame(self.Dist_matrix))
        return self.Dist_matrix
    def sort(self, show=False):
        dim = self.len+1
        tab = []
        _nodes = self.nodes
        _nodes.insert(0,self.origin)
        for i in range(dim):                #creating the list
            for j in range(1,dim):
                if i > j:
                    tab.append([[_nodes[i],_nodes[j]],self.Dist_matrix[j,i]])
        #for i in range(21):
        #    print(tab[i])
        for t in range(0,len(tab)):         #Sorting the list
            max = t
            for k in range(t,len(tab)):
                if tab[k][1] > tab[max][1]:
                    max = k
            #print (tab[max][1])
            _elt = tab[t]
            tab[t] = tab[max]
            tab[max] = _elt
        self.saving_list = tab
        if show:
            display(pd.DataFrame(tab)) 
        return  self.saving_list 

    def optimise(self, debug = False,show=False):
        list =[]                #this is where we are going to store our element by order
        list.append(self.origin)
        list.append(self.origin)          
        total_saving =0         #initiation
        tab_lenght = len(self.saving_list)
        tab = self.saving_list
        for k in range(tab_lenght):
            #Now we are going to go trough every branch and see if its valid, then we will insert it in case it is valid:
            
            if debug:
                print("\n",k,end="\t")
            b_elemts = tab[k][0]
            elt = [b_elemts[0],b_elemts[1]]
            if debug:
                print("for element",elt[0].getname(),"and",elt[1],end="\t")
            #b_lenght = tab[k][1]
            #validation
            ##in case we are just starting we insert the 2 starting element
            if list[1] is self.origin:
                list.insert(1,elt[0])
                list.insert(1,elt[1])
                total_saving += tab[k][1]           
                if debug:
                    print("list initiated:",list,end="\t")
                ##is containing accessible elements without containing the other
            elif len(list)==self.len+1:
                if debug:
                    print("the list is finished")
                break
            elif elt[0] in list:
                if debug:
                    print("first element in list",end="\t")
                #if the first element is in the list
                if elt[1] in list:
                    #if both element are already in the list, we skip
                    if debug:
                        print("both elements already in the list, pass",end="\t")
                    pass
                else:
                    #repetitive to keep the possibilities
                    
                    #if only the first element is in the list
                    if check_1_valid(elt[0],list[1],list[-2]) != 0:
                        if debug:
                            print("first element in valid position, we insert the second",end="\t")
                        #if the first element is in a valid posistion we insert the second in his position 
                        list.insert(check_1_valid(elt[0],list[1],list[-2]),elt[1])
                        total_saving += tab[k][1]
                    else:
                        if debug:
                            print("the first element ",elt[0]," is not valid, pass",end="\t")
                        pass
                        #else the first element is in the middle of the list, hence its innaccessible 
            elif elt[1] in list:
                if debug:
                    print("the second element in the list",end="\t")
                #if only the second element is in the list
                if check_1_valid(elt[1],list[1],list[-2]) != 0:
                    if debug:
                        print("the second element in a valid position, we insert the second",end="\t")
                    #and the second element is in a valid posistion we insert the first in his position
                    list.insert(check_1_valid(elt[1],list[1],list[-2]),elt[0])
                    total_saving += tab[k][1]
                else:
                    #the second element is in the middle of the list, hence its innaccessible 
                    if debug:
                        print("the second element is in the middle of the list, pass",end="\t")
                    pass
            else:
                if debug:
                    print("this solution is not the most optimal",end="\t")
                #else they both arent in the list witch we should be tackeling later
            if debug:
                print("list:",list,"\t total savings =", total_saving,end="\t")  
        self.route = list
        self.total_saving = total_saving
        if show:
            print(self.display_route())
            print("\n \nThe final list is:",list,"\t with total savings =", total_saving) 
        return self.route
    def display_route(self):
        output = []
        #print("the route is:")
        for N in self.route:
            output.append(N.getname())
            #print(N.getname())
        #print("total saving = ", self.total_saving)
        #output += self.total_saving
        return output   
    def get_route_coords(self):
        output = []
        #print("the route is:")
        for N in self.route:
            output.append(N.getcoords())
            #print(N.getname())
        #print("total saving = ", self.total_saving)
        #output += self.total_saving
        return output   
#Test = False            
#if Test:
#    my_input = Distance_matrice(INPUT)
#    my_input.preprocess()
#    my_input.count_saving()
#    my_input.sort()[0][0]
#    #a[0].getname()
#    output = my_input.optimise(show=True)