# Task Manager API — Prueba Técnica

API REST de gestión de tareas construida con **FastAPI + SQLAlchemy + SQLite**.

## Requisitos

- Python 3.11+

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar la API

```bash
uvicorn app.main:app --reload
```

Documentación interactiva disponible en: http://localhost:8000/docs

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | /tasks/ | Crear tarea |
| GET | /tasks/ | Listar tareas (filtro: `?status=`) |
| GET | /tasks/{id} | Obtener tarea por ID |
| PATCH | /tasks/{id} | Actualizar tarea parcialmente |
| DELETE | /tasks/{id} | Eliminar tarea |

**Valores válidos para `status`:** `pending`, `in_progress`, `done`  
**Valores válidos para `priority`:** `1` (baja) a `5` (alta)

## Tu misión

Esta API contiene comportamientos incorrectos. Tu tarea es:

1. Identificar todos los problemas en el código.
2. Corregirlos.
3. Verificar tus correcciones ejecutando los tests:

```bash
python -m pytest tests/ -v
```

Los 3 tests deben pasar para completar el desafío.

**No se permite el uso de inteligencia artificial.**

## Arquitectura

```
app/
├── main.py            # Entry point
├── database.py        # Configuración SQLAlchemy
├── dependencies.py    # Inyección de dependencias
├── models/            # Modelos ORM
├── schemas/           # Esquemas Pydantic
├── repositories/      # Acceso a datos
├── services/          # Lógica de negocio
└── routers/           # Endpoints HTTP
```
