# Attendance Tracker - AI Agent Guidelines

## Project Overview
This is a Python-based attendance tracking system using Flask backend with MySQL database. The project uses QR code generation for attendance tracking and provides CORS-enabled API endpoints.

## Architecture

### Technology Stack
- **Backend**: Flask web framework
- **Database**: MySQL (credentials stored in environment variables, see `.venv/db.py`)
- **Utilities**: 
  - `qrcode` - QR code generation for attendance links
  - `Pillow` - Image processing for QR codes
  - `Flask-CORS` - Cross-origin request handling
  - `python-dotenv` - Environment variable management
  - `gunicorn` - Production WSGI server

### Project Structure
```
.
├── attandancce.py          # Main application entry point (currently contains dependency list)
├── .venv/
│   └── db.py              # MySQL connection utility
└── .github/
    └── copilot-instructions.md
```

## Key Patterns & Conventions

### Database Connection Pattern
The `db.py` module exports a `get_db()` function that returns a MySQL connector instance. Always use this for database operations:
```python
from db import get_db
conn = get_db()
cursor = conn.cursor()
# Execute queries
cursor.close()
conn.close()
```

**Important**: MySQL password is currently hardcoded in `db.py`. Before production, migrate to environment variables using `python-dotenv`.

### Environment Configuration
The project uses `python-dotenv` for secrets management. Create a `.env` file in the project root with:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=<your_password>
MYSQL_DB=attendance_db
FLASK_ENV=development
```

### API Design
- Flask endpoints should include CORS decorators: `@cross_origin()`
- Responses should be JSON with consistent error handling
- QR codes should be generated and stored for later attendance scanning

## Development Workflow

### Setup
1. Virtual environment is configured (`.venv/` exists)
2. Install dependencies: `pip install Flask mysql-connector-python qrcode Pillow Flask-CORS python-dotenv gunicorn`
3. Ensure MySQL server is running and `attendance_db` database exists
4. Configure `.env` with database credentials

### Running the Application
- **Development**: Flask development server (typically `python -m flask run`)
- **Production**: Use gunicorn for deployment
- **Database**: Ensure MySQL is accessible at localhost with configured credentials

### Important Notes
- Typo in filename: `attandancce.py` (likely should be `attendance.py`)
- QR code functionality requires image file storage directory to be defined
- CORS is explicitly enabled, suggesting frontend/backend separation

## Extending the Project
When adding features:
1. Database operations go through `db.get_db()` connection utility
2. New Flask routes should include appropriate CORS decorators
3. QR code generation should use the `qrcode` library with `Pillow` for image output
4. Use environment variables via `python-dotenv` for all configuration
5. Consider adding Flask blueprints as the API grows
