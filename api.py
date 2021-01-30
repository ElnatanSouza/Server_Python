from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    else:
        return 'Você esta acessando por outro Metodo'

@app.route('/<int:id>')
def homeId(id):
    return str(id + 1)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')


app.run(debug=True)
