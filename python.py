from flask import Flask, render_template

# Criar uma instância do Flask
app = Flask(__name__)

# Definir uma rota (URL)
@app.route('/')
def home():
    return render_template('index.html')

# Rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)