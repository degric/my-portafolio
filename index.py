from flask import Flask, render_template

#app
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def inicio():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(port=5000)
