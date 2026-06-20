# URL Shortener API

A simple URL shortening service built with FastAPI and PostgreSQL.
Takes a long URL, returns a short code, and redirects visitors from the short code to the original URL.

## Features
- Shorten any URL into a 6-character code
- Redirect from short code to original URL
- PostgreSQL persistence

## Tech Stack
- FastAPI (Python)
- PostgreSQL + SQLAlchemy ORM
- Pydantic for validation

## API Endpoints

| Method | Endpoint         | Description                          |
|--------|------------------|--------------------------------------|
| POST   | `/shorten`       | Create a short code for a long URL   |
| GET    | `/{short_code}`  | Redirect to the original URL         |

### Example
POST `/shorten`
```json
{ "original_url": "https://example.com/very/long/path" }
```
Response:
```json
{ "short_code": "a3Kf9x", "original_url": "https://example.com/very/long/path" }
```
Then visiting `/a3Kf9x` redirects to the original URL.

## Design Decisions
- **Random 6-char codes**: generated from letters + digits, giving ~56 billion combinations.
- **Unique constraint on short_code**: ensures every code maps to exactly one URL.
- **Indexed short_code**: lookups by code are the most frequent operation, so the column is indexed for speed.

## Running Locally
1. Create a PostgreSQL database
2. Set `DATABASE_URL` in a `.env` file
3. `pip install -r requirements.txt`
4. `uvicorn main:app --reload`
5. Open `http://localhost:8000/docs`