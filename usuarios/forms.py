from django import forms

# Abaixo temos uma herança de classes, onde a classe LoginForms herda da classe Form.
# Isso significa que LoginForms é uma subclasse de Form e herda todos os métodos e atributos da classe Form.
class LoginForms(forms.Form):
    email_login = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': "form-input", 'placeholder': "Digite seu email"})
    )
    # Acima temos um campo de email, que é um tipo de campo específico para capturar endereços de email.
    # O campo é obrigatório e tem um tamanho máximo de 100 caracteres.
    # O label é o texto que será exibido para o usuário.

    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': "form-input", 'placeholder': "Digite sua senha"})
    )
    # Acima temos um campo de senha, que é um tipo de campo específico para capturar senhas.
    # O campo é obrigatório e tem um tamanho máximo de 70 caracteres.
    # O widget PasswordInput() é usado para ocultar a senha enquanto o usuário a digita.
