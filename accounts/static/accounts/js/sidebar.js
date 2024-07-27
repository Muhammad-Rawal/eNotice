document.addEventListener('DOMContentLoaded', function() {
    const sidebarButton = document.querySelector('[data-drawer-toggle="cta-button-sidebar"]');
    const sidebar = document.getElementById('cta-button-sidebar');

    sidebarButton.addEventListener('click', function() {
        sidebar.classList.toggle('-translate-x-full');
    });

    document.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && event.target !== sidebarButton) {
            sidebar.classList.add('-translate-x-full');
        }
    });
});