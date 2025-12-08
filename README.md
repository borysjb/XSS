# XSS Attacks - Instrukcja

## Prerequisites:

- Przeglądarka internetowa
- Konto w [WebSecurity Academy](https://portswigger.net/web-security)
- Opcjonalnie: [Burp Suite](https://portswigger.net/burp/communitydownload)
- Podstawowa znajomość HTML oraz Javascript

## Materiały referencyjne:

- [Podstawy XSS](https://portswigger.net/web-security/cross-site-scripting), może komuś lepiej siądzie inne wytłumaczenie :)
- [Cheat Sheet z payloadami](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

## Stored XSS

### [Laboratorium 1](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

<summary> <b> Kliknij aby rozwinąć kolejne wskazówki </b> </summary>
<details> <summary> 1. </summary>
Znajdź formularz zapisujący dane po stronie serwera.
</details>
<details> <summary> 2.</summary>
Wstaw payload w komentarz
</details>
<details>
  <summary> 3. - Rozwiązanie</summary>
  Payload `<script> alert(1);</script>`
</details>

### [Laboratorium 2] (https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped)

W tym laboratorim przyda się Burpsuite

<summary> <b> Kliknij aby rozwinąć kolejne wskazówki</b></summary>
<details>
  <summary> 1. </summary>
  Przyjrzyj się jak aplikacja przetwarza komentarz po opublikowaniu go, szukaj parametrów `onclick`
</details>
<details><summary>2.</summary>
Sprawdź jak aplikacja filtruje znaki w parametrze "Website", i w jaki sposób trafiają one do `onclick`
</details>
<details><summary>3.</summary>
Zastanów się (wygooglaj) jak można sprawić aby `onclick` wykonał więcej niż jedną funkcję JS
</details>
