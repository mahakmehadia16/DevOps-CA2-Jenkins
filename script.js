function validateForm() {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let mobile = document.getElementById("mobile").value;
    let department = document.getElementById("department").value;
    let feedback = document.getElementById("feedback").value;
    let gender = document.querySelector('input[name="gender"]:checked');
    let error = document.getElementById("error");

    error.innerHTML = "";

    // Name validation
    if (name === "") {
        error.innerHTML = "Name cannot be empty";
        return false;
    }

    // Email validation
    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        error.innerHTML = "Invalid Email";
        return false;
    }

    // Mobile validation
    let mobilePattern = /^[0-9]{10}$/;
    if (!mobile.match(mobilePattern)) {
        error.innerHTML = "Invalid Mobile Number";
        return false;
    }

    // Gender validation
    if (!gender) {
        error.innerHTML = "Select Gender";
        return false;
    }

    // Department validation
    if (department === "") {
        error.innerHTML = "Select Department";
        return false;
    }

    // Feedback validation (min 10 words)
    let wordCount = feedback.trim().split(/\s+/).length;
    if (feedback === "" || wordCount < 10) {
        error.innerHTML = "Feedback must be at least 10 words";
        return false;
    }

    alert("Form Submitted Successfully!");
    return true;
}