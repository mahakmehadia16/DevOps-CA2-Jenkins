# 🎓 Student Feedback Registration Form (DevOps Project)

## 📌 Project Description

This project is a web-based **Student Feedback Registration Form** developed using HTML, CSS, and JavaScript. It includes form validation and automated testing using Selenium. Jenkins is used to automate test case execution as part of a DevOps workflow.

---

## 🚀 Technologies Used

* HTML (Form Structure)
* CSS (Styling)
* JavaScript (Validation)
* Selenium (Automation Testing)
* Jenkins (CI/CD Automation)
* Python (Selenium Script)

---

## 📋 Features

* User-friendly feedback form
* Input validation using JavaScript:

  * Name cannot be empty
  * Email format validation
  * Mobile number validation
  * Gender selection required
  * Department selection required
  * Feedback must be at least 10 words
* Automated testing using Selenium
* Continuous Integration using Jenkins

---

## 🧪 Selenium Test Cases

* Check if form page loads successfully
* Submit form with valid data
* Validate empty fields
* Validate incorrect email format
* Validate invalid mobile number
* Check dropdown selection
* Test Submit and Reset buttons

---

## ⚙️ Jenkins Integration

* Created a Freestyle Project in Jenkins
* Configured build step to execute Selenium Python script
* Automated test execution
* Verified build status (Success/Failure)

---

## 📁 Project Structure

```
Student-Feedback-Form/
│
├── index.html
├── style.css
├── script.js
├── test_form.py
└── README.md
```

---

## ▶️ How to Run Project

### 🔹 Run Web Form

1. Open `index.html` in browser

### 🔹 Run Selenium Test

```bash
python test_form.py
```

### 🔹 Run via Jenkins

* Create job → Add build step → Run Python script
* Click **Build Now**

---

## 🎯 Outcome

The project successfully demonstrates:

* Web development basics
* Client-side validation
* Automation testing
* CI/CD using Jenkins

---

## 🧠 Learning Outcome

* Understanding of DevOps pipeline
* Hands-on experience with Selenium and Jenkins
* Automation of testing process

---

## 👩‍💻 Author

Mahak Mehadia

---
