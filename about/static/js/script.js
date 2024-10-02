document.getElementById('menu-toggle').addEventListener('change', function () {
    const nav = document.querySelector('nav ul');
    if (this.checked) {
        nav.style.display = 'flex';
    } else {
        nav.style.display = 'none';
    }
});
