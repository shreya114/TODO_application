document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signup-form");

    form.addEventListener("submit", (e) => {
        const username = document.getElementById("username").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (username === "" || email === "" || password === "") {
            e.preventDefault();
            alert("All fields are required. Please fill out the form completely.");
        } else if (!validateEmail(email)) {
            e.preventDefault();
            alert("Please enter a valid email address.");
        }
    });

    const validateEmail = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    };
});
