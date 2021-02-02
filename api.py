from flask import Flask, render_template, request
import tkinter

janela = tkinter.Tk()
janela.geometry('400x300')

etiqueta = tkinter.Label(
    janela, text='Olá, Seja bem vindo! \n \n Para acessar minha atividade abra o navegador e digite: \n \n localhost:5000 ', bg='#B0E0E6', font = 'Calibri')
etiqueta.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)


janela.mainloop()


app = Flask(__name__, template_folder='./src/views')


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    else:
        if (request.form['num1'] != '' and request.form['num2'] != ''):
            num1 = request.form['num1']
            num2 = request.form['num2']

            if (request.form['opc'] == 'soma'):
                soma = int(num1) + int(num2)
                return {
                    'Resultado': str(soma)
                }

            elif(request.form['opc'] == 'subt'):
                subt = int(num1) - int(num2)
                return {
                    'Resultado': str(subt)
                }

            elif(request.form['opc'] == 'mult'):
                mult = int(num1) * int(num2)
                return {
                    'Resultado': str(mult)
                }

            else:
                divi = int(num1) / int(num2)
                return {
                    'Resultado': str(divi)
                }

        else:
            return {
                'Erro': 'É necessário digitar os dois valores!'
            }


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')


app.run(debug=True)
