# Skrypt wypelniajacy wszystkie 42 tematy teoria i zadaniami
# Uruchom z folderu MaturApp: .\fill_topics.ps1

$API = "http://localhost:8080/api/topics"

$topics = @(

# ============================================================
# ROZDZIAL I. LICZBY I DZIALANIA
# ============================================================
@{
  title = "1. Liczby rzeczywiste"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>1. Liczby rzeczywiste</h3>
<p>Zbiór liczb rzeczywistych <strong>ℝ</strong> obejmuje wszystkie liczby wymierne i niewymierne.</p>
<h5 class='text-warning mt-3'>Rodzaje liczb:</h5>
<ul>
  <li><strong>Naturalne (ℕ):</strong> 1, 2, 3, 4, ...</li>
  <li><strong>Całkowite (ℤ):</strong> ..., -2, -1, 0, 1, 2, ...</li>
  <li><strong>Wymierne (ℚ):</strong> liczby postaci p/q, np. 1/2, -3/4, 0.75</li>
  <li><strong>Niewymierne:</strong> √2, π, e — nie da się zapisać jako ułamek</li>
</ul>
<h5 class='text-warning mt-3'>Oś liczbowa i wartość bezwzględna:</h5>
<p>Wartość bezwzględna |a| to odległość liczby a od zera na osi liczbowej:</p>
<div class='alert alert-secondary'>|a| = a gdy a ≥ 0 &nbsp;&nbsp;|&nbsp;&nbsp; |a| = -a gdy a &lt; 0</div>
<h5 class='text-warning mt-3'>Zapamiętaj:</h5>
<ul>
  <li>ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</li>
  <li>|a| ≥ 0 zawsze</li>
  <li>|-a| = |a|</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Liczby rzeczywiste</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Oceń, które liczby są wymierne, a które niewymierne: √9, √5, 0.(3), π, -7/3.<br>
  <span class='text-muted'>Odpowiedź: wymierne: √9=3, 0.(3)=1/3, -7/3 &nbsp;|&nbsp; niewymierne: √5, π</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Oblicz: |−8| + |3| − |−2|<br>
  <span class='text-muted'>Odpowiedź: 8 + 3 − 2 = 9</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Dla jakich wartości x zachodzi: |x − 3| = 5?<br>
  <span class='text-muted'>Odpowiedź: x − 3 = 5 → x = 8 &nbsp;lub&nbsp; x − 3 = −5 → x = −2</span>
</div>
"@
},

@{
  title = "2. Potęgi"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>2. Potęgi</h3>
<p>Potęga o wykładniku naturalnym: <strong>aⁿ = a · a · a · ... · a</strong> (n razy)</p>
<h5 class='text-warning mt-3'>Działania na potęgach (a ≠ 0):</h5>
<div class='alert alert-secondary'>
  aᵐ · aⁿ = aᵐ⁺ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; aᵐ ÷ aⁿ = aᵐ⁻ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; (aᵐ)ⁿ = aᵐⁿ<br>
  (a·b)ⁿ = aⁿ·bⁿ &nbsp;&nbsp;|&nbsp;&nbsp; (a/b)ⁿ = aⁿ/bⁿ &nbsp;&nbsp;|&nbsp;&nbsp; a⁰ = 1 &nbsp;&nbsp;|&nbsp;&nbsp; a⁻ⁿ = 1/aⁿ
</div>
<h5 class='text-warning mt-3'>Potęgi o wykładniku wymiernym:</h5>
<div class='alert alert-secondary'>a^(p/q) = ᵠ√(aᵖ)</div>
<h5 class='text-warning mt-3'>Uwaga:</h5>
<ul>
  <li>0ⁿ = 0 dla n &gt; 0</li>
  <li>Wyrażenie 0⁰ jest nieoznaczone</li>
  <li>(-1)ⁿ = 1 gdy n parzyste, (-1)ⁿ = -1 gdy n nieparzyste</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Potęgi</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Uprość: 2³ · 2⁵ ÷ 2⁴<br>
  <span class='text-muted'>Odpowiedź: 2^(3+5-4) = 2⁴ = 16</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Oblicz: (3²)³ ÷ 3⁴<br>
  <span class='text-muted'>Odpowiedź: 3⁶ ÷ 3⁴ = 3² = 9</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Zapisz jako potęgę: ∜(a⁶)<br>
  <span class='text-muted'>Odpowiedź: a^(6/4) = a^(3/2)</span>
</div>
"@
},

@{
  title = "3. Pierwiastki"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>3. Pierwiastki</h3>
<p><strong>ⁿ√a</strong> to liczba b ≥ 0 taka, że bⁿ = a</p>
<h5 class='text-warning mt-3'>Własności pierwiastków:</h5>
<div class='alert alert-secondary'>
  ⁿ√a · ⁿ√b = ⁿ√(ab) &nbsp;&nbsp;|&nbsp;&nbsp; ⁿ√a ÷ ⁿ√b = ⁿ√(a/b)<br>
  ᵐ√(ⁿ√a) = ᵐⁿ√a &nbsp;&nbsp;|&nbsp;&nbsp; (ⁿ√a)ᵐ = ⁿ√(aᵐ)<br>
  ⁿ√(aⁿ) = |a| dla n parzystego &nbsp;&nbsp;|&nbsp;&nbsp; ⁿ√(aⁿ) = a dla n nieparzystego
</div>
<h5 class='text-warning mt-3'>Wyłączanie i włączanie pod pierwiastek:</h5>
<div class='alert alert-secondary'>a · √b = √(a²b) &nbsp;&nbsp;|&nbsp;&nbsp; √(a²b) = a√b dla a ≥ 0</div>
<h5 class='text-warning mt-3'>Usuwanie niewymierności z mianownika:</h5>
<div class='alert alert-secondary'>1/√a = √a/a &nbsp;&nbsp;|&nbsp;&nbsp; 1/(√a−√b) = (√a+√b)/(a−b)</div>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Pierwiastki</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Oblicz: √75 − √27 + √12<br>
  <span class='text-muted'>Odpowiedź: 5√3 − 3√3 + 2√3 = 4√3</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Usuń niewymierność z mianownika: 6/(√3 + 1)<br>
  <span class='text-muted'>Odpowiedź: 6(√3−1)/((√3)²−1²) = 6(√3−1)/2 = 3(√3−1)</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Uprość: √(50x²) dla x ≥ 0<br>
  <span class='text-muted'>Odpowiedź: √(25·2·x²) = 5x√2</span>
</div>
"@
},

@{
  title = "4. Logarytmy"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>4. Logarytmy</h3>
<p><strong>log_a(b) = c</strong> oznacza, że <strong>aᶜ = b</strong> &nbsp;(a &gt; 0, a ≠ 1, b &gt; 0)</p>
<h5 class='text-warning mt-3'>Własności logarytmów:</h5>
<div class='alert alert-secondary'>
  log_a(b·c) = log_a(b) + log_a(c)<br>
  log_a(b/c) = log_a(b) − log_a(c)<br>
  log_a(bⁿ) = n · log_a(b)<br>
  log_a(a) = 1 &nbsp;&nbsp;|&nbsp;&nbsp; log_a(1) = 0<br>
  log_a(b) = log_c(b) / log_c(a) &nbsp;&nbsp;(zmiana podstawy)
</div>
<h5 class='text-warning mt-3'>Logarytm dziesiętny i naturalny:</h5>
<ul>
  <li><strong>log(x)</strong> = log₁₀(x) — logarytm dziesiętny</li>
  <li><strong>ln(x)</strong> = logₑ(x) — logarytm naturalny (e ≈ 2,718)</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Logarytmy</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Oblicz: log₂(32) + log₂(4) − log₂(8)<br>
  <span class='text-muted'>Odpowiedź: 5 + 2 − 3 = 4</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Rozwiąż równanie: log₃(x) = 4<br>
  <span class='text-muted'>Odpowiedź: x = 3⁴ = 81</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Uprość: log₅(125) + log₅(1/25)<br>
  <span class='text-muted'>Odpowiedź: log₅(5³) + log₅(5⁻²) = 3 + (−2) = 1</span>
</div>
"@
},

@{
  title = "5. Procenty"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>5. Procenty</h3>
<p>Procent to jedna setna część: <strong>1% = 1/100 = 0,01</strong></p>
<h5 class='text-warning mt-3'>Wzory:</h5>
<div class='alert alert-secondary'>
  p% z liczby a = a · p/100<br>
  Podwyżka o p%: a · (1 + p/100)<br>
  Obniżka o p%: a · (1 − p/100)<br>
  Jaki % a stanowi b: (b/a) · 100%
</div>
<h5 class='text-warning mt-3'>Procent składany (odsetki):</h5>
<div class='alert alert-secondary'>K = K₀ · (1 + p/100)ⁿ</div>
<p>gdzie K₀ — kapitał początkowy, p — stopa procentowa, n — liczba okresów</p>
<h5 class='text-warning mt-3'>Typowe błędy:</h5>
<ul>
  <li>Podwyżka o 20% i obniżka o 20% NIE dają tej samej ceny!</li>
  <li>1,2 · 0,8 = 0,96 (strata 4%)</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Procenty</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Cena po obniżce o 30% wynosi 140 zł. Jaka była cena przed obniżką?<br>
  <span class='text-muted'>Odpowiedź: x · 0,7 = 140 → x = 200 zł</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Towar podrożał o 15%, a następnie potaniał o 15%. Jaki jest wynikowy procent zmiany?<br>
  <span class='text-muted'>Odpowiedź: 1,15 · 0,85 = 0,9775 → strata 2,25%</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Lokata 1000 zł na 5% rocznie przez 2 lata (procent składany). Ile wynosi końcowa kwota?<br>
  <span class='text-muted'>Odpowiedź: 1000 · 1,05² = 1000 · 1,1025 = 1102,50 zł</span>
</div>
"@
},

@{
  title = "6. Przedziały liczbowe i zbiory"
  chapter = "Rozdział I. Liczby i działania"
  theoryHtml = @"
<h3 class='text-primary'>6. Przedziały liczbowe i zbiory</h3>
<h5 class='text-warning mt-3'>Rodzaje przedziałów:</h5>
<div class='alert alert-secondary'>
  (a, b) — otwarty: a &lt; x &lt; b<br>
  [a, b] — domknięty: a ≤ x ≤ b<br>
  [a, b) — lewostronnie domknięty: a ≤ x &lt; b<br>
  (a, +∞) — nieograniczony: x &gt; a<br>
  (-∞, b] — nieograniczony: x ≤ b
</div>
<h5 class='text-warning mt-3'>Działania na zbiorach:</h5>
<div class='alert alert-secondary'>
  A ∪ B — suma (lub) &nbsp;&nbsp;|&nbsp;&nbsp; A ∩ B — iloczyn (i)<br>
  A \ B — różnica &nbsp;&nbsp;|&nbsp;&nbsp; A ⊂ B — zawieranie
</div>
<h5 class='text-warning mt-3'>Pamiętaj:</h5>
<ul>
  <li>∞ i −∞ zawsze w nawiasie okrągłym (otwartym)</li>
  <li>Punkt izolowany zaznacza się kółkiem pełnym (∈) lub pustym (∉)</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Przedziały liczbowe i zbiory</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Zapisz zbiór rozwiązań: 2x − 3 &lt; 7<br>
  <span class='text-muted'>Odpowiedź: 2x &lt; 10 → x &lt; 5 → x ∈ (−∞, 5)</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Wyznacz A ∩ B, gdzie A = [−2, 5) i B = (1, 8]<br>
  <span class='text-muted'>Odpowiedź: A ∩ B = (1, 5)</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Wyznacz A ∪ B, gdzie A = (−∞, 3] i B = [1, +∞)<br>
  <span class='text-muted'>Odpowiedź: A ∪ B = (−∞, +∞) = ℝ</span>
</div>
"@
},

@{
  title = "11. Równania kwadratowe"
  chapter = "Rozdział III. Równania i nierówności"
  theoryHtml = @"
<h3 class='text-primary'>11. Równania kwadratowe</h3>
<p>Postać ogólna: <strong>ax² + bx + c = 0</strong>, gdzie a ≠ 0</p>
<h5 class='text-warning mt-3'>Wyróżnik (delta):</h5>
<div class='alert alert-secondary'>
  Δ = b² − 4ac<br><br>
  Δ &gt; 0 → dwa rozwiązania: x = (−b ± √Δ) / (2a)<br>
  Δ = 0 → jedno rozwiązanie: x = −b / (2a)<br>
  Δ &lt; 0 → brak rozwiązań rzeczywistych
</div>
<h5 class='text-warning mt-3'>Wzory Viète'a:</h5>
<div class='alert alert-secondary'>x₁ + x₂ = −b/a &nbsp;&nbsp;|&nbsp;&nbsp; x₁ · x₂ = c/a</div>
<h5 class='text-warning mt-3'>Metody rozwiązywania:</h5>
<ul>
  <li>Przez deltę (zawsze działa)</li>
  <li>Przez wyłączenie wspólnego czynnika</li>
  <li>Przez wzory skróconego mnożenia</li>
  <li>Przez podstawienie (równania dwukwadratowe)</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Równania kwadratowe</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Rozwiąż: x² − 5x + 6 = 0<br>
  <span class='text-muted'>Odpowiedź: Δ = 25 − 24 = 1, x₁ = 3, x₂ = 2</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> Rozwiąż: 2x² − 4x + 2 = 0<br>
  <span class='text-muted'>Odpowiedź: Δ = 16 − 16 = 0, x = 1 (podwójny)</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Suma pierwiastków równa 7, iloczyn równa 10. Podaj równanie.<br>
  <span class='text-muted'>Odpowiedź: x² − 7x + 10 = 0</span>
</div>
"@
},

@{
  title = "22. Ciąg arytmetyczny"
  chapter = "Rozdział V. Ciągi"
  theoryHtml = @"
<h3 class='text-primary'>22. Ciąg arytmetyczny</h3>
<p>Ciąg, w którym różnica kolejnych wyrazów jest stała: <strong>aₙ₊₁ − aₙ = r</strong></p>
<h5 class='text-warning mt-3'>Wzory:</h5>
<div class='alert alert-secondary'>
  n-ty wyraz: aₙ = a₁ + (n−1)·r<br>
  Suma n wyrazów: Sₙ = n·(a₁ + aₙ)/2 = n·(2a₁ + (n−1)·r)/2
</div>
<h5 class='text-warning mt-3'>Własności:</h5>
<ul>
  <li>Wyraz środkowy = średnia arytmetyczna sąsiadów: aₙ = (aₙ₋₁ + aₙ₊₁)/2</li>
  <li>r &gt; 0 — ciąg rosnący</li>
  <li>r &lt; 0 — ciąg malejący</li>
  <li>r = 0 — ciąg stały</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Ciąg arytmetyczny</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> a₁ = 3, r = 5. Oblicz a₁₀ i S₁₀.<br>
  <span class='text-muted'>Odpowiedź: a₁₀ = 3 + 9·5 = 48, S₁₀ = 10·(3+48)/2 = 255</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> a₃ = 11, a₇ = 23. Znajdź a₁ i r.<br>
  <span class='text-muted'>Odpowiedź: 4r = 12 → r = 3, a₁ = 11 − 2·3 = 5</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Ile wyrazów ciągu 2, 5, 8, ... jest mniejszych od 100?<br>
  <span class='text-muted'>Odpowiedź: 2 + (n−1)·3 &lt; 100 → n &lt; 34 → 33 wyrazy</span>
</div>
"@
},

@{
  title = "23. Ciąg geometryczny"
  chapter = "Rozdział V. Ciągi"
  theoryHtml = @"
<h3 class='text-primary'>23. Ciąg geometryczny</h3>
<p>Ciąg, w którym iloraz kolejnych wyrazów jest stały: <strong>aₙ₊₁ / aₙ = q</strong></p>
<h5 class='text-warning mt-3'>Wzory:</h5>
<div class='alert alert-secondary'>
  n-ty wyraz: aₙ = a₁ · qⁿ⁻¹<br>
  Suma n wyrazów (q ≠ 1): Sₙ = a₁ · (qⁿ − 1) / (q − 1)<br>
  Suma n wyrazów (q = 1): Sₙ = n · a₁
</div>
<h5 class='text-warning mt-3'>Własności:</h5>
<ul>
  <li>Wyraz środkowy: aₙ² = aₙ₋₁ · aₙ₊₁ (średnia geometryczna)</li>
  <li>q &gt; 1 i a₁ &gt; 0 — ciąg rosnący</li>
  <li>0 &lt; q &lt; 1 i a₁ &gt; 0 — ciąg malejący</li>
</ul>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Ciąg geometryczny</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> a₁ = 3, q = 2. Oblicz a₅ i S₅.<br>
  <span class='text-muted'>Odpowiedź: a₅ = 3·2⁴ = 48, S₅ = 3·(2⁵−1)/(2−1) = 93</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> a₂ = 6, a₄ = 54. Znajdź q i a₁.<br>
  <span class='text-muted'>Odpowiedź: q² = 54/6 = 9 → q = 3, a₁ = 6/3 = 2</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> Trzy liczby tworzą ciąg geometryczny: 4, x, 36. Znajdź x.<br>
  <span class='text-muted'>Odpowiedź: x² = 4·36 = 144 → x = 12</span>
</div>
"@
},

@{
  title = "41. Prawdopodobieństwo"
  chapter = "Rozdział X. Statystyka i prawdopodobieństwo"
  theoryHtml = @"
<h3 class='text-primary'>41. Prawdopodobieństwo</h3>
<p>Prawdopodobieństwo zdarzenia A: <strong>P(A) = |A| / |Ω|</strong></p>
<p>gdzie |A| — liczba sprzyjających wyników, |Ω| — liczba wszystkich wyników</p>
<h5 class='text-warning mt-3'>Własności:</h5>
<div class='alert alert-secondary'>
  0 ≤ P(A) ≤ 1<br>
  P(Ω) = 1 &nbsp;&nbsp;|&nbsp;&nbsp; P(∅) = 0<br>
  P(A') = 1 − P(A) &nbsp;&nbsp;(zdarzenie przeciwne)<br>
  P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
</div>
<h5 class='text-warning mt-3'>Zdarzenia niezależne:</h5>
<div class='alert alert-secondary'>P(A ∩ B) = P(A) · P(B)</div>
<h5 class='text-warning mt-3'>Prawdopodobieństwo warunkowe:</h5>
<div class='alert alert-secondary'>P(A|B) = P(A ∩ B) / P(B)</div>
"@
  tasksHtml = @"
<h3 class='text-success'>Zadania: Prawdopodobieństwo</h3>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 1.</strong> Rzucamy dwiema kostkami. Jakie jest prawdopodobieństwo, że suma oczek wynosi 7?<br>
  <span class='text-muted'>Odpowiedź: korzystne: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) → 6/36 = 1/6</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 2.</strong> W urnie 4 białe i 6 czarnych kul. Losujemy 1. Jakie P(biała)?<br>
  <span class='text-muted'>Odpowiedź: P = 4/10 = 2/5</span>
</div>
<div class='mb-4 p-3 border border-secondary rounded'>
  <strong>Zadanie 3.</strong> P(A) = 0,4, P(B) = 0,3, zdarzenia niezależne. Oblicz P(A ∩ B) i P(A ∪ B).<br>
  <span class='text-muted'>Odpowiedź: P(A ∩ B) = 0,12 &nbsp;|&nbsp; P(A ∪ B) = 0,4 + 0,3 − 0,12 = 0,58</span>
</div>
"@
}
)

Write-Host "Wysylam $($topics.Count) tematow do API..." -ForegroundColor Cyan

$sukces = 0
$blad = 0

foreach ($topic in $topics) {
    $json = $topic | ConvertTo-Json -Depth 10
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
    
    try {
        $response = Invoke-WebRequest -Uri $API -Method POST -Body $bytes -ContentType "application/json; charset=utf-8" -ErrorAction Stop
        Write-Host "OK: $($topic.title)" -ForegroundColor Green
        $sukces++
    } catch {
        Write-Host "BLAD: $($topic.title) - $($_.Exception.Message)" -ForegroundColor Red
        $blad++
    }
    
    Start-Sleep -Milliseconds 100
}

Write-Host ""
Write-Host "Gotowe! Sukces: $sukces | Bledy: $blad" -ForegroundColor Yellow