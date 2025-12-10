# Laboratorium: XSS
Justyna Michalik, Hubert Korzeniowski, Borys Jarnot-Bałuszek  
11.12.2025

## 1. Wstęp
W ramach tego laboratorium zajmiemy się analizą oraz praktycznym wykorzystaniem podatności typu **Cross-Site Scripting (XSS)**.  
Ćwiczenia wykonujemy z użyciem platformy **PortSwigger Web Security Academy**, która udostępnia interaktywne scenariusze ataków. :contentReference[oaicite:2]{index=2}

### Wymagania i narzędzia
- Przeglądarka internetowa (Chrome / Firefox)  
- Konto w PortSwigger Web Security Academy: https://portswigger.net/web-security  
- Opcjonalnie: Burp Suite (Community / Pro): https://portswigger.net/burp/communitydownload  
- Podstawowa znajomość HTML oraz JavaScript  

## 2. Cele laboratorium
1. Zrozumieć, czym jest XSS i dlaczego stanowi zagrożenie.  
2. Poznać różnice między:
   - Reflected XSS,  
   - Stored XSS,  
   - DOM-based XSS.  
3. Wykonać praktyczne laboratoria PortSwigger.  
4. Poznać techniki obrony i filtracji danych.  

## 3. Materiały referencyjne
- Podstawy XSS: https://portswigger.net/web-security/cross-site-scripting  
- Payloady testowe (cheat sheet):  
  https://portswigger.net/web-security/cross-site-scripting/cheat-sheet  

---

# 4. Zadania laboratoryjne

---

## 4.1 Zadanie 1 – Reflected XSS  
**Laboratorium:**  
https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked

### Kroki
<div class="step">1. Sprawdź, jak aplikacja reaguje na różne tagi HTML w parametrze search. Podpowiedź: nie wszystkie tagi są traktowane tak samo. </div>
<div class="step">2. Zauważ, że część tagów jest filtrowana, ale pewne niestandardowe tagi nie podlegają blokadzie — spróbuj użyć tagu, który nie istnieje w HTML. </div>
<div class="step">3. Sprawdź, czy w niestandardowych tagach aplikacja zachowuje atrybuty i czy można wykorzystać takie atrybuty do wywołania zdarzeń. </div>
<div class="step">4. Zaprojektuj sposób automatycznego wywołania zdarzenia bez udziału użytkownika — pamiętaj, że element musi być możliwy do aktywowania przez przeglądarkę. </div>
<div class="step">5. Przeglądarka przy nawigacji do fragmentu #id może próbować ustawić fokus lub przesunąć widok — połącz to z eventem reagującym na fokus. </div>
<div class="step">6. Stwórz własny niestandardowy element z odpowiednimi właściwościami, aby uzyskać automatyczne wykonanie JS. </div>

---

## 4.2 Zadanie 2 – Stored XSS

### Laboratorium 1 (łatwe)  
https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded  

### Kroki
<div class="step">1. Znajdź formularz zapisujący dane po stronie serwera.</div>
<div class="step">2. Wstaw payload w komentarz: &lt;script&gt;alert(1)&lt;/script&gt; </div>

---

### Laboratorium 2 (mniej łatwe)  
https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped  

To laboratorium opiera się na tym samym blogu co poprzednie, lecz zawiera dodatkowe mechanizmy filtracji, które są niepełne, co prowadzi do podatności. :contentReference[oaicite:3]{index=3}

### Kroki
<div class="step">1. Przeanalizuj dokładnie, jak aplikacja przetwarza pole “Website” w komentarzu i zobacz, gdzie trafia ono w generowanym HTML. </div>
<div class="step">2. Sprawdź filtrowanie znaków — porównaj surowy input i finalny HTML wyświetlany przez przeglądarkę.</div>
<div class="step">3. Zwróć uwagę na działanie HTML Entities wewnątrz atrybutów JS, np. onclick="...". Zwłaszcza na sposób kodowania apostrofów: [url][encoded ’] - alert(1) - [encoded ’]</div>

---

## 4.3 Zadanie 3 – DOM-based XSS

---

### Laboratorium 1  
https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink  

To laboratorium prezentuje zagrożenie wynikające z używania `innerHTML` bez filtrowania.

### Kroki
<div class="step">1. Wyszukaj coś na stronie — zobaczysz, że strona generuje fragment HTML wyświetlający twoje zapytanie.</div>
<div class="step">2. Sprawdź, jak aplikacja reaguje na różne tagi HTML (np. &lt;i&gt;, &lt;b&gt;).</div>
<div class="step">3. Otwórz konsolę deweloperską i przeanalizuj kod JS.</div>
<div class="step">4. Znajdź fragment, który operuje na location.search — zobaczysz, że twoje wyszukiwanie tam trafia, więc nie musisz ręcznie edytować adresu URL.</div>
<div class="step">5. Zaprojektuj payload manipulujący DOM, wstrzykujący JS.</div>
<div class="step">6. Spoiler: &lt;img src=x onerror=alert(1)&gt;</div>

---

### Laboratorium 2  
https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink  

To laboratorium działa podobnie do poprzedniego, ale zamiast `innerHTML` używa `document.write`.  

### Kroki
<div class="step">1. Wpisz dowolną wartość w pole input na stronie.</div>
<div class="step">2. Zauważ, że podobnie jak wcześniej — brak filtrowania przed wstawieniem wartości do HTML.</div>
<div class="step">3. Przeglądając kod, zauważysz, że input trafia bezpośrednio do document.write.</div>
<div class="step">4. Zaprojektuj payload umożliwiający wstrzyknięcie skryptu. </div>
<div class="step">5. W URL po query znajduje się sekwencja `">`, co pozwala na zakończenie aktualnego znacznika i wstawienie własnego HTML.</div>
<div class="step">6. Spoiler: `&quot;&gt;&lt;svg onload=alert(1)&gt;`</div>


---

<style>
.step {
  color: #384;
  background: #444;
  padding: 6px;
  margin: 4px 0;
  border-radius: 6px;
  transition: 0.3s;
  opacity: 0.25;
}
.step:hover {
  opacity: 1;
  background: #e8e8e8;
}
</style>
