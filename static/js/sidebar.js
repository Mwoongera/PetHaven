// Example of toggle functionality for mobile view (optional)
const sidebar = document.querySelector('.sidebar');

document.querySelector('.toggle-sidebar').addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
});
