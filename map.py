
from flask import Flask, render_template

import folium
import haversine as hs                      #these two import are only necessery during the test, later they will be uneccesery 
from haversine import Unit
from algo import cw, vns
# import map
Test = True
# if Test:
#     fake_data = "clt1_rabat Latitude: 34.0128 Longitude: -6.8314    clt2_rabat Latitude: 34.0623 Longitude: -6.7889   clt3_rabat Latitude: 33.9371 Longitude: -6.9028   clt4_rabat Latitude: 33.9354 Longitude: -6.8081   clt5_casa Latitude: 33.5998 Longitude: -7.6321   clt7_casa Latitude: 33.6060 Longitude: -7.5620   clt8_casa Latitude: 33.5872 Longitude: -7.5229   clt9_casa Latitude: 33.5500 Longitude: -7.6891   clt10_casa Latitude: 33.5368 Longitude: -7.6829   clt11_casa Latitude: 33.5895 Longitude: -7.6128   clt12_fez Latitude: 34.0041 Longitude: -5.0350   clt13_fez Latitude: 34.0561 Longitude: -5.0455   clt14_mkech Latitude: 31.6680 Longitude: -8.0228   clt15_mkech Latitude: 31.6516 Longitude: -8.0653   clt16_mkech Latitude: 31.6183 Longitude: -8.0653   clt17_tanger Latitude: 35.7799 Longitude: -5.8059   clt18_tanger Latitude: 35.7613 Longitude: -5.7817   clt19_tanger Latitude: 35.7414 Longitude: -5.7948   clt20_tetouan Latitude: 35.5677 Longitude: -5.4097"
#     A = fake_data.split()
#     Entropot = ('INPT',33.9794, -6.8673)
#     Client=  [ (A[5*i],float(A[5*i+2]),float(A[5*i+4]) ) for i in range(19)]
#     Client
#     INPUT = [(i+1, Entropot[0], Client[i][0],Entropot[1],Entropot[2],Client[i][1],Client[i][2], hs.haversine((Entropot[1],Entropot[2]),(Client[i][1],Client[i][2]),unit=Unit.METERS) ) for i in range(19)]
    
# if Test:
#     my_input = cw.Distance_matrice(INPUT)
#     my_input.preprocess()
#     my_input.count_saving()
#     my_input.sort()[0][0]
#     #a[0].getname()
#     my_input.optimise()
#     # param1 = my_input.display_route()
#     coords = my_input.get_route_coords()
#     # map.rendermap(coords)

app = Flask(__name__)
# m = folium.Map(location=coords[0], tiles="OpenStreetMap", zoom_start=6)

# def rendermap():
    

@app.route('/map')
def render_map(coords=None):
    if coords==None:
        return None
    m = folium.Map(location=coords[0], tiles="OpenStreetMap", zoom_start=6)
    # Ajout d'un marqueur
    folium.Marker([34.020882, -6.831650],
                  popup="Rabat",
                  icon=folium.Icon(color='green')).add_to(m)

    folium.Marker([31.669746,-7.973328],
                  popup='Marrakech',
                  icon=folium.Icon(color='Yellow')).add_to(m)
    # Ajout d'une ligne à partir de 5 points
    points = coords
    folium.PolyLine(points, color="blue", weight=2.5, opacity=0.8).add_to(m)
    # return m
    m.save('templates/map.html')
    return render_template('map.html')

if __name__ == '__main__':
    
    # m = rendermap(coords)
    app.run(debug=True)