from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome completo:', [validators.Length(min=4, max=25)])
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha:', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repita sua senha')

class LoginFormulario(Form):
    email = StringField('Email:', [validators.length(min=6, max=35)])
    password = PasswordField('Senha', [validators.DataRequired()])