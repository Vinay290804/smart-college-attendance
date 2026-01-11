import qrcode
from qrcode.image.styledpil import StyledPilImage
import os
from datetime import datetime

def generate_attendance_qr(student_id, class_id, attendance_url):
    """
    Generate a QR code for attendance tracking
    
    Args:
        student_id: Student ID number
        class_id: Class/Course ID
        attendance_url: Base URL for attendance endpoint
    
    Returns:
        filepath: Path to saved QR code image
    """
    try:
        # Create QR directory if it doesn't exist
        qr_dir = "qr_codes"
        if not os.path.exists(qr_dir):
            os.makedirs(qr_dir)
        
        # Generate unique QR data
        qr_data = f"{attendance_url}?student_id={student_id}&class_id={class_id}&timestamp={datetime.now().isoformat()}"
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{student_id}_{class_id}_{timestamp}.png"
        filepath = os.path.join(qr_dir, filename)
        
        img.save(filepath)
        return filepath
    
    except Exception as e:
        raise Exception(f"QR code generation failed: {str(e)}")

def generate_batch_qr_codes(student_list, class_id, attendance_url):
    """
    Generate QR codes for multiple students
    
    Args:
        student_list: List of student IDs
        class_id: Class/Course ID
        attendance_url: Base URL for attendance endpoint
    
    Returns:
        dict: Mapping of student_id to QR code filepath
    """
    qr_map = {}
    for student_id in student_list:
        try:
            filepath = generate_attendance_qr(student_id, class_id, attendance_url)
            qr_map[student_id] = filepath
        except Exception as e:
            qr_map[student_id] = None
    
    return qr_map
