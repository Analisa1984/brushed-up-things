document.addEventListener('DOMContentLoaded', function() {
    const logoutLink = document.getElementById('logout-link');
    
    // Check if the element exists on the current page to prevent console errors
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            const confirmLogout = confirm('Are you sure you want to log out of Brushed up Things?');
            
            if (!confirmLogout) {
                // If they click 'Cancel', stop the browser from following the link
                event.preventDefault();
            }
        });
    }
});