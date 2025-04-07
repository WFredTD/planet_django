""""
Para criar um banco usamos o comando no terminal:
    python manage.py migrate

Para criarmor o primeiro usuário temos que fazer pelo terminal também, após o primeiro
usuário criado, podemos criar outros usuários pelo admin do django
O comando é o seguinte:
    python manage.py createsuperuser
O superuser é o usuário administrador do django, ele tem acesso a todas as funcionalidades do admin do django

Usando o shell do django, podemos por exemplo, acrescentar uma imagemno banco, os comandos são os seguintes:
    python manage.py shell
    from galeria.models import Fotografias
    foto = Fotografias(nome="planeta shell",legenda=" o shell se abrindo",descricao="o shell se abrindo",foto="planeta_shell.jpg") 
    foto.save()
    Fotografias.objects.all()

Existe um comando pelo shell para deletar o objeto, caso nescessite. Primeiro tenho pegar o ID do objeto que quero deletar, depois usar o comando delete, o comando é o seguinte:
    foto = Fotografias.objects.get(pk=1)
    foto.delete()
    Fotografias.objects.all()

Tembém existe uma forma de fazer um "update" na tabela, ou seja, alterar os dados do objeto, o comando é o seguinte:
    foto = Fotografias.objects.get(pk=1)
    foto.nome = "planeta shell alterado"
    foto.save()

"""