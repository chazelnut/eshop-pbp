// toast.js (versi aman, bebas error ganda)
const TOAST_DURATION = 2500;

function showToast(title, message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast ${type} show bounce`;

  toast.innerHTML = `
    <strong>${title}</strong><br>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.remove('show');
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, TOAST_DURATION);
}
