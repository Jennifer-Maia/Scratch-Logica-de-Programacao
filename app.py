from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.secret_key = 'segredo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    didatica = db.Column(db.String(10), nullable=False)
    mais_aulas = db.Column(db.String(10), nullable=False)
    conteudo = db.Column(db.String(10), nullable=False)
    exercicios = db.Column(db.String(10), nullable=False)
    dificuldades = db.Column(db.String(200), nullable=False)
    divertido = db.Column(db.String(200), nullable=False)

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/programacao')
def programacao():
    return render_template('programacao.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Professor.query.filter_by(username=username, password=password).first()
        if user:
            session['user'] = username
            session['type'] = 'professor'
            return redirect(url_for('professor'))

        user = Aluno.query.filter_by(username=username, password=password).first()
        if user:
            session['user'] = username
            session['type'] = 'aluno'
            return redirect(url_for('aluno'))

        error = "Nome de usuário ou senha inválidos"
        return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/professor')
def professor():
    if 'user' in session and session.get('type') == 'professor':
        return render_template('professor.html')
    else:
        return redirect(url_for('login'))

@app.route('/aluno')
def aluno():
    if 'user' in session and session.get('type') == 'aluno':
        return render_template('aluno.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('type', None)
    return redirect(url_for('home'))

@app.route('/semana/<int:numero>')
def semana(numero):
    if 'user' in session:
        template_name = f'semana{numero}.html'
        return render_template(template_name)
    else:
        return redirect(url_for('login'))
    
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Captura dos dados do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        didatica = request.form['didatica']
        mais_aulas = request.form['mais_aulas']
        conteudo = request.form['conteudo']
        exercicios = request.form['exercicios']
        dificuldades = request.form['dificuldades']
        divertido = request.form['divertido']

        # Criação de um novo objeto Feedback
        novo_feedback = Feedback(nome=nome, idade=idade, didatica=didatica,
                                 mais_aulas=mais_aulas, conteudo=conteudo,
                                 exercicios=exercicios, dificuldades=dificuldades,
                                 divertido=divertido)

        # Adiciona ao banco de dados
        db.session.add(novo_feedback)
        db.session.commit()

    return render_template('feedback.html')

@app.route('/resultados')
def resultados():
    feedbacks = Feedback.query.all()
    return render_template('resultados.html', feedbacks=feedbacks)
    
if __name__ == '__main__':
    app.run(debug=True)
