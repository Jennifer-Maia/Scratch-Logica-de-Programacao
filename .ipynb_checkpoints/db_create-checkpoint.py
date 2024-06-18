# db_create.py

from app import app, db, Professor, Aluno, Feedback

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

    # Exemplos de professores
    professor1 = Professor(username='professor1', password='1234')
    professor2 = Professor(username='professor2', password='1234')
    professor3 = Professor(username='professor3', password='1234')
    professor4 = Professor(username='professor4', password='1234')

    # Exemplos de alunos
    aluno1 = Aluno(username='aluno1', password='1234')
    aluno2 = Aluno(username='aluno2', password='1234')
    aluno3 = Aluno(username='aluno3', password='1234')
    aluno4 = Aluno(username='aluno4', password='1234')
    aluno5 = Aluno(username='aluno5', password='1234')
    aluno6 = Aluno(username='aluno6', password='1234')
    aluno7 = Aluno(username='aluno7', password='1234')
    aluno8 = Aluno(username='aluno8', password='1234')
    aluno9 = Aluno(username='aluno9', password='1234')
    aluno10 = Aluno(username='aluno10', password='1234')

    # Adiciona os exemplos ao banco de dados
    db.session.add(professor1)
    db.session.add(professor2)
    db.session.add(professor3)
    db.session.add(professor4)
    db.session.add(aluno1)
    db.session.add(aluno2)
    db.session.add(aluno3)
    db.session.add(aluno4)
    db.session.add(aluno5)
    db.session.add(aluno6)
    db.session.add(aluno7)
    db.session.add(aluno8)
    db.session.add(aluno9)
    db.session.add(aluno10)

    # Commit das adições ao banco de dados
    db.session.commit()

print("Dados de professores e alunos inseridos com sucesso!")
