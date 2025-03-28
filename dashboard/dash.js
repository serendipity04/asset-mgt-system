const darkModeToggle = document.getElementById("dark-mode-toggle");
darkModeToggle.addEventListener("click", ()=>{
    document.body.classList.toggle("darkMode");
});

// Select the toggle button and sidebar
const toggleButton = document.getElementById('fa-bars');
const retoggle = document.getElementById('fa-x')
const sidebar = document.getElementById('sidebar');

// Add an event listener for button clicks
toggleButton.addEventListener('click', function() {
    // If the sidebar is hidden, show it; if it's shown, hide it
    if (sidebar.style.left === '-250px') {
        sidebar.style.left = '0';
        toggleButton.style.visibility = 'hidden';
        retoggle.style.visibility = 'visible';

    } else {
        sidebar.style.left = '-250px';
        toggleButton.style.visibility = 'visible';
    }
});
