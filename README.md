# divorce_predictor
Machine learning application Devorce predit

# Please note: PIP dependency management tool need to be installed in the computer
# Open terminal or CMD from this folder and type pip install -r requirements.txt
# Once the libraries have installed, type python app.py
# Then the app server will be started.
# To test, run this curl

# linux or mac
  curl -XPOST -H "Content-type: application/json" -d '[1, 1, 0, 0, 0, 1, 0, 0, 1, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 0]' 'http://127.0.0.1:5000/api/v1/divorce/predict'

# windows
  curl -i -X POST -H "Content-Type:application/json" -d "[1, 1, 0, 0, 0, 1, 0, 0, 1, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 0]" http://127.0.0.1:5000/api/v1/divorce/predict

# postman 
  url          - http://127.0.0.1:5000/api/v1/divorce/predict
  method       - POST
  request data - [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

