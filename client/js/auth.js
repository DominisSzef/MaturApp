

// ODKOMENTOWAŁEM TO, ŻEBYŚ NIE MIAŁ BŁĘDU "UNDEFINED"
const API_URL = 'http://localhost:8080/api';

async function handleLogin() {
    // Pobieramy ID takie jak masz w HTML: login-user i login-pass
    const u = document.getElementById('login-user').value;
    const p = document.getElementById('login-pass').value;
    const msg = document.getElementById('msg');

    if(!u || !p) { msg.innerText = "Podaj login i hasło"; return; }

    try {
        const res = await fetch(`${API_URL}/auth/login`, {
            method: 'POST', headers: {'Content-Type':'application/json'},
            body: JSON.stringify({ username: u, password: p })
        });

        if (res.ok) {
            const user = await res.json();
            // KLUCZOWE: Zapisujemy usera w pamięci przeglądarki
            localStorage.setItem('maturapp_user', JSON.stringify(user));
            // Przekierowanie na dashboard
            window.location.href = 'dashboard.html';
        } else {
            msg.innerText = "Błędne dane.";
            msg.style.color = "red";
        }
    } catch (e) { console.error(e); msg.innerText = "Błąd serwera."; }
}

async function handleRegister() {
    const u = document.getElementById('login-user').value;
    const p = document.getElementById('login-pass').value;
    const msg = document.getElementById('msg');

    try {
        const res = await fetch(`${API_URL}/auth/register`, {
            method: 'POST', headers: {'Content-Type':'application/json'},
            body: JSON.stringify({ username: u, password: p })
        });
        if (res.ok) {
            msg.innerText = "Konto założone! Zaloguj się.";
            msg.style.color = "green";
        } else {
            msg.innerText = "Taki login już istnieje.";
        }
    } catch (e) { console.error(e); }
}