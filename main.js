const BASE = "http://127.0.0.1:5000";

// STUDENT LOGIN
function studentLogin() {
  let roll = document.getElementById("roll").value;
  let pwd = document.getElementById("pwd").value;

  fetch(`${BASE}/auth/student/login`, {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({roll_no: roll, password: pwd, device_id:"web"})
  })
  .then(res=>res.json())
  .then(data=>{
    if(data.status){
      localStorage.setItem("student_id", data.student_id);
      location.href="student_dashboard.html";
    } else {
      document.getElementById("msg").innerText = data.message;
    }
  });
}

// TEACHER LOGIN
function teacherLogin() {
  let email = document.getElementById("email").value;
  let pwd = document.getElementById("pwd").value;

  fetch(`${BASE}/auth/teacher/login`, {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({email: email, password: pwd})
  })
  .then(res=>res.json())
  .then(data=>{
    if(data.status){
      location.href="teacher_dashboard.html";
    } else {
      document.getElementById("msg").innerText = data.message;
    }
  });
}

// GENERATE QR
function generateQR() {
  let classId = document.getElementById("classSelect").value;

  fetch(`${BASE}/teacher/generate_qr`, {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({class_id: classId})
  })
  .then(res=>res.json())
  .then(data=>{
    if(data.status){
      document.getElementById("qrImg").src = BASE + data.qr_image;
      document.getElementById("qrImg").style.display="block";
    }
  });
}

// LOAD STUDENT ATTENDANCE
function loadAttendance() {
  const id = localStorage.getItem("student_id");

  fetch(`${BASE}/student/attendance_percentage/${id}`)
  .then(res=>res.json())
  .then(data=>{
    document.getElementById("total").innerText = data.total;
    document.getElementById("present").innerText = data.present;
    document.getElementById("percent").innerText = data.percentage + "%";
  });
}
