# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return "This is Homepage"

@app.route('/dashboard')
def dashboard():
    return "<h1>This is my dashboard</h1>"

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hi I am %s</h2>" %username

@app.route('/dashboard/<int:dashboardID>')
def showDashboard(dashboardID):
    return "<h2>The Dashboard ID is %s</h2>" %dashboardID

if __name__ == "__main__":
   app.run(debug=True)

