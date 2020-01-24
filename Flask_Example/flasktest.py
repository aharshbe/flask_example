from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/score/<int:score>')
def display_pass_fail(score):
   return render_template('score.html', marks = score)

@app.route('/table')
def result():
   dict = {'Dakota':"is cool",'Austin':"22",'maths':70}
   return render_template('table.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
