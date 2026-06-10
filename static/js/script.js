document.addEventListener('DOMContentLoaded', function() {
    
    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            const confirmLogout = confirm('Are you sure you want to log out of Brushed up Things?');
            if (!confirmLogout) {
                event.preventDefault();
            }
        });
    }

    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const itemName = this.getAttribute('data-name') || 'this item';
            const confirmDelete = confirm(`Are you sure you want to delete "${itemName}"?`);
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

});