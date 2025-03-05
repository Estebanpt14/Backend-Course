# FastAPI User and Product Management API

## Descripción
Este proyecto es una API construida con FastAPI para la gestión de usuarios y productos. Incluye autenticación con OAuth2, manejo de base de datos en MongoDB, y endpoints para CRUD de usuarios y productos.

## Tecnologías Utilizadas
- FastAPI
- Pydantic
- OAuth2 con JWT
- MongoDB
- PyMongo
- Passlib para hashing de contraseñas

## Instalación
1. Crear un entorno virtual y activarlo:
   ```sh
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```
2. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Configurar la conexión a MongoDB en `db/client.py`.

## Uso
### Iniciar la API
```sh
uvicorn main:app --reload
```
La API estará disponible en `http://127.0.0.1:8000`.

### Endpoints
#### Usuarios
- **POST /:** Crear usuario
- **GET /{item_id}:** Obtener usuario por ID
- **GET /:** Obtener todos los usuarios
- **POST /login:** Autenticación de usuario con OAuth2

#### Productos
- **GET /productos/** Listar todos los productos

## Autenticación
La API usa OAuth2 con JWT. Para autenticarse:
```sh
curl -X POST "http://127.0.0.1:8000/login" -d "username=manu&password=1234wasd"
```
Esto devuelve un token de acceso que se debe incluir en los headers de las peticiones protegidas:
```sh
Authorization: Bearer <token>
```
