from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign In')

"""
5.
Создать форму регистрации для пользователя.

Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на обработку персональных данных.
"""
class Registration2Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Сonsent to the processing of user data', validators=[DataRequired()])
    submit = SubmitField('Sign In')

"""
8.
Создать форму для регистрации пользователей на сайте.
"""
class Registration3Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Сonsent to the processing of user data', validators=[DataRequired()])
    submit = SubmitField('Sign In')