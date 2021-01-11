from django import forms
from django.contrib.auth.forms import AuthenticationForm
from webhooks.models import Users


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUser(forms.ModelForm):
    """ Formulario de registro de un Usuario en la base de datos

    variables:

        - Password1: Contraseña
        - password2: Verificación de la contraseña

    """
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Users
        fields = ('email', 'name', 'date_of_birth', 'gender', 'country')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese su name',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese su date_of_birth',
                }
            ),
            'gender': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese su gender',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese su country',
                }
            ),
        }

    def clean_password2(self):
        """ Validación de contraseña

        Método que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadaa en la base de datos, Retornar la contraseña válida.

        Excepciones:
        -validationError -- cuando las contraseñas no son iguales muestra un mensaje de error

        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
