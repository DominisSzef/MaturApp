// client/js/session.js

// To jest jedyne miejsce, gdzie definiujemy adres API
const API_URL = 'http://localhost:8080/api';
// (Jeśli używasz var zamiast const, unikniesz błędów, ale const jest ok, jeśli jest tylko tu)

// Sprawdzanie sesji użytkownika
let currentUser = null;

try {
    const userJson = localStorage.getItem('maturapp_user');
    if (userJson) {
        currentUser = JSON.parse(userJson);
        console.log("✅ Zalogowany jako:", currentUser.username);
    }
} catch (e) {
    console.error("Błąd odczytu sesji", e);
}

function logout() {
    localStorage.removeItem('maturapp_user');
    window.location.href = 'login.html';
}

// Jeśli nie ma usera, a nie jesteśmy na stronie logowania/rejestracji -> wyrzuć
if (!currentUser && !window.location.href.includes('login.html') && !window.location.href.includes('setup.html')) {
    window.location.href = 'login.html';
}