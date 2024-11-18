
// Remove 'alert' messages
window.onload = function() {
    // Find all elements with the class 'alert' and remove them after page load
    setTimeout(function() {
        const alertElement = document.querySelector('.alert');
        if (alertElement) {
            alertElement.style.display = 'none';
        }
    }, 3000); // Delay to ensure the user sees the message for a short while before hiding it
};
