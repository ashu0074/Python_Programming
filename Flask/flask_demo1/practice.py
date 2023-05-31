
""" GET and POST --> BOTH Has been used to get data 
GET-> get is used during the url and it is not secure one in this we can easily see the input in the url, 
eg- web searching 

Post-> Post is used in the body in which it is more secure and encripted one
eg- login or sign in time, at that point it seccure our password  """




from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# @app.route --- route to the local system


@app.route('/+postman_try', methods = ['POST'])
def calculator_via_postman():
    if (request.method =='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation == 'add'):
            r = num1+num2
            result = "the sum of "+ str(num1)+"and"+str(num2)+ 'is'+str(r)

        if(operation == 'sub'):
            r = num1-num2
            result = 'the sub of '+ str(num1)+'and'+ str(num2)+'is'+str(r)

        return jsonify(result)
    


@app.route('/try2', methods = ['POST'])
def math_try():
    if(request.method =="POST"):
        num0 = int(request.json['num0'])
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        result = num0+num1+num2

        return jsonify(result)


# URL calling ---> using "GET"
@app.route('/Flask_URL_function')
def url_test():
    test1 = request.args.get('val1')
    test2  = request.args.get('val2')
    test3 = int(test1)+int(test2)

    return """<h1> my result is {}</h1>""".format(test3)



if __name__ == '__main__':
    app.run()

