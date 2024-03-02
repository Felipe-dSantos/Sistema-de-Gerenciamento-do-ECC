# Sistema-de-Gerenciamento-do-ECC

## Configuração do Ambiente Virtual 


Crie um novo ambiente virtual Python. Você pode fazer isso usando o módulo `venv` que vem com o Python. Execute o seguinte comando para criar um ambiente virtual chamado `venv`: 
```
python -m venv venv
```

### Ative o ambiente virtual:

- No Windows:

  ```
  .\venv\Scripts\activate
  ```
-  No macOS e Linux:

    ```
    source venv/bin/activate
    ```
## Comandos Django 

 Algumas informações úteis sobre comandos importantes do Django.

Instale as dependências do projeto:

```
pip install -r requirements.txt
```
### Criar um Novo Projeto Django

Para criar um novo projeto Django, utilize o seguinte comando:

``` 
django-admin startproject nome_do_projeto 
```


### Criar uma Nova Aplicação Django

Para criar uma nova aplicação dentro do projeto Django, utilize o seguinte comando:
```
python manage.py startapp nome_da_aplicacao
```

### Rodar o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:
```
python manage.py runserver
```

### Criar as Migrações do Banco de Dados

Após fazer alterações nos seus modelos `(models)`, você precisa criar as migrações para atualizar o banco de dados. Utilize o seguinte comando:
```
python manage.py makemigrations
```
### Aplicar as Migrações

Para aplicar as migrações e atualizar o banco de dados, execute o seguinte comando:
```
python manage.py migrate
```

### Criar um Superusuário

Para criar um superusuário (administrador) para acessar o painel de administração do Django, utilize o seguinte comando e siga as instruções:
```
python manage.py createsuperuser

```
