// client/js/dashboard.js

// UWAGA: Usunąłem linię "const API_URL = ...", bo jest już w session.js!
// Dzięki temu nie ma błędu "Identifier has already been declared".

// Zmienne stanu
let currentTopicData = null;
let contentMode = 'theory'; // 'theory' lub 'tasks'

// 1. START APLIKACJI
document.addEventListener('DOMContentLoaded', () => {
    console.log("🚀 Dashboard startuje...");

    // Wyświetlanie usera (jeśli jest zalogowany)
    if (typeof currentUser !== 'undefined' && currentUser) {
        const userDisplay = document.getElementById('nav-username');
        if(userDisplay) userDisplay.innerText = currentUser.username;
    }

    // Pobieranie tematów
    loadTopics();
});

// 2. POBIERANIE TEMATÓW Z BAZY
async function loadTopics() {
    // API_URL jest teraz brany z session.js
    console.log("🔄 Pobieranie tematów z:", API_URL + "/topics");
    const list = document.getElementById('chapter-list');

    try {
        const res = await fetch(`${API_URL}/topics`);

        if (!res.ok) {
            throw new Error(`Błąd serwera: ${res.status}`);
        }

        const allTopics = await res.json();
        console.log("✅ Pobrano tematów:", allTopics.length);

        if(allTopics.length === 0) {
            list.innerHTML = '<li class="list-group-item text-warning">Baza jest pusta. Użyj setup.html</li>';
            return;
        }

        renderSidebar(allTopics);

    } catch (e) {
        console.error("❌ Błąd krytyczny:", e);
        list.innerHTML = `<li class="list-group-item text-danger">
            <strong>Błąd połączenia!</strong><br>
            Sprawdź konsolę (F12).<br>
            Czy serwer Docker działa?
        </li>`;
    }
}

// 3. RYSOWANIE SIDEBARA (Pasek boczny)
function renderSidebar(allTopics) {
    const list = document.getElementById('chapter-list');
    list.innerHTML = ""; // Czyścimy "Ładowanie..."

    // Grupujemy tematy po rozdziałach
    const chapters = {};
    allTopics.forEach(t => {
        if (!chapters[t.chapter]) chapters[t.chapter] = [];
        chapters[t.chapter].push(t);
    });

    // Sortujemy rozdziały
    const sortedChapters = Object.keys(chapters).sort();

    for (const chapName of sortedChapters) {
        const topics = chapters[chapName];

        // Nagłówek rozdziału
        const header = document.createElement('div');
        header.className = "chapter-header text-uppercase fw-bold text-muted mt-3 mb-2 ms-3 small";
        header.innerText = chapName;
        list.appendChild(header);

        // Lista tematów w rozdziale
        topics.forEach(t => {
            const btn = document.createElement('button');
            btn.className = "list-group-item list-group-item-action bg-transparent text-secondary border-0 py-2 ps-3";
            btn.style.fontSize = "0.95rem";
            btn.innerHTML = `<i class="bi bi-circle-fill me-2" style="font-size: 6px;"></i> ${t.title}`;

            // KLIKNIĘCIE W TEMAT
            btn.onclick = () => {
                // Reset stylów innych przycisków
                document.querySelectorAll('.list-group-item').forEach(el => {
                    el.classList.remove('active', 'text-white', 'fw-bold');
                    el.classList.add('text-secondary');
                });

                // Aktywacja tego przycisku
                btn.classList.remove('text-secondary');
                btn.classList.add('active', 'text-white', 'fw-bold');

                // Ustawienie danych i odświeżenie widoku
                currentTopicData = t;
                console.log("👉 Wybrano temat:", t.title);
                renderContentArea();
            };
            list.appendChild(btn);
        });
    }
}

// 4. PRZEŁĄCZANIE TEORIA / ZADANIA
// Przypisujemy do window, żeby HTML widział tę funkcję
window.switchContentMode = function(mode) {
    console.log("🔀 Przełączanie trybu na:", mode);
    contentMode = mode;

    const btnTheory = document.getElementById('btn-theory');
    const btnTasks = document.getElementById('btn-tasks');

    if (!btnTheory || !btnTasks) return;

    if (mode === 'theory') {
        // Aktywna Teoria
        btnTheory.classList.add('active', 'bg-primary', 'text-white');
        btnTheory.classList.remove('text-secondary', 'bg-transparent');

        // Nieaktywne Zadania
        btnTasks.classList.remove('active', 'bg-primary', 'text-white');
        btnTasks.classList.add('text-secondary', 'bg-transparent');
    } else {
        // Aktywne Zadania
        btnTasks.classList.add('active', 'bg-primary', 'text-white');
        btnTasks.classList.remove('text-secondary', 'bg-transparent');

        // Nieaktywna Teoria
        btnTheory.classList.remove('active', 'bg-primary', 'text-white');
        btnTheory.classList.add('text-secondary', 'bg-transparent');
    }

    renderContentArea();
}

// 5. WYŚWIETLANIE TREŚCI
function renderContentArea() {
    const titleEl = document.getElementById('topic-title');
    const contentEl = document.getElementById('content-area');

    if (!currentTopicData) {
        return;
    }

    titleEl.innerText = currentTopicData.title;

    // Prosta animacja zanikania
    contentEl.style.opacity = "0.3";

    setTimeout(() => {
        if (contentMode === 'theory') {
            contentEl.innerHTML = currentTopicData.theoryHtml || "<p class='text-muted'>Brak treści teoretycznej.</p>";
        } else {
            contentEl.innerHTML = currentTopicData.tasksHtml ||
                `<div class="text-center py-5">
                    <i class="bi bi-tools display-1 text-secondary opacity-25"></i>
                    <h4 class="mt-4 text-white">Sekcja Zadań</h4>
                    <p class="text-secondary">Wkrótce pojawią się tu zadania.</p>
                </div>`;
        }
        contentEl.style.opacity = "1";
    }, 150);
}