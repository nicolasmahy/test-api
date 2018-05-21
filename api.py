#!C:\Users\n.mahy\AppData\Local\Programs\Python\Python36\python.exe

import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS
from flask import abort
from flask import make_response
from flask import request
import pickle

# load the model from disk
neigh = pickle.load(open('model.sav', 'rb'))

app = Flask(__name__)
CORS(app)

@app.route('/api/', methods=['GET'])
def get_task():

    if request.args.get('access') != "passwtest":
        abort(404)
    var1 = request.args.get('var1')
    var2 = request.args.get('var2')
    var3 = request.args.get('var3')
    var4 = request.args.get('var4')

    var_id = request.args.get('id');

    input = [[var1, var2, var3, var4]]    
    prediction = neigh.predict(input)
    prediction_int = np.asscalar(np.int16(prediction))
    return jsonify({'prediction': prediction_int, 'id': var_id})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'No access'}), 404)

if __name__ == '__main__':
    app.run(debug=True)



#https://jsfiddle.net/qzn7Lquq/1/




#<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
#<script>
#$(document).ready(function(){
#    $("button").click(function(){

#$.getJSON('http://localhost:5000/api/?var1=6&var2=2&var3=10&var4=4&access=passwtest&id=ns', function(data) {
#console.log(data);
#$("div").append('ID: '+data['id']+'<br>');
#$("div").append('Prediction: '+data['prediction']+'<br><br>');
#});         
#    });
#});
#</script>

#<button>test</button>

#<div></div>