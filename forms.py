from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField


class ProgramForm(FlaskForm):
    program = TextAreaField(
        "台山话program",
        default="",
        render_kw={"rows": 10},
    )
    submit = SubmitField("Transpile")
