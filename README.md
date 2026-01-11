Sure! Below is a clean and professional `README.md` for your **Smart QR-Based Student Attendance System** project.

You can copy-paste this directly into your GitHub repo.

---

# 📘 **Smart QR-Based Student Attendance System**

A secure and automated attendance management solution for educational institutions using dynamic QR codes, Flutter mobile app, Flask backend, and MySQL database.

---

## 🚀 **Overview**

This system replaces manual classroom attendance with a modern, secure, and time-saving digital solution.
Teachers generate a QR code for each class, and students scan it using their mobile app to mark their attendance.

The system ensures:

✔ No proxy attendance
✔ One-device login restriction
✔ Real-time attendance tracking
✔ Cloud-hosted backend
✔ Class-wise and student-wise statistics

---

## 🏗 **Tech Stack**

**Frontend (Student App):**

* Flutter (Dart)
* mobile_scanner (QR Scanner)
* device_info_plus (Android ID)

**Backend (Server):**

* Flask (Python)
* Flask-CORS
* Gunicorn (for deployment)
* python-dotenv

**Database:**

* MySQL (Cloud or Local)

**Teacher Web Dashboard:**

* HTML + CSS + JS (served via Flask)

**Cloud Hosting (Recommended):**

* Render / Railway / AWS / DigitalOcean

---

## 🎯 **Features**

### 👨‍🎓 **Student Side**

* Login via Roll No + Password
* Android ID device lock
* Scan QR to mark attendance
* View attendance percentage
* View attendance history

### 👨‍🏫 **Teacher Side**

* Login via Email + Password
* Generate QR for each class
* QR auto-expires in minutes
* Realtime attendance tracking

### 🏫 **Admin Side**

* Manage students
* Manage teachers
* Manage branches & classes
* View attendance reports

---

## 🛡 **Security Mechanisms**

| Mechanism         | Purpose                      |
| ----------------- | ---------------------------- |
| Dynamic QR Tokens | Prevent screenshot re-use    |
| Token Expiry      | Prevent late/proxy scans     |
| Device Binding    | Prevent login sharing        |
| Cloud Auth        | Secure communication         |
| DB Validation     | Prevent duplicate attendance |

---

## 📂 **Project Structure**

```
student-attendance-system/
│
├── backend_flask/
│   ├── app.py
│   ├── db.py
│   ├── config.py
│   ├── requirements.txt
│   ├── routes/
│   │   ├── auth.py
│   │   ├── student.py
│   │   └── teacher.py
│   ├── utils/
│   │   └── qr_generator.py
│   ├── static/
│   │   └── qr/
│   └── templates/
│       ├── login.html
│       ├── dashboard_teacher.html
│       └── dashboard_student.html
│
└── mobile_app_flutter/
    ├── lib/
    │   ├── main.dart
    │   ├── screens/
    │   ├── services/
    │   └── widgets/
    └── pubspec.yaml
```

---

## 🗄 **Database Schema (MySQL)**

### 📌 `students` Table

| Field     | Type         |
| --------- | ------------ |
| id        | INT          |
| name      | VARCHAR(100) |
| roll_no   | VARCHAR(20)  |
| branch    | ENUM(...)    |
| year      | INT          |
| password  | VARCHAR(255) |
| device_id | VARCHAR(255) |

### 📌 `teachers` Table

| Field    | Type         |
| -------- | ------------ |
| id       | INT          |
| name     | VARCHAR(100) |
| email    | VARCHAR(100) |
| role     | ENUM(...)    |
| branch   | ENUM(...)    |
| password | VARCHAR(255) |

### 📌 `qr_tokens` Table

| Field      | Type         |
| ---------- | ------------ |
| id         | INT          |
| class_id   | INT          |
| token      | VARCHAR(255) |
| expires_at | DATETIME     |

### 📌 `attendance` Table

| Field      | Type                     |
| ---------- | ------------------------ |
| id         | INT                      |
| student_id | INT                      |
| class_id   | INT                      |
| date       | DATE                     |
| time       | TIME                     |
| status     | ENUM('Present','Absent') |

---

## 🔌 **API Endpoints**

### **Auth**

| Method | Endpoint              | Description                   |
| ------ | --------------------- | ----------------------------- |
| POST   | `/auth/student/login` | Student login with Android ID |
| POST   | `/auth/teacher/login` | Teacher login                 |

### **Teacher**

| Method | Endpoint                        | Description           |
| ------ | ------------------------------- | --------------------- |
| POST   | `/teacher/generate_qr`          | Generate QR for class |
| GET    | `/teacher/class_attendance/:id` | View attendance       |

### **Student**

| Method | Endpoint                             | Description               |
| ------ | ------------------------------------ | ------------------------- |
| POST   | `/student/scan_qr`                   | Scan QR → Mark attendance |
| GET    | `/student/attendance_percentage/:id` | Attendance %              |

---

## 🌐 **Deployment Guide (Cloud Hosting)**

1. Push backend to GitHub
2. Create Render/Railway service
3. Add environment variables:

```
DB_HOST=
DB_USER=
DB_PASS=
DB_NAME=
```

4. Add `Procfile`:

```
web: gunicorn app:app
```

5. Deploy and get public URL
6. Update Flutter `BASE_URL`

---

## 📱 **Flutter Setup**

Install dependencies:

```
flutter pub add http mobile_scanner device_info_plus shared_preferences
```

Update `BASE_URL`:

```dart
const String BASE_URL = "https://your-cloud-backend.com";
```

Build & run:

```
flutter run
```

---

## 🧪 **Testing Scenario**

| Test Case        | Expected Result          |
| ---------------- | ------------------------ |
| Valid QR         | Status: Present          |
| Expired QR       | Error: QR Expired        |
| Wrong Class      | Error: Invalid QR        |
| Duplicate Scan   | Error: Already Marked    |
| New Device Login | Error: Device Restricted |

---

## 📈 **Future Enhancements**

* Face recognition
* Low attendance alerts (SMS/Email)
* Admin analytics dashboard
* Class timetable integration
* Offline sync mode
* PDF/Excel report export

---

## 📝 **License**

This project is intended for educational purposes.
Feel free to modify and extend functionality.

---



