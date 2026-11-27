document.getElementById("myForm").onsubmit = function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    let valid = true;

    document.getElementById("nameError").innerHTML = "";
    document.getElementById("emailError").innerHTML = "";
    document.getElementById("passwordError").innerHTML = "";
    document.getElementById("success").innerHTML = "";

    if (name.trim() === "") {
        document.getElementById("nameError").innerHTML = "Name is required";
        valid = false;
    }

    if (!email.includes("@") || !email.includes(".")) {
        document.getElementById("emailError").innerHTML = "Enter valid email";
        valid = false;
    }

    if (password.length < 8) {
        document.getElementById("passwordError").innerHTML =
            "Password must contain at least 8 characters";
        valid = false;
    }

    if (valid) {
        document.getElementById("success").innerHTML =
            "Registration Successful!";
    }
};