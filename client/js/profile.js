// client/js/profile.js

// 1. Wczytaj dane użytkownika
document.getElementById('nav-username').innerText = currentUser.username;
document.getElementById('profile-name').innerText = currentUser.username;

// Obsługa pola "O mnie" (Bio)
const savedBio = localStorage.getItem('maturapp_bio_' + currentUser.username);
if (savedBio) {
    document.getElementById('about-me').value = savedBio;
}

function saveBio() {
    const text = document.getElementById('about-me').value;
    localStorage.setItem('maturapp_bio_' + currentUser.username, text);
    alert("Bio zapisane!");
}

// 2. Obliczanie Levela i XP
const xp = currentUser.xp || 0; // Jeśli nie ma XP, to 0
const streak = currentUser.dailyStreak || 0;

// Logika: Każdy level to 100 XP * numer poziomu (uproszczone)
const level = Math.floor(xp / 100) + 1;
const nextLevelXp = level * 100;
const currentLevelXpStart = (level - 1) * 100;
const xpInThisLevel = xp - currentLevelXpStart; // Ile XP zdobyliśmy w tym levelu
const xpRequired = nextLevelXp - currentLevelXpStart; // Ile trzeba zdobyć
const progressPercent = (xpInThisLevel / xpRequired) * 100;

// Aktualizacja UI statystyk
document.getElementById('current-lvl').innerText = `Lvl ${level}`;
document.getElementById('xp-info').innerText = `${xp} XP`;
document.getElementById('xp-fill').style.width = `${progressPercent}%`;
document.getElementById('xp-needed').innerText = (nextLevelXp - xp);
document.getElementById('stat-streak').innerText = streak;
document.getElementById('stat-tasks').innerText = Math.floor(xp / 10); // Zakładamy 10xp za zadanie

// 3. System Leaderboard (Symulacja + Ty)
function renderLeaderboard() {
    // Generujemy fikcyjnych graczy, żeby ranking żył
    const fakeUsers = [
        { username: "MatmaMaster", xp: 1500, lvl: 15 },
        { username: "Pitagoras_PL", xp: 850, lvl: 8 },
        { username: "SzybkiLopez", xp: 420, lvl: 4 },
        { username: "Kujon99", xp: 120, lvl: 2 }
    ];

    // Dodajemy Ciebie do listy
    fakeUsers.push({
        username: currentUser.username,
        xp: xp,
        lvl: level,
        isMe: true // Flaga, żeby Cię podświetlić
    });

    // Sortujemy: Kto ma najwięcej XP jest pierwszy
    fakeUsers.sort((a, b) => b.xp - a.xp);

    const tbody = document.getElementById('leaderboard-body');
    tbody.innerHTML = "";

    fakeUsers.forEach((u, index) => {
        const rank = index + 1;
        let trophy = "";
        if (rank === 1) trophy = "🥇";
        if (rank === 2) trophy = "🥈";
        if (rank === 3) trophy = "🥉";

        const row = document.createElement('tr');
        if (u.isMe) row.classList.add('my-rank'); // Klasa do podświetlenia Ciebie

        row.innerHTML = `
            <td>${trophy || rank}</td>
            <td><strong>${u.username}</strong> ${u.isMe ? '(Ty)' : ''}</td>
            <td><span class="lvl-tag">Lvl ${u.lvl}</span></td>
            <td>${u.xp} XP</td>
        `;
        tbody.appendChild(row);
    });
}

renderLeaderboard();