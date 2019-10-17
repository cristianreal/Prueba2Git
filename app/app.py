import urllib, json
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    titulo = "Sistemas Operativos"
    usuario = {'nombre': 'Christian'}
    return render_template('index.html', titulo=titulo, usuario=usuario)


@app.route('/prueba', methods=['GET'])
def Prueba():
	if request.method == 'POST'
		url = "https://opensource.adobe.com/Spry/data/json/donuts.js"
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		print(data)
		#headers = {'Content-type': 'application/json'}
		return "Hola hermoso"
	return render_template('Button.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')