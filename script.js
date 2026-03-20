function validateForm() {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let department = document.getElementById("department").value;
    let feedback = document.getElementById("feedback").value.trim();
    let gender = document.querySelector('input[name="gender"]:checked');
    let error = document.getElementById("error");

    error.innerHTML = "";

    if (name === "") return error.innerHTML = "Enter name", false;
    if (!/^[^ ]+@[^ ]+\.[a-z]{2,3}$/.test(email)) return error.innerHTML = "Invalid email", false;
    if (!/^[0-9]{10}$/.test(mobile)) return error.innerHTML = "Invalid mobile", false;
    if (!gender) return error.innerHTML = "Select gender", false;
    if (department === "") return error.innerHTML = "Select department", false;

    let words = feedback.split(/\s+/).length;
    if (words < 10) return error.innerHTML = "Min 10 words required", false;

    document.getElementById("popup").style.display = "block";
    return false;
}

/* Close popup */
function closePopup() {
    document.getElementById("popup").style.display = "none";
}

/* Dark mode toggle */
function toggleMode() {
    document.body.classList.toggle("dark");
}
