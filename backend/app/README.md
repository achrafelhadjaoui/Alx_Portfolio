# BookBuddy Backend

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with the following:
    ```
    SECRET_KEY=your_secret_key
    DATABASE_URL=sqlite:///site.db
    ```
3. Run migrations: `flask db upgrade`
4. Start the server: `python run.py`

## Endpoints

- **POST /api/register**: Register a new user.
- **POST /api/login**: Authenticate a user and get a JWT token.
- **POST /api/users/<id>/books**: Add a new book for the user.
- **GET /api/users/<id>/books**: List all books for the user.
