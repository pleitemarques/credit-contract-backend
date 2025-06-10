# 📄 Credit Contract Backend

API para gerenciamento de contratos de crédito pessoal, desenvolvida como parte do case técnico para a vaga de Desenvolvedor Backend na **Guardian Gestora**.

---

## 🚀 Stack utilizada

- **Python 3.12**
- **Django + DRF**
- **PostgreSQL**
- **Docker + Docker Compose**
- **drf-spectacular** (Swagger)
- **django-filter**
- **Poetry**

---

## 📦 Como rodar o projeto com Docker

```bash
docker compose up --build
```

Acesse:

- 🟢 App: [http://localhost:8001](http://localhost:8001)
- 📘 Swagger: [http://localhost:8001/api/schema/swagger-ui/](http://localhost:8001/api/schema/swagger-ui/)
- 🐘 PGAdmin: [http://localhost:5050](http://localhost:5050)

---

## ⚙️ Variáveis de ambiente (.env)

```env
SECRET_KEY=django-insecure-...
DEBUG=True
DB_NAME=credit_contract_database
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=postgres
DB_PORT=5432
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
```

---

## 🔄 Endpoints disponíveis

### 🔹 Contratos

| Método | Endpoint               | Descrição                                 |
|--------|------------------------|-------------------------------------------|
| POST   | `/api/contracts/`      | Cadastra contrato com parcelas e endereço |
| GET    | `/api/contracts/`      | Lista contratos com filtros               |
| GET    | `/api/contracts/{id}/` | Detalha um contrato específico            |

#### Filtros disponíveis:
- `external_id`
- `borrower_document`
- `emission_date` (com suporte a `year`, `month`, `day`)
- `borrower_address__state`

---

### 🔹 Resumo dos contratos

| Método | Endpoint                  | Descrição                                                |
|--------|---------------------------|------------------------------------------------------------|
| GET    | `/api/contracts/summary/` | Retorna totais consolidados com base em filtros opcionais |

#### Parâmetros de filtro:
- `borrower_document` – Documento do tomador
- `emission_date` – Data de emissão do contrato
- `borrower_state` – Estado de residência do tomador

#### Exemplo de resposta:
```json
{
  "total_receivable_amount": "10250.00",
  "total_disbursed_amount": "10000.00",
  "total_contracts": 1,
  "average_contract_rate": "2.5"
}
```

---

## 📥 Exemplo de payload para criação de contrato

```json
{
  "external_id": "abc123",
  "emission_date": "2024-06-01",
  "amount": 10000.00,
  "rate": 2.5,
  "borrower_document": "12345678901",
  "borrower_birthdate": "1990-01-01",
  "borrower_phone": "5511999999999",
  "borrower_address": {
    "country": "Brasil",
    "state": "SP",
    "city": "São Paulo",
    "neighborhood": "Centro",
    "street": "Rua Exemplo",
    "number": "123",
    "complement": "Apto 101",
    "postal_code": "01234-567"
  },
  "installments": [
    {
      "number": 1,
      "amount": 5125.00,
      "due_date": "2024-07-01"
    },
    {
      "number": 2,
      "amount": 5125.00,
      "due_date": "2024-08-01"
    }
  ]
}
```

---

## 🔐 Autenticação

Atualmente a API permite acesso livre (`AllowAny`). Em produção, recomenda-se adicionar OAuth2, JWT ou outro método seguro.

---

## 📚 Documentação da API

Documentação automática gerada com **drf-spectacular**:

- Swagger UI: [`/api/schema/swagger-ui/`](http://localhost:8001/api/schema/swagger-ui/)
- Redoc: [`/api/schema/redoc/`](http://localhost:8001/api/schema/redoc/)
- YAML: [`/api/schema/`](http://localhost:8001/api/schema/)

---

## ✅ Status

- [x] Cadastro de contratos com parcelas e endereço
- [x] Filtros com `django-filter`
- [x] Endpoint de resumo consolidado
- [x] Documentação Swagger
- [x] Docker completo com PostgreSQL e PGAdmin

---

## ✉️ Envio

Este projeto foi desenvolvido por **Pedro Marques** como parte do processo seletivo da Guardian Gestora.

---