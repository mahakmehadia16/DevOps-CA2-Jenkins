# 🎓 Student Feedback Registration Form (DevOps Project)

## 📌 Project Description

This project is a web-based **Student Feedback Registration Form** developed using HTML, CSS, and JavaScript. It includes modern UI design, form validation, automated testing using Selenium, and CI/CD automation using Jenkins.

---

## 🚀 Technologies Used

* HTML (Form Structure)
* CSS (Styling & UI Design)
* JavaScript (Validation & Interactivity)
* Python (Selenium Script)
* Selenium (Automation Testing)
* Jenkins (CI/CD Automation)
* Git & GitHub (Version Control)

---

## 📋 Features

* User-friendly and modern UI design
* Glassmorphism (transparent card UI)
* Responsive layout
* Dark/Light mode toggle 🌙
* Smooth animations and transitions
* Custom success popup (instead of alert)
* Input validation using JavaScript:

  * Name cannot be empty
  * Email format validation
  * Mobile number validation (10 digits)
  * Gender selection required
  * Department selection required
  * Feedback must contain at least 10 words

---

## 🎨 UI Enhancements

* Gradient background design
* Animated form appearance (fade-in effect)
* Hover effects on buttons
* Improved spacing and alignment
* Modern input styling with focus effects

---

## 🧪 Selenium Test Cases

* Verify form page loads successfully
* Submit form with valid data
* Validate empty fields
* Validate incorrect email format
* Validate invalid mobile number
* Verify dropdown selection
* Test Submit and Reset buttons

---

## ⚙️ Jenkins Integration

* Created a Freestyle Project in Jenkins
* Configured build step to execute Selenium Python script
* Automated execution of test cases
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

## ▶️ How to Run the Project

### 🔹 Run Web Form

1. Open `index.html` in any browser

### 🔹 Run Selenium Test

```bash
python test_form.py
```

### 🔹 Run via Jenkins

1. Open Jenkins Dashboard
2. Create a Freestyle Job
3. Add build step:

```bash
cd "your_project_path"
python test_form.py
```

4. Click **Build Now**

---

## 🎯 Outcome

The project successfully demonstrates:

* Frontend web development
* Client-side validation
* Automation testing using Selenium
* CI/CD pipeline using Jenkins
* Enhanced UI/UX with animations and dark mode

---

## 🧠 Learning Outcomes

* Understanding of DevOps lifecycle
* Hands-on experience with Selenium automation
* Knowledge of Jenkins job configuration
* Experience with Git and GitHub

---

## 👩‍💻 Author

Mahak Mehadia

---
