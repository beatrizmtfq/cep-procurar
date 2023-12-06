from flask import Flask, render_template, request
from controllers.controllers import search_endereco_by_cep 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search_query']
        data = search_endereco_by_cep(search_query)
        return render_template('index.html', data=data)

    return render_template('index.html', data=[])

if __name__ == '__main__':
    app.run(debug=True)