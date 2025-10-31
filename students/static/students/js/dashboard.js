// --- Profile Dropdown ---
const profilePic = document.getElementById('profilePic');
const profileDropdown = document.getElementById('profileDropdown');

profilePic.addEventListener('click', () => {
    profileDropdown.style.display = profileDropdown.style.display === 'flex' ? 'none' : 'flex';
});

// Close dropdown if clicked outside
window.addEventListener('click', e => {
    if (!profilePic.contains(e.target) && !profileDropdown.contains(e.target)) {
        profileDropdown.style.display = 'none';
    }
});

// --- Mood Selection ---
const moodIcons = document.querySelectorAll('.mood-icon');
let selectedMood = null;

moodIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        moodIcons.forEach(i => i.classList.remove('selected'));
        icon.classList.add('selected');
        selectedMood = icon.dataset.mood;
    });
});

document.getElementById('saveMoodBtn').addEventListener('click', () => {
    if (!selectedMood) return alert('Select a mood first!');
    document.getElementById('moodMessage').style.display = 'block';
    setTimeout(() => { document.getElementById('moodMessage').style.display = 'none'; }, 2000);
    // Here you can also send selectedMood to backend via AJAX
});

// --- Journal Save ---
document.querySelector('.journal-action-btn').addEventListener('click', () => {
    const text = document.querySelector('.journal-textarea').value.trim();
    if (!text) return alert('Write something first!');
    alert('Journal entry saved!'); 
    // Here you can send text to backend via AJAX
    document.querySelector('.journal-textarea').value = '';
});

// --- Email Modal ---
const emailModal = document.getElementById('emailModal');
const openModalBtn = document.getElementById('openModalBtn');
const closeModalBtn = document.getElementById('closeModalBtn');

openModalBtn.addEventListener('click', () => emailModal.style.display = 'block');
closeModalBtn.addEventListener('click', () => emailModal.style.display = 'none');
window.addEventListener('click', e => { if (e.target === emailModal) emailModal.style.display = 'none'; });

document.getElementById('emailChangeForm').addEventListener('submit', e => {
    e.preventDefault();
    const newEmail = document.getElementById('newEmailInput').value.trim();
    if (!newEmail) return;
    document.getElementById('saveMessage').innerText = 'Email updated successfully!';
    document.getElementById('newEmailInput').value = '';
});

// --- Chart.js Mood Chart ---
const ctx = document.getElementById('moodChart').getContext('2d');
const moodChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Mood Score',
            data: [7, 6, 8, 5, 7, 6, 8],
            borderColor: '#7e22ce',
            backgroundColor: 'rgba(126, 34, 206, 0.2)',
            tension: 0.3,
            fill: true,
        }]
    },
    options: {
        responsive: true,
        plugins: { legend: { display: false }, tooltip: { mode: 'index' } },
        scales: { y: { min: 0, max: 10 } }
    }
});
