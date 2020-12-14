"""
in this script I will create a user session to organize the work flow of the website;

What can a user do beside login in :
have a test data
run an optimisation methode,
create a map for display


##Other classes:
Optimisation methode, 
this can go under the utilities that the user can do
user.tool.methode():
it contains the 



"""

"""
Brainstorming

if all the data is in the database let see what we can doo 

vns blayer input:


"""


import numpy as np
import pandas as pd
from algo import cw, vns
from algo import vns_balayer as vb
from io import StringIO     #enable us to run preprocessing on data from the form

import folium

class Tms_User():
    """
    usage: 
    first initiate with a name:
    user = Tms_User("Zakaria")
    
    and set the data and methode 
    >> user.set_data("csv_file_path", "csv")
    >> user.set_methode("vns")
    or do it all in one line
    user = Tms_User("Zakaria").set_data("csv_file_path","csv").set_methode("vns")

    Then run the optimisation you want 
    user.run_optimisation()
    
    Then view the output or use it :
    print(user.opt)

    """
    def __init__(self,name):
        self.name=name
        self.mtd = None
        self.data = None
        self.opt = None
        self.map = None

        self.capacity = None
        self.expedition_data = None
        self.balayed_opt = None

        # self.camions = None
    def render_map(self, update=True):
        coords = self.get_optimisation()
        m = folium.Map(location=coords[0], tiles="OpenStreetMap", zoom_start=6)
        folium.Marker(coords[0],
                    popup="Rabat",
                    icon=folium.Icon(color='green')).add_to(m)
        points = coords
        folium.PolyLine(points, color="blue" , weight=2.5, opacity=0.8).add_to(m)
        self.map = m

    def render_map_balay(self, update=True):
        coords = self.balayed_opt.output.Y
        m = folium.Map(location=coords[0], tiles="OpenStreetMap", zoom_start=6)
        folium.Marker(coords[0],
                    popup="Rabat",
                    icon=folium.Icon(color='green')).add_to(m)
        # points = coords
        colors = ["blue","red","green","lime", "yellow", "black", "white"]
        i=0
        for cam in self.balayed_opt.camions:
            color_number = i%len(colors)
            color = colors[color_number]
            i+=1

            points = cam.get_otp_coords()
            folium.PolyLine(points, color=color , weight=2.5, opacity=0.8).add_to(m)
        self.map = m
    
    def set_data(self, data, type, separetor = '\t'):
        data_title = self.name + " data"
        mydata = Data(title=data_title)
        if type=="csv":
            self.data = mydata.set_client_csv(data,separetor=separetor)
        return self
    
    def set_data_bytes(self, bytes_data, separetor = ','):
        data_title = self.name + " data"
        mydata = Data(title=data_title)
        s = str(bytes_data,'utf-8')
        data = StringIO(s)
        self.data = mydata.set_client_csv(data,separetor=separetor)
        return self
    
    def set_expedition_data(self, bytes_data, separetor=','):
        data_title = self.name + "_expedition_data"
        mydata = Data(title=data_title)
        s = str(bytes_data,'utf-8')
        data = StringIO(s)
        self.expedition_data = mydata.set_expedtion_csv(data,separetor=separetor)
        return self
    
    def set_methode(self, method):
        self.mtd = method
        return self
    
    def run_optimisation(self):
        
        self.opt = Optimisation(self.mtd,self.data)
        
        return self
    ## this next methode is used in case you want to use a 
    ## diffrent optimisation without reinitiating all the settings 
    def run_new_optimisation(self, method, data): 
        self.mtd = method
        self.data = data
        self.run_optimisation()
        return self
    
    def get_optimisation(self):
        if self.opt:
            if self.opt.output_coords:
                return self.opt.output_coords
            else:
                return self.opt.output
        else:
            return "no optimisation defined"
    
    
    def set_capacity(self, capacity):
        self.capacity=capacity
        return self
    
    def run_balayage(self,mtd):
        expedition = self.expedition_data.get_expedition_data()
        self.balayed_opt = Balayed_Optimisation(mtd, self.data.clients, expedition, self.capacity)
        return self
    def get_balayage(self):
        return self.balayed_opt.output
    

class Balayed_Optimisation():
    def __init__(self, mtd, clients, quantities, capacity):
        self.mtd = mtd
        self.clients = clients
        # make in mind quantities here is a csv from StinngIO from upload
        self.quantities = quantities #this is good in the begening but should be fixed to allow other input possibilities
        self.capacity = capacity
        self.output = None
        if mtd==1:
            self.run_blayage_type1()
        if mtd==2:
            self.run_blayage_type2()
        else:
            print("methode not added yet")
    
    def run_blayage_type1(self):
        output = vb.VNS_Optimizer(self.clients,25,5,200)
        output.set_quantity_pd(self.quantities)
        output.set_capacity(self.capacity)
        output.balayage(output.capacity, output.quantity)
        output.tour_per_camion()
        self.camions = output.camion_tour
        self.output = output
        return self

    def run_blayage_type2(self):
        output = vb.VNS_Optimizer(self.clients,250,50,1000)
        output.set_quantity_pd(self.quantities)
        output.set_capacity(self.capacity)
        output.balayage(output.capacity, output.quantity)
        output.tour_per_camion()
        self.camions = output.camion_tour
        self.output = output
        return self


class Optimisation():
    def __init__(self, methode, data):
        self.output=None
        self.data = data
        if methode==None or data==None:
            self.output = "methode or data not provided"
        elif methode=="vns":
            self.run_vns()
        # elif methode=="cw":
        #     self.run_cw()
        else:
            self.output = "method not supported"
    
    def run_vns(self,max_attempts=25, neighbourhood_size=5, iterations=150):
        INPUT_vns = self.data.clients    #input is entropot first with name, attitude and latitude folowed by the rest of the clients
        
        self.output_coords = vns.VNS_Optimizer(INPUT_vns,max_attempts=max_attempts,
                                                neighbourhood_size=neighbourhood_size, 
                                                iterations=iterations).get_otp_coords()
        self.output = "optimisaion done"

class Data():
    def __init__(self,title="no title"):
        self.title = title
        self.clients  = None
        self.expedition = None
    def set_client_csv(self,csv, separetor='\t'):
        dataset_coordinates = pd.read_csv(csv, sep = separetor)
        self.clients = dataset_coordinates.values
        self.names=[i[0] for i in self.clients]
        self.coords = np.asarray([[i[1], i[2]] for i in self.clients])
        return self
    # def set_client_db(self.db):
    #     #read db and fill the llist of clients
    def get_clients_data(self):
        return self.clients    
    
    def set_expedtion_csv(self, csv, separetor=','):
        dataset_coordinates = pd.read_csv(csv, sep = separetor)
        self.expedition = dataset_coordinates.values
        return self  

    def get_expedition_data(self):
        return self.expedition  
    

    # def set_expedition_csv(self,csv,separetor='\t'):
    #     dataset_coordinates = pd.read_csv(csv, sep = separetor)
    #     self.clients = dataset_coordinates.values
    #     self.names=[i[0] for i in self.clients]
    #     self.coords = np.asarray([[i[1], i[2]] for i in self.clients])
        
    #     return self