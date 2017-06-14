from flask import Flask,render_template
from Website_Db import  DbClass

app = Flask(__name__)


@app.route('/')
# De hoofdpagina van de wabsite
def index():
    return render_template('index.html')

@app.route('/tabellen')
#De tabellen met cerschillende gegevens
def collection():
    DB_layer = DbClass()
    list_products = DB_layer.getcollection()
    return render_template('collection.html', products=list_products)


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error.html", error =error)


if __name__ == '__main__':
    app.run()
