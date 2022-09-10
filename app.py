#start with 3 basic functions:
#1) GET all
#2) GET by id
#3) POST
#4) PUT
#5) Delete

import process as emp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def get_employee():
    emp_all = emp.get_all_employee()
    return jsonify(emp_all)

app.run(debug=True)