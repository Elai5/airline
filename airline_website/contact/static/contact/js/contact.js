// Reset the form when "Send" is clicked (after submission)
function handleSubmit(event) {
    event.preventDefault();  // Prevent the form from actually submitting (if you don't want to use a backend)

    // Simulate a successful submission (show an alert or console log)
    alert("Thank you for reaching out! We will get back to you soon.");

    // Reset the form
    document.getElementById("contact-form").reset();
}

// Focus on the next input field when the user presses Enter
document.querySelectorAll('.field').forEach((field, index, fields) => {
    field.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            // Check if it's the last input field, then do nothing
            if (index < fields.length - 1) {
                fields[index + 1].focus();  // Focus on the next input
                event.preventDefault();  // Prevent form submission
            }
        }
    });
});
