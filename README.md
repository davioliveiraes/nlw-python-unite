<h1 align="center">NLW Unite trilha de Python da Rocketseat</h1>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp
  <a href="#-Para-executar-o-projeto">Para executar o projeto</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Flask

## 📚 Principais Bibliotecas

- blinker==1.9.0
- click==8.1.8
- distlib==0.3.9
- filelock==3.18.0
- Flask==3.1.0
- flask-cors==5.0.1
- greenlet==3.1.1
- iniconfig==2.1.0
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- packaging==24.2
- platformdirs==4.3.7
- pluggy==1.5.0
- pytest==8.3.5
- SQLAlchemy==2.0.39
- typing_extensions==4.13.0
- virtualenv==20.29.3
- Werkzeug==3.1.3



## 💻 Projeto

  O projeto foi desenvolvida utilizando Python com o microframework Flask, integradno o ORM SQLAlchemy para gerenciador do banco de dados. O objetivo do sistema é permitir o cadastro de eventos, inscrição de participantes (attendees) e o registro de check-ins durante os eventos.

## 👨‍💻 Para executar o projeto

1. Clone o repositório: `git clone https://github.com/davioliveiraes/nlw-python-unite.git`
2. Entre na pasta do projeto: `cd nlw-python-unite`
3. Ative o ambiente virtual: `source venv/bin/activate (Linux/Ubuntu)`
4. Instale as dependências: `pip3 install -r requirements.txt`
5. Execute o programa: `python3 run.py`
6. Pode baixar o `postman` e executar os seguintes métodos(Exemplo): 
- POST - `http://localhost:3000/events`
- GET - `http://localhost:3000/events/:event_id`
- POST - `http://localhost:3000/events/:event_id/register`
- GET - `http://localhost:3000/attendees/:attendee_id/badge`
- GET - `http://localhost:3000/events/:event_id/attendees`
- POST - `http://localhost:3000/attendees/:attendee_id/check-in`