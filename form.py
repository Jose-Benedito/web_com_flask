from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('nome completo', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite sua senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repita sua senha')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])