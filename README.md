# Python Financial Operation
Flask application to handle bank transaction

## How to run application
Create an envfile with the follow key
```bash
DATABASE_URL=postgresql://admin:admin@py_db:5432/your_database
```
Run docker container
```bash
make docker-run
make migrate-up
```

## Import Postman files
```bash
Env.postman_environment.json
financial_transaction.postman_collection.json
```

## Makefile

Create python environment
```bash
make create-env
make activate-env
```

Install dependencies
```bash
make install
```

Running local app
```bash
make run
```

Docker containers
```bash
make docker-run
make docker-down
```

Pytest
```bash
make test
```

Coverage
```bash
make coverage
```

Database migration
```bash
make migrate-up
```

Linting
```bash
make lint
```

Format
```bash
make format
```