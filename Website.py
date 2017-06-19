from flask import Flask, render_template
from Website_Db import DbClass
import os

app = Flask(__name__)


@app.route('/')
# De hoofdpagina van de wabsite
def index():
    return render_template('index.html')

@app.route('/tabellen')
#De tabellen met verschillende gegevens
def tabellen():
    #DB_layer = DbClass()
    #list_products = DB_layer.getcollection()
    return render_template('tabellen.html')


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error.html", error =error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)
