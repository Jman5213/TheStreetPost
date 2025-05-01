from flask import Flask, render_template

app = Flask(__name__, template_folder='HTML')


@app.route('/')
def main():
    return render_template("home.html", title="Welcome")


@app.route('/login')
def signin():
    return render_template("login.html", title="Sign In")


@app.route('/about')
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run()
