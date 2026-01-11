from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from qr_generator import generate_attendance_qr, generate_batch_qr_codes

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/create-attendance', methods=['POST'])
@cross_origin()
def create_attendance():
    """Create attendance session with QR code"""
    try:
        data = request.get_json()
        class_id = data.get('class_id')
        student_ids = data.get('student_ids', [])  # List of student IDs
        
        # Generate QR codes for all students
        attendance_url = request.host_url + 'student/mark-attendance'
        qr_codes = generate_batch_qr_codes(student_ids, class_id, attendance_url)
        
        return jsonify({
            'message': 'Attendance session created',
            'status': 'success',
            'qr_codes': qr_codes
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@teacher_bp.route('/view-attendance/<session_id>', methods=['GET'])
@cross_origin()
def view_attendance(session_id):
    """View attendance records for a session"""
    try:
        # TODO: Fetch attendance records from database
        return jsonify({'message': f'View attendance for session {session_id}', 'status': 'pending'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
