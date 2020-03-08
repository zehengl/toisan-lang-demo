import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from toisan_lang import parse
from whitenoise import WhiteNoise

from forms import ProgramForm


app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


def transpile(program):
    try:
        code, _ = parse(program)
    except:
        code = None

    return code


@app.route("/", methods=["get", "post"])
def index():
    form = ProgramForm(request.form)

    python_code = transpile(form.program.data)

    if python_code:
        num_lines = len(python_code.split("\n"))
    else:
        num_lines = 0

    return render_template(
        "index.html", form=form, python_code=python_code, num_lines=num_lines
    )


if __name__ == "__main__":
    app.run(debug=True)
