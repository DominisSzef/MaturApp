import urllib.request
import json

API = httplocalhost8080apitopics

topics = [
    {
        title 1. Liczby rzeczywiste,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'1. Liczby rzeczywisteh3pZbior liczb rzeczywistych strongu211dstrong obejmuje wszystkie liczby wymierne i niewymierne.ph5 class='text-warning mt-3'Rodzaje liczbh5ullistrongNaturalne (u2115)strong 1, 2, 3, ...lilistrongCau0142kowite (u2124)strong ..., -2, -1, 0, 1, 2, ...lilistrongWymierne (u211a)strong liczby postaci pq, np. 12, 0.75lilistrongNiewymiernestrong u221a2, u03c0 &mdash; nie da siu0119 zapisau0107 jako uu0142amekliulh5 class='text-warning mt-3'Wartou015bu0107 bezwzglu0119dnah5div class='alert alert-secondary'a = a gdy a &ge; 0 &nbsp;&nbsp; a = -a gdy a &lt; 0div,
        tasksHtml h3 class='text-success'Zadania Liczby rzeczywisteh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Oblicz -8 + 3 - -2brspan class='text-muted'Odpowiedu017a 8 + 3 - 2 = 9spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Dla jakich x x - 3 = 5brspan class='text-muted'Odpowiedu017a x = 8 lub x = -2spandiv
    },
    {
        title 2. Potu0119gi,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'2. Potu0119gih3pPotu0119ga strongau207f = a &middot; a &middot; ... &middot; astrong (n razy)ph5 class='text-warning mt-3'Dziau0142ania na potu0119gachh5div class='alert alert-secondary'au1d50 &middot; au207f = au1d50u207au207f &nbsp;&nbsp; au1d50 &divide; au207f = au1d50u207bu207f &nbsp;&nbsp; (au1d50)u207f = au1d50u207fbrau2070 = 1 &nbsp;&nbsp; au207bu207f = 1au207f &nbsp;&nbsp; a^(pq) = u1da0u221a(au1d56)div,
        tasksHtml h3 class='text-success'Zadania Potu0119gih3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Uprość 2u00b3 &middot; 2u2075 &divide; 2u2074brspan class='text-muted'Odpowiedu017a 2^(3+5-4) = 2u2074 = 16spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Oblicz (3u00b2)u00b3 &divide; 3u2074brspan class='text-muted'Odpowiedu017a 3u2076 &divide; 3u2074 = 3u00b2 = 9spandiv
    },
    {
        title 3. Pierwiastki,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'3. Pierwiastkih3pstrongu207fu221aastrong to liczba b &ge; 0 taka, u017ce bu207f = aph5 class='text-warning mt-3'Wu0142asnou015bcih5div class='alert alert-secondary'u207fu221aa &middot; u207fu221ab = u207fu221a(ab) &nbsp;&nbsp; u207fu221aa &divide; u207fu221ab = u207fu221a(ab)brUsuwanie niewymiernou015bci 1u221aa = u221aaadiv,
        tasksHtml h3 class='text-success'Zadania Pierwiastkih3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Oblicz u221a75 - u221a27 + u221a12brspan class='text-muted'Odpowiedu017a 5u221a3 - 3u221a3 + 2u221a3 = 4u221a3spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Usuu0144 niewymiernou015bu0107 6(u221a3 + 1)brspan class='text-muted'Odpowiedu017a 3(u221a3 - 1)spandiv
    },
    {
        title 4. Logarytmy,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'4. Logarytmyh3pstronglog_a(b) = cstrong oznacza, u017ce strongau1d9c = bstrong (a &gt; 0, a &ne; 1, b &gt; 0)ph5 class='text-warning mt-3'Wu0142asnou015bcih5div class='alert alert-secondary'log_a(b&middot;c) = log_a(b) + log_a(c)brlog_a(bc) = log_a(b) - log_a(c)brlog_a(bu207f) = n &middot; log_a(b)brlog_a(a) = 1 &nbsp;&nbsp; log_a(1) = 0div,
        tasksHtml h3 class='text-success'Zadania Logarytmyh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Oblicz logu2082(32) + logu2082(4) - logu2082(8)brspan class='text-muted'Odpowiedu017a 5 + 2 - 3 = 4spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Rozwiu0105u017c logu2083(x) = 4brspan class='text-muted'Odpowiedu017a x = 81spandiv
    },
    {
        title 5. Procenty,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'5. Procentyh3p1% = 1100 = 0,01ph5 class='text-warning mt-3'Wzoryh5div class='alert alert-secondary'p% z liczby a = a &middot; p100brPodwyu017cka o p% a &middot; (1 + p100)brObniu017cka o p% a &middot; (1 - p100)brProcent sku0142adany K = Ku2080 &middot; (1 + p100)u207fdiv,
        tasksHtml h3 class='text-success'Zadania Procentyh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Cena po obniu017cce o 30% wynosi 140 zu0142. Jaka byu0142a cena przed obniu017cku0105brspan class='text-muted'Odpowiedu017a 200 zu0142spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Lokata 1000 zu0142 na 5% rocznie przez 2 lata. Ile wynosi kou0144cowa kwotabrspan class='text-muted'Odpowiedu017a 1102,50 zu0142spandiv
    },
    {
        title 6. Przedziau0142y liczbowe i zbiory,
        chapter Rozdziau0142 I. Liczby i dziau0142ania,
        theoryHtml h3 class='text-primary'6. Przedziau0142y liczbowe i zbioryh3h5 class='text-warning mt-3'Rodzaje przedziau0142u00f3wh5div class='alert alert-secondary'(a,b) otwart a &lt; x &lt; bbr[a,b] domkniu0119ty a &le; x &le; bbr[a,b) pu00f3u0142otwarty a &le; x &lt; bbr(a,+u221e) nieograniczony x &gt; adivh5 class='text-warning mt-3'Dziau0142ania na zbiorachh5div class='alert alert-secondary'A u222a B &mdash; suma &nbsp;&nbsp; A u2229 B &mdash; iloczyn &nbsp;&nbsp; A  B &mdash; ru00f3u017cnicadiv,
        tasksHtml h3 class='text-success'Zadania Przedziau0142yh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Zapisz zbiu00f3r rozwiu0105zau0144 2x - 3 &lt; 7brspan class='text-muted'Odpowiedu017a x &isin; (-u221e, 5)spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Wyznacz A u2229 B, gdzie A = [-2,5) i B = (1,8]brspan class='text-muted'Odpowiedu017a (1, 5)spandiv
    },
    {
        title 7. Wielomiany,
        chapter Rozdziau0142 II. Algebra,
        theoryHtml h3 class='text-primary'7. Wielomianyh3pWielomian stopnia n strongW(x) = au2099xu207f + au2099u208bu2081xu207fu207bu00b9 + ... + au2081x + au2080strongph5 class='text-warning mt-3'Dziau0142aniah5ulliDodawanie u0142u0105czenie wyrazu00f3w podobnychliliMnou017cenie kau017cdy przez kau017cdegoliliDzielenie schemat Hornera lub pisemneliulh5 class='text-warning mt-3'Pierwiastek wielomianuh5div class='alert alert-secondary'Jeu015bli W(a) = 0, to (x - a) jest dzielnikiem W(x)div,
        tasksHtml h3 class='text-success'Zadania Wielomianyh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Sprawdu017a czy x=2 jest pierwiastkiem W(x) = xu00b3 - 3x + 2brspan class='text-muted'Odpowiedu017a W(2) = 8 - 6 + 2 = 4 &ne; 0, wiu0119c nie jest pierwiastkiem. W(1) = 1-3+2 = 0, x=1 jest pierwiastkiem.spandiv
    },
    {
        title 8. Wzory skru00f3conego mnou017cenia,
        chapter Rozdziau0142 II. Algebra,
        theoryHtml h3 class='text-primary'8. Wzory skru00f3conego mnou017ceniah3div class='alert alert-secondary'(a+b)u00b2 = au00b2 + 2ab + bu00b2br(a-b)u00b2 = au00b2 - 2ab + bu00b2br(a+b)(a-b) = au00b2 - bu00b2br(a+b)u00b3 = au00b3 + 3au00b2b + 3abu00b2 + bu00b3br(a-b)u00b3 = au00b3 - 3au00b2b + 3abu00b2 - bu00b3brau00b3 + bu00b3 = (a+b)(au00b2 - ab + bu00b2)brau00b3 - bu00b3 = (a-b)(au00b2 + ab + bu00b2)div,
        tasksHtml h3 class='text-success'Zadania Wzory skru00f3conego mnou017ceniah3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Oblicz (x+3)u00b2 - (x-3)u00b2brspan class='text-muted'Odpowiedu017a (xu00b2+6x+9) - (xu00b2-6x+9) = 12xspandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Rozlou017c na czynniki xu00b2 - 16brspan class='text-muted'Odpowiedu017a (x+4)(x-4)spandiv
    },
    {
        title 9. Ru00f3wnania i nieru00f3wnou015bci liniowe,
        chapter Rozdziau0142 III. Ru00f3wnania i nieru00f3wnou015bci,
        theoryHtml h3 class='text-primary'9. Ru00f3wnania i nieru00f3wnou015bci linioweh3pRu00f3wnanie liniowe strongax + b = 0strong, rozwiu0105zanie x = -ba (a &ne; 0)ph5 class='text-warning mt-3'Nieru00f3wnou015bci &mdash; uwagah5div class='alert alert-warning'Przy mnou017ceniudzieleniu przez liczbu0119 ujemnu0105 &mdash; odwracamy znak nieru00f3wnou015bci!divdiv class='alert alert-secondary'ax &gt; b &nbsp;u21d2&nbsp; x &gt; ba (gdy a &gt; 0) lub x &lt; ba (gdy a &lt; 0)div,
        tasksHtml h3 class='text-success'Zadania Ru00f3wnania linioweh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Rozwiu0105u017c 3x - 7 = 2x + 5brspan class='text-muted'Odpowiedu017a x = 12spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Rozwiu0105u017c nieru00f3wnou015bu0107 -2x + 4 &gt; 10brspan class='text-muted'Odpowiedu017a -2x &gt; 6 u21d2 x &lt; -3, x &isin; (-u221e, -3)spandiv
    },
    {
        title 10. Uku0142ad ru00f3wnau0144,
        chapter Rozdziau0142 III. Ru00f3wnania i nieru00f3wnou015bci,
        theoryHtml h3 class='text-primary'10. Uku0142ad ru00f3wnau0144h3pUku0142ad dwu00f3ch ru00f3wnau0144 z dwiema niewiadomymi x, y.ph5 class='text-warning mt-3'Metody rozwiu0105zywaniah5ullistrongPodstawianiastrong wyrau017c jednu0105 zmiennu0105 i podstaw do drugiego ru00f3wnanialilistrongEliminacjistrong dodajodejmij ru00f3wnania aby wyeliminowau0107 zmiennu0105lilistrongGraficznastrong punkt przeciu0119cia dwu00f3ch prostychliul,
        tasksHtml h3 class='text-success'Zadania Uku0142ad ru00f3wnau0144h3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Rozwiu0105u017c x + y = 10 i x - y = 4brspan class='text-muted'Odpowiedu017a dodaj ru00f3wnania 2x = 14 u21d2 x = 7, y = 3spandiv
    },
    {
        title 11. Ru00f3wnania kwadratowe,
        chapter Rozdziau0142 III. Ru00f3wnania i nieru00f3wnou015bci,
        theoryHtml h3 class='text-primary'11. Ru00f3wnania kwadratoweh3pPostau0107 ogu00f3lna strongaxu00b2 + bx + c = 0strong, gdzie a &ne; 0ph5 class='text-warning mt-3'Wyru00f3u017cnik (delta)h5div class='alert alert-secondary'u0394 = bu00b2 - 4acbrbru0394 &gt; 0 u2192 dwa rozwiu0105zania x = (-b &plusmn; u221au0394)  (2a)bru0394 = 0 u2192 jedno x = -b(2a)bru0394 &lt; 0 u2192 brak rozwiu0105zau0144divh5 class='text-warning mt-3'Wzory Vietu00e8ah5div class='alert alert-secondary'xu2081+xu2082 = -ba &nbsp;&nbsp; xu2081&middot;xu2082 = cadiv,
        tasksHtml h3 class='text-success'Zadania Ru00f3wnania kwadratoweh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Rozwiu0105u017c xu00b2 - 5x + 6 = 0brspan class='text-muted'Odpowiedu017a u0394=1, xu2081=3, xu2082=2spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Suma pierwiastku00f3w = 7, iloczyn = 10. Podaj ru00f3wnanie.brspan class='text-muted'Odpowiedu017a xu00b2 - 7x + 10 = 0spandiv
    },
    {
        title 12. Nieru00f3wnou015bci kwadratowe,
        chapter Rozdziau0142 III. Ru00f3wnania i nieru00f3wnou015bci,
        theoryHtml h3 class='text-primary'12. Nieru00f3wnou015bci kwadratoweh3pPostau0107 strongaxu00b2 + bx + c &gt; 0strong (lub &lt;, &ge;, &le;)ph5 class='text-warning mt-3'Metodah5olliZnajdu017a miejsca zerowe (rozwiu0105u017c ru00f3wnanie kwadratowe)liliNarysuj parabolu0119 (ramiona gu00f3ra gdy a&gt;0, du00f3u0142 gdy a&lt;0)liliOdczytaj przedziau0142y speu0142niaju0105ce nieru00f3wnou015bu0107lioldiv class='alert alert-secondary'a &gt; 0, u0394 &gt; 0 axu00b2+bx+c &gt; 0 dla x &isin; (-u221e,xu2081) u222a (xu2082,+u221e)div,
        tasksHtml h3 class='text-success'Zadania Nieru00f3wnou015bci kwadratoweh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Rozwiu0105u017c xu00b2 - 4 &gt; 0brspan class='text-muted'Odpowiedu017a (x-2)(x+2) &gt; 0, x &isin; (-u221e,-2) u222a (2,+u221e)spandiv
    },
    {
        title 14. Wu0142asnou015bci funkcji,
        chapter Rozdziau0142 IV. Funkcje,
        theoryHtml h3 class='text-primary'14. Wu0142asnou015bci funkcjih3ullistrongDziedzinastrong zbiu00f3r argumentu00f3w xlilistrongZbiu00f3r wartou015bcistrong zbiu00f3r wartou015bci f(x)lilistrongMiejsce zerowestrong x dla ktu00f3rego f(x)=0lilistrongMonotonicznou015bu0107strong rosnu0105ca  maleju0105calilistrongRu00f3u017cznou015bu0107strong kau017cdemu y odpowiada co najwyu017cej jedno xlilistrongParzystou015bu0107strong f(-x)=f(x); nieparzystou015bu0107 f(-x)=-f(x)liul,
        tasksHtml h3 class='text-success'Zadania Wu0142asnou015bci funkcjih3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Podaj dziedzinu0119 f(x) = u221a(x-3)brspan class='text-muted'Odpowiedu017a x - 3 &ge; 0, D = [3, +u221e)spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Czy f(x) = xu00b2 jest parzystabrspan class='text-muted'Odpowiedu017a f(-x) = (-x)u00b2 = xu00b2 = f(x), tak &mdash; jest parzystaspandiv
    },
    {
        title 15. Wykresy, wzory i wspu00f3u0142czynniki funkcji liniowej,
        chapter Rozdziau0142 IV. Funkcje,
        theoryHtml h3 class='text-primary'15. Funkcja liniowah3pPostau0107 strongf(x) = ax + bstrongpullistrongastrong &mdash; wspu00f3u0142czynnik kierunkowy (nachylenie prostej)lilistrongbstrong &mdash; wyraz wolny (przeciu0119cie z osiu0105 Y)liulh5 class='text-warning mt-3'Wu0142asnou015bcih5div class='alert alert-secondary'a &gt; 0 u2192 rosnu0105ca &nbsp;&nbsp; a &lt; 0 u2192 maleju0105ca &nbsp;&nbsp; a = 0 u2192 stau0142abrMiejsce zerowe x = -babrProste ru00f3wnolegu0142e au2081 = au2082 &nbsp;&nbsp; Proste prostopadu0142e au2081 &middot; au2082 = -1div,
        tasksHtml h3 class='text-success'Zadania Funkcja liniowah3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Znajdu017a miejsce zerowe f(x) = 3x - 9brspan class='text-muted'Odpowiedu017a 3x - 9 = 0 u21d2 x = 3spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Prosta y = 2x + 1. Jaki wspu00f3u0142czynnik ma prosta prostopadu0142abrspan class='text-muted'Odpowiedu017a a = -12spandiv
    },
    {
        title 16. Wykresy funkcji kwadratowej,
        chapter Rozdziau0142 IV. Funkcje,
        theoryHtml h3 class='text-primary'16. Funkcja kwadratowa &mdash; wykresyh3pWykres funkcji kwadratowej to strongparabolastrong.pullia &gt; 0 u2192 ramiona skierowane w gu00f3ru0119 (uu015bmiech)lilia &lt; 0 u2192 ramiona skierowane w du00f3u0142 (smutek)liulh5 class='text-warning mt-3'Wierzchou0142ek parabolih5div class='alert alert-secondary'xu1d68 = -b(2a) &nbsp;&nbsp; yu1d68 = f(xu1d68) = -u0394(4a)div,
        tasksHtml h3 class='text-success'Zadania Wykres funkcji kwadratowejh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Podaj wspu00f3u0142rzu0119dne wierzchou0142ka f(x) = xu00b2 - 4x + 3brspan class='text-muted'Odpowiedu017a xu1d68 = 2, yu1d68 = 4 - 8 + 3 = -1, W = (2, -1)spandiv
    },
    {
        title 17. Wzory i wspu00f3u0142czynniki funkcji kwadratowej,
        chapter Rozdziau0142 IV. Funkcje,
        theoryHtml h3 class='text-primary'17. Wzory funkcji kwadratowejh3div class='alert alert-secondary'strongPostau0107 ogu00f3lnastrong f(x) = axu00b2 + bx + cbrstrongPostau0107 kanonicznastrong f(x) = a(x - xu1d68)u00b2 + yu1d68brstrongPostau0107 iloczynowa (gdy u0394&ge;0)strong f(x) = a(x - xu2081)(x - xu2082)div,
        tasksHtml h3 class='text-success'Zadania Wzory funkcji kwadratowejh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Zapisz w postaci kanonicznej f(x) = xu00b2 - 6x + 5brspan class='text-muted'Odpowiedu017a xu1d68=3, yu1d68=-4, f(x) = (x-3)u00b2 - 4spandiv
    },
    {
        title 21. Ciu0105gi liczbowe,
        chapter Rozdziau0142 V. Ciu0105gi,
        theoryHtml h3 class='text-primary'21. Ciu0105gi liczboweh3pCiu0105g to funkcja f u2115 u2192 u211d. Oznaczamy au2081, au2082, au2083, ...pullistrongWyraz ogu00f3lnystrong wzru00f3r na au2099lilistrongWzru00f3r rekurencyjnystrong au2099u208au2081 wyrau017cony przez poprzednie wyrazylilistrongMonotonicznou015bu0107strong rosnu0105cy gdy au2099u208au2081 &gt; au2099, maleju0105cy gdy au2099u208au2081 &lt; au2099liul,
        tasksHtml h3 class='text-success'Zadania Ciu0105gi liczboweh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Podaj 5 pierwszych wyrazu00f3w ciu0105gu au2099 = 2n - 1brspan class='text-muted'Odpowiedu017a 1, 3, 5, 7, 9spandiv
    },
    {
        title 22. Ciu0105g arytmetyczny,
        chapter Rozdziau0142 V. Ciu0105gi,
        theoryHtml h3 class='text-primary'22. Ciu0105g arytmetycznyh3pRu00f3u017cnica kolejnych wyrazu00f3w jest stau0142a strongau2099u208au2081 - au2099 = rstrongpdiv class='alert alert-secondary'n-ty wyraz au2099 = au2081 + (n-1)&middot;rbrSuma n wyrazu00f3w Su2099 = n&middot;(au2081 + au2099)2div,
        tasksHtml h3 class='text-success'Zadania Ciu0105g arytmetycznyh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong au2081=3, r=5. Oblicz au2081u2080 i Su2081u2080.brspan class='text-muted'Odpowiedu017a au2081u2080=48, Su2081u2080=255spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong au2083=11, au2087=23. Znajdu017a r i au2081.brspan class='text-muted'Odpowiedu017a r=3, au2081=5spandiv
    },
    {
        title 23. Ciu0105g geometryczny,
        chapter Rozdziau0142 V. Ciu0105gi,
        theoryHtml h3 class='text-primary'23. Ciu0105g geometrycznyh3pIloraz kolejnych wyrazu00f3w jest stau0142y strongau2099u208au2081  au2099 = qstrongpdiv class='alert alert-secondary'n-ty wyraz au2099 = au2081 &middot; qu207fu207bu00b9brSuma (q&ne;1) Su2099 = au2081 &middot; (qu207f - 1)  (q - 1)div,
        tasksHtml h3 class='text-success'Zadania Ciu0105g geometrycznyh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong au2081=3, q=2. Oblicz au2085 i Su2085.brspan class='text-muted'Odpowiedu017a au2085=48, Su2085=93spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Trzy liczby tworzu0105 ciu0105g geometryczny 4, x, 36. Znajdu017a x.brspan class='text-muted'Odpowiedu017a x=12spandiv
    },
    {
        title 32. Ru00f3wnanie prostej,
        chapter Rozdziau0142 VIII. Geometria analityczna,
        theoryHtml h3 class='text-primary'32. Ru00f3wnanie prostejh3div class='alert alert-secondary'strongPostac kierunkowastrong y = ax + bbrstrongPostac ogu00f3lnastrong Ax + By + C = 0brstrongPrzez dwa punktystrong (y-yu2081)(yu2082-yu2081) = (x-xu2081)(xu2082-xu2081)divh5 class='text-warning mt-3'Wspu00f3u0142czynnik kierunkowy przez 2 punktyh5div class='alert alert-secondary'a = (yu2082 - yu2081)  (xu2082 - xu2081)div,
        tasksHtml h3 class='text-success'Zadania Ru00f3wnanie prostejh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Znajdu017a ru00f3wnanie prostej przez A=(1,2) i B=(3,8)brspan class='text-muted'Odpowiedu017a a=(8-2)(3-1)=3, y-2=3(x-1), y=3x-1spandiv
    },
    {
        title 39. Statystyka,
        chapter Rozdziau0142 X. Statystyka i prawdopodobieu0144stwo,
        theoryHtml h3 class='text-primary'39. Statystykah3div class='alert alert-secondary'strongu015arednnia arytmetycznastrong xu0305 = (xu2081+xu2082+...+xu2099)nbrstrongMedianastrong wartou015bu0107 u015brodkowa po posortowaniubrstrongModastrong wartou015bu0107 najczu0119u015bciej wystu0119puju0105cabrstrongOdchylenie standardowestrong miara rozproszenia danychdiv,
        tasksHtml h3 class='text-success'Zadania Statystykah3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Oblicz u015bredniu0105 i medianu0119 3, 7, 5, 9, 1brspan class='text-muted'Odpowiedu017a u015brednia=5, po sortowaniu 1,3,5,7,9, mediana=5spandiv
    },
    {
        title 40. Kombinatoryka,
        chapter Rozdziau0142 X. Statystyka i prawdopodobieu0144stwo,
        theoryHtml h3 class='text-primary'40. Kombinatorykah3div class='alert alert-secondary'strongSilniastrong n! = 1&middot;2&middot;3&middot;...&middot;nbrstrongPermutacjestrong (kolejnou015bu0107 ma znaczenie) P(n) = n!brstrongWariacjestrong (k z n, powtarzaju0105ce siu0119) W = nu1d4fbrstrongKombinacjestrong (kolejnou015bu0107 nie ma znaczenia) C(n,k) = n!(k!(n-k)!)div,
        tasksHtml h3 class='text-success'Zadania Kombinatorykah3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Na ile sposobu00f3w mou017cna ustawiu0107 5 osu00f3b w rzu0119dziebrspan class='text-muted'Odpowiedu017a 5! = 120spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong Ile 3-elementowych podzbioru00f3w ma zbior 5-elementowybrspan class='text-muted'Odpowiedu017a C(5,3) = 10spandiv
    },
    {
        title 41. Prawdopodobieu0144stwo,
        chapter Rozdziau0142 X. Statystyka i prawdopodobieu0144stwo,
        theoryHtml h3 class='text-primary'41. Prawdopodobieu0144stwoh3pP(A) = A  u03a9 (liczba korzystnych  liczba wszystkich)pdiv class='alert alert-secondary'0 &le; P(A) &le; 1brP(A') = 1 - P(A)brP(A u222a B) = P(A) + P(B) - P(A u2229 B)brZdarzenia niezaleu017cne P(A u2229 B) = P(A) &middot; P(B)div,
        tasksHtml h3 class='text-success'Zadania Prawdopodobieu0144stwoh3div class='mb-4 p-3 border border-secondary rounded'strongZadanie 1.strong Rzucamy dwiema kostkami. P(suma = 7)brspan class='text-muted'Odpowiedu017a 636 = 16spandivdiv class='mb-4 p-3 border border-secondary rounded'strongZadanie 2.strong W urnie 4 biau0142e i 6 czarnych kul. P(biau0142a)brspan class='text-muted'Odpowiedu017a 410 = 25spandiv
    }
]

print(fWysylam {len(topics)} tematow...)
sukces = 0
blad = 0

for topic in topics
    data = json.dumps(topic, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(API, data=data, headers={'Content-Type' 'applicationjson; charset=utf-8'}, method='POST')
    try
        with urllib.request.urlopen(req, timeout=10) as resp
            print(fOK {topic['title']})
            sukces += 1
    except Exception as e
        print(fBLAD {topic['title']} - {e})
        blad += 1

print(fnGotowe! Sukces {sukces}  Bledy {blad})