document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting and refreshing the page
    alert('Message sent!');
    // Optionally, you can clear the form after showing the alert:
    this.reset();
});
