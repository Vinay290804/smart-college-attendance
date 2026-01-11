from flask import Flask, jsonify
import json
from flask_cors import CORS
from routes.auth import auth_bp
from routes.teacher import teacher_bp
from routes.student import student_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret123"

# Enable CORS for all routes
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(teacher_bp, url_prefix="/teacher")
app.register_blueprint(student_bp, url_prefix="/student")

@app.route('/', methods=['GET'])
def home():
    """Health check and API info endpoint"""
    try:
        with open('api_info.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        data = {
            'message': 'Attendance Tracker API',
            'status': 'running',
            'endpoints': {
                'auth': '/auth/login, /auth/register',
                'teacher': '/teacher/create-attendance, /teacher/view-attendance/<session_id>',
                'student': '/student/mark-attendance, /student/view-my-attendance'
            }
        }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
