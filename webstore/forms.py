from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class CustomerLoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('Login')