// Optional: Toggle dropdown on click for better mobile experience
const dropdown = document.querySelector('.dropdown');
const dropdownContent = document.querySelector('.dropdown-content');

dropdown.addEventListener('click', () => {
    dropdownContent.classList.toggle('show');
});

// Close the dropdown if the user clicks outside of it
window.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target)) {
        dropdownContent.classList.remove('show');
    }
});
