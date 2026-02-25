// client/js/profile.js

document.addEventListener('DOMContentLoaded', async () => {
    // 1. Sprawdzamy, czy użytkownik jest zalogowany
    if (typeof currentUser === 'undefined' || !currentUser) {
        window.location.href = 'login.html';
        return;
    }


    document.getElementById('nav-username').innerText = currentUser.username;
    document.getElementById('profile-name').innerText = currentUser.username;

    // Obsługa pola "O mnie" (Bio)
    const savedBio = localStorage.getItem('maturapp_bio_' + currentUser.username);
    if (savedBio) {
        document.getElementById('about-me').value = savedBio;
    }

    // Pobranie aktualnego XP prosto z bazy danych
    await fetchUserXp();
});

// Zapis notatki
window.saveBio = function() {
    const text = document.getElementById('about-me').value;
    localStorage.setItem('maturapp_bio_' + currentUser.username, text);
    alert("Bio zapisane!");
}

// Pobieranie XP z backendu
async function fetchUserXp() {
    try {
        const response = await fetch(`http://localhost:8080/api/auth/get-user?username=${currentUser.username}`);

        if (response.ok) {
            const userData = await response.json();

            // Zapisujemy nowe dane
            currentUser.xp = userData.xp;
            currentUser.tasksCompleted = userData.tasksCompleted; // <--- Zapisujemy prawdziwe zadania

            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            if(localStorage.getItem('user')) localStorage.setItem('user', JSON.stringify(currentUser));
            if(localStorage.getItem('userSession')) localStorage.setItem('userSession', JSON.stringify(currentUser));

            // Przekazujemy prawdziwą liczbę zadań do interfejsu
            updateProfileUI(userData.xp, userData.tasksCompleted);
        } else {
            updateProfileUI(currentUser.xp || 0, currentUser.tasksCompleted || 0);
        }
    } catch (error) {
        updateProfileUI(currentUser.xp || 0, currentUser.tasksCompleted || 0);
    }
}


function updateProfileUI(xp, tasksCompleted) {
    const streak = currentUser.dailyStreak || 0;

    const level = Math.floor(xp / 100) + 1;
    const nextLevelXp = level * 100;
    const currentLevelXpStart = (level - 1) * 100;
    const xpInThisLevel = xp - currentLevelXpStart;
    const xpRequired = nextLevelXp - currentLevelXpStart;
    const progressPercent = (xpInThisLevel / xpRequired) * 100;

    document.getElementById('current-lvl').innerText = `Lvl ${level}`;
    document.getElementById('xp-info').innerText = `${xp} XP`;

    setTimeout(() => {
        document.getElementById('xp-fill').style.width = `${progressPercent}%`;
    }, 100);

    document.getElementById('xp-needed').innerText = (nextLevelXp - xp);
    document.getElementById('stat-streak').innerText = streak;

    // TUTAJ ZMIANA: Wyświetlamy prosto z bazy danych, zero dzielenia
    document.getElementById('stat-tasks').innerText = tasksCompleted || 0;

    renderLeaderboard(xp, level);
}

// System Leaderboard
function renderLeaderboard(currentXp, currentLvl) {
    const fakeUsers = [
        { username: "MatmaMaster", xp: 1500, lvl: 15 },
        { username: "Pitagoras_PL", xp: 850, lvl: 8 },
        { username: "SzybkiLopez", xp: 420, lvl: 4 },
        { username: "Kujon99", xp: 120, lvl: 2 }
    ];

    fakeUsers.push({
        username: currentUser.username,
        xp: currentXp,
        lvl: currentLvl,
        isMe: true
    });

    fakeUsers.sort((a, b) => b.xp - a.xp);

    const tbody = document.getElementById('leaderboard-body');
    if (!tbody) return;
    tbody.innerHTML = "";

    fakeUsers.forEach((u, index) => {
        const rank = index + 1;
        let trophy = "";
        if (rank === 1) trophy = "🥇";
        if (rank === 2) trophy = "🥈";
        if (rank === 3) trophy = "🥉";

        const row = document.createElement('tr');
        if (u.isMe) row.classList.add('my-rank');

        row.innerHTML = `
            <td class="ps-4 py-3 text-secondary fw-bold">${trophy || rank}</td>
            <td class="py-3 fw-bold ${u.isMe ? 'text-primary' : 'text-white'}">
                ${u.username} ${u.isMe ? '(Ty)' : ''}
            </td>
            <td class="py-3"><span class="badge bg-secondary text-dark">Lvl ${u.lvl}</span></td>
            <td class="py-3 text-end pe-4 text-success fw-bold">${u.xp} XP</td>
        `;
        tbody.appendChild(row);
    });
}