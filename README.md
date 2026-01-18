# 🔐 NovaScale Auth

Un microservicio de autenticación con detección de anomalías.  
Diseñado para ser **escalable, seguro y desplegable**.

## 🚀 Features

- Registro y login con JWT (JSON Web Tokens).
- Validación de datos robusta con Pydantic y SQLModel.
- Detección de anomalías integrada (arquitectura lista para ML).
- Testing automatizado con Pytest.
- Gestión de dependencias moderna con `uv`.

## 🛠️ Stack

- **Backend**: FastAPI
- **Base de datos**: PostgreSQL (SQLModel)
- **Seguridad**: Passlib (bcrypt), PyJWT
- **Testing**: Pytest
- **Tooling**: `uv`, Ruff
- **Lenguaje**: Python 3.14+

## 📦 Requisitos

- Python 3.14+
- `uv` (https://github.com/astral-sh/uv)
- PostgreSQL (local o remoto)

## ▶️ Iniciar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/danielpcar9/novascale-auth.git
cd novascale-auth

# 2. Crear entorno virtual e instalar dependencias
uv sync

# 3. Configurar variables de entorno (Opcional por ahora)
# El servicio usa una DATABASE_URL por defecto en app/database.py

# 4. Correr la aplicación
uv run uvicorn app.main:app --reload
```

## 🧪 Testing

Para ejecutar los tests automatizados:

```bash
export PYTHONPATH=$PYTHONPATH:.
pytest
```

## 🏗️ Estructura del Proyecto

- `app/api/`: Endpoints de la API (v1).
- `app/models/`: Definición de modelos de datos y schemas.
- `app/services/`: Lógica de negocio y autenticación.
- `app/ml/`: Componentes de Machine Learning (detección de anomalías).
- `tests/`: Pruebas unitarias y de integración.
