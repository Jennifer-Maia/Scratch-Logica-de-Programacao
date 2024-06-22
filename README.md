# Introdução à Lógica de Programação com Scratch

Este repositório contém materiais e código fonte do curso "Introdução à Lógica de Programação com Scratch", que abrange desde a configuração básica até projetos mais avançados utilizando a plataforma Scratch.

## Visão Geral

O curso é projetado para ensinar fundamentos de programação de forma prática e interativa, utilizando o ambiente visual do Scratch. Inclui lições semanais, exemplos de código, atividades práticas e projetos colaborativos.

## Estrutura do Projeto

### Arquivos Principais

- **base.html**: Template HTML base utilizado em todas as páginas do site do curso.
- **app.py**: Aplicação Flask que gerencia o site do curso, incluindo rotas, autenticação e interação com o banco de dados.
- **db_create.py**: Script Python para criar e popular o banco de dados SQLite com dados iniciais de professores, alunos e feedbacks.
- **static/**: Pasta contendo arquivos estáticos como CSS e imagens utilizados no site.
- **templates/**: Pasta contendo os templates HTML das diferentes páginas do site.

### Funcionalidades Implementadas

- **Autenticação de Usuários**: Professores e alunos podem fazer login para acessar áreas específicas do site.
- **Feedbacks**: Os alunos podem enviar feedbacks sobre o curso, que são armazenados no banco de dados.
- **Resultados**: Visualização dos feedbacks coletados pelo professor.

### Banco de Dados SQLite

O projeto utiliza SQLite como banco de dados para armazenar informações de login e feedbacks dos alunos. As tabelas principais são:

- **Professor**: Armazena dados de login dos professores.
- **Aluno**: Armazena dados de login dos alunos.
- **Feedback**: Armazena feedbacks enviados pelos alunos.

## Como Executar

Para executar o projeto localmente, siga os passos abaixo:

1. **Clonar o repositório**:

   ```bash
   git clone https://github.com/Jennifer-Maia/Scratch-Logica-de-Programacao.git
   cd Scratch-Logica-de-Programacao

