# To run this repo
## first initiat Flask variable 
for windows: 
> setx FLASK_APP 'app/__ init__.py'   
/!\ Remove the space before init__
for MacOs/Linux:
> export FLASK_APP='app/__ init__.py'
/!\ Remove the space before init__

## then run the app

> flask run


## debuging notes
if stuff didn't work check your envirenement variable FLASK_APP, and see if it has he space if it does reset it without space
Also you might have to run 
> flask fab create-admin 
if you dont have it run yet 
