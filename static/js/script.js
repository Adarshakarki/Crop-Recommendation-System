const toggleBtn = document.getElementById('darkModeToggle');
const htmlEl = document.documentElement;

toggleBtn.addEventListener('click', () => {
  if (htmlEl.getAttribute('data-theme') === 'light') {
    htmlEl.setAttribute('data-theme', 'dark');
    toggleBtn.textContent = '☀️';
  } else {
    htmlEl.setAttribute('data-theme', 'light');
    toggleBtn.textContent = '🌙';
  }
});
