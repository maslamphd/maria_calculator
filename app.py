from flask import Flask, render_template, request
import socket
from datetime import datetime

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
today = datetime.today()

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    
    #writing to the logFile
    f = open("logFile.txt", "a")
    f.write(repr(var_1) + " " + repr(operation) + " " + repr(var_2) + " = " + repr(result) + " Host:" + repr(ip_address) + " Date-Time:" + repr(today.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
    f.close()
    
    return render_template('result.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
