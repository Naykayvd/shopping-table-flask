from flask import Flask, render_template, request

app = Flask(__name__)
shopping_items = {"apples": 2, "bananas": 1.70, "eggs": 6, "chicken": 50}


@app.route('/')
def log():
    return render_template('login1.html')


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['username']
    passwrd = request.form['userpass']
    if uname == "nahum" and passwrd == "1234":
        return "Welcome %s" % uname + request.method
    else:
        return "Error in logging in" + request.method


@app.route('/shopping')
def shop():
    return render_template('showitems.html')


@app.route('/showitems', methods=['POST'])
def showshop():
    if request.method == 'POST':
        result = request.form
        return render_template('shoppinglist.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
