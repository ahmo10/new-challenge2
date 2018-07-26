[![Build Status](https://travis-ci.org/ahmo10/new-challenge2.svg?branch=master)](https://travis-ci.org/ahmo10/new-challenge2)
# my app diary

## DESCRIPTION
My-diary-api is a restful api intended to communicate with a front end of your choice using various api endpoints. The api endpoints are meant to do the following

- post entries from a user
- fetch entries from the user entries
- delete an entry from entries
- modify an entry

## AUTHOR
### By Ahmed Ibrahim
## PREREQUISITES
- you require a browser preferably postman/insomnia to test the each endpoint.
- nose2/pytest to test to test if the endpoints are passing the test
- you will need an editor to edit the code
To get this project git clone to your local machine and open the file index.html with your favourite browser
## BUILT WITH
- Flask_restplus
- Flask

# RUNNING THE APPLICATION
- Clone the repository to your local machine by running git clone https://github.com/ahmo10/new-challenge2.git
- navigate to the project directory
- activate the virtual environment by running source venv/bin/activate for Ubuntu users
- install dependencies by running pip install -r requirements.txt
- install flask by running pip install flask
- run the application by python3 app.py
- run the endpoints by python3 test_app.py

## API ROUTES

| Methods        | Url          | Description |
| ------------- |:-------------:| -----:|
| GET     |http://127.0.0.1:5000/api/v1/entries   |  Fetches all diary entries |          
| POST    |http://127.0.0.1:5000/api/v1/entries |  Fetches all diary entries    |
| GET    |http://127.0.0.1:5000/api/v1/entries/</int:id>   |  Creates a new diary entry       |
| PUT     | http://127.0.0.1:5000/api/v1/entries/<int:id>  |   Modifies an entry in the diary       |
| DELETE  | http://127.0.0.1:5000/api/v1/entries/<int:id>  |   Deletes an entry from my Diary |


## TESTING THE APP
Use insomnia or postman to the test the endpoints 

## CONTACT DETAILS
in case of any problems when accesing my site feel free to contact me on ahmo.osmern@gmail.com your feedback will be highly appreciated

