# 📚 Library API

API REST de uma biblioteca, construída com **Django** e **Django REST Framework (DRF)**.

Este é um projeto de **estudo**: a ideia é aprender o DRF na prática, evoluindo a API passo a passo. No final, um **cliente em React JS** vai consumir esta API.

---

## 🎯 Objetivos

- Entender como o Django e o DRF se organizam (models, serializers, viewsets, routers)
- Modelar uma biblioteca com relacionamentos entre entidades
- Aplicar validação, paginação, filtros, autenticação e permissões
- Documentar a API e deixá-la pronta para um frontend React consumir

---

## 🛠️ Tecnologias

| Camada   | Tecnologia                     |
| -------- | ------------------------------ |
| Backend  | Python 3, Django 6.1, DRF 3.18 |
| Banco    | SQLite (desenvolvimento)       |
| Frontend | React JS *(planejado)*         |

---

## 🚀 Como rodar

```sh
# 1. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Instale as dependências
pip install django djangorestframework

# 3. Crie as tabelas no banco
python manage.py makemigrations
python manage.py migrate

# 4. (Opcional) Crie um usuário para o admin
python manage.py createsuperuser

# 5. Suba o servidor
python manage.py runserver
```

A API fica disponível em: **http://127.0.0.1:8000/api/**

---

## 🔌 Endpoints

| Método    | Rota               | Descrição               |
| --------- | ------------------ | ----------------------- |
| GET       | `/api/books/`      | Lista todos os livros   |
| POST      | `/api/books/`      | Cria um livro           |
| GET       | `/api/books/<id>/` | Detalha um livro        |
| PUT/PATCH | `/api/books/<id>/` | Atualiza um livro       |
| DELETE    | `/api/books/<id>/` | Remove um livro         |
| —         | `/admin/`          | Painel admin do Django  |

Exemplo de livro:

```json
{
  "id_book": "3f1c2a9e-8b7d-4e2f-9a61-0c5d7e8f1a23",
  "title": "O Senhor dos Anéis",
  "author": "J. R. R. Tolkien",
  "publication_date": "1954-07-29",
  "editoras": "HarperCollins"
}
```

---

## 🗺️ Roadmap de estudo

### 🟢 Nível 1: Fundamentos
- [x] Criar o projeto Django e o app `books`
- [x] Criar o model `Books`
- [x] Criar o serializer, o viewset e o router
- [x] Gerar e aplicar as migrations
- [ ] Explorar a API navegável do DRF (CRUD completo)
- [ ] Registrar o model no admin
- [ ] Adicionar `__str__` ao model

### 🟡 Nível 2: Model e validações
- [ ] Revisar a nomenclatura dos campos
- [ ] Validações no serializer (ex.: data de publicação no futuro)
- [ ] Trocar `fields = '__all__'` por campos explícitos

### 🟠 Nível 3: Relacionamentos
- [ ] Model `Author` com `ForeignKey` em `Books`
- [ ] Model `Publisher` (editora)
- [ ] Endpoints de autores e editoras
- [ ] Serializers aninhados

### 🔴 Nível 4: API de verdade
- [ ] Paginação
- [ ] Filtros, busca e ordenação
- [ ] Autenticação e permissões
- [ ] Testes automatizados com `APITestCase`
- [ ] CORS configurado para o frontend

### 🟣 Nível 5: Extras
- [ ] Sistema de empréstimos
- [ ] Avaliações de livros
- [ ] Documentação com Swagger (`drf-spectacular`)

### ⚛️ Frontend
- [ ] Cliente em React JS consumindo a API (listar, cadastrar, editar e remover livros)

---

## 📖 Referências

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Django REST Framework](https://www.django-rest-framework.org/)
- [Documentação do React](https://react.dev/)
