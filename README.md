# py-profile

A lightweight FastAPI service for managing user profile records in MongoDB.

## Author

This project was authored by Dr. Alfonso J. Barroso Barajas

## Overview

`py-profile` is a small backend application that exposes a profile API and stores user data in a MongoDB collection. The project is organized around a simple layered structure:

- `src/main.py` starts the FastAPI application
- `src/controller/profile_controller.py` defines the HTTP routes
- `src/service/profile_service.py` contains the business logic
- `src/model/profile_model.py` defines the request/response schemas
- `src/database/database_connection.py` manages the MongoDB connection
- `src/environment/environment_loader.py` loads environment-specific configuration
- `src/constants/constants.py` holds shared API constants

## Tech stack

- Python 3.14+
- FastAPI
- Pydantic
- Motor (async MongoDB driver)
- Uvicorn
- MongoDB

## Project structure

```text
py-profile/
├── pyproject.toml
├── run.sh
├── README.md
├── src/
│   ├── main.py
│   ├── constants/
│   │   └── constants.py
│   ├── controller/
│   │   └── profile_controller.py
│   ├── database/
│   │   └── database_connection.py
│   ├── environment/
│   │   └── environment_loader.py
│   ├── model/
│   │   └── profile_model.py
│   └── service/
│       └── profile_service.py
└── gists/
```

## API behavior

The service currently exposes a profile endpoint under `/profile`.

### Endpoints

- `GET /profile`  
  Returns an empty list at the moment. This is the read endpoint placeholder for retrieving all profiles.

- `POST /profile`  
  Creates a new user profile. The request body must include:

```json
{
  "user_name": "alice",
  "user_rol": [
    { "rol": "admin" }
  ]
}
```

A successful response returns the new MongoDB record ID:

```json
{
  "id": "<mongo_object_id>"
}
```

## Configuration

The application expects an environment file such as `.env.dev` and reads it through the `ENVIRONMENT` variable.

Example:

```env
ENVIRONMENT=dev
mongodb_url=mongodb://localhost:27017
```

`run.sh` sets the environment to `dev` and launches the application with Uvicorn:

```bash
export ENVIRONMENT=dev
python -m uvicorn src.main:app --port 8000 --reload
```

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

If you are using Poetry or the project metadata from `pyproject.toml`, you can also install the project with:

```bash
pip install .
```

3. Start MongoDB locally.
4. Create a file named `.env.dev` with your MongoDB connection URL.
5. Launch the app:

```bash
./run.sh
```

The API will be available at:

```text
http://localhost:8000
```

## Example request

```bash
curl -X POST "http://localhost:8000/profile" \
  -H "Content-Type: application/json" \
  -d '{
    "user_name": "alice",
    "user_rol": [{"rol": "admin"}]
  }'
```

## Notes

This is a minimal starter project for profile management and is a good base for extending the API with features such as:

- retrieving a single profile by ID
- updating profile data
- deleting profiles
- validation and pagination
- authentication and authorization
- test coverage for controller and service layers

## License

This project does not currently define a license in the repository metadata.
