# Antwoorden

### Oefening 2.
Het programma loopt vast op regel 48. Het zit hier in een oneindige while-loop.

### Oefening 3.
Het lijkt erop dat er per ongeluk een nieuwe variabele aangemaakt wordt vanwege een spellingsfout. self.naem wordt aangemaakt, maar waarschijnlijk is het de bedoeling dat self.name wordt aangepast.

### Oefening 5.
Ja

Ja, dat betekent dat beide variabelen naar dezelfde geheugenlocatie verwijzen.

Name heeft een nieuw adres gekregen, naam verwijst nog naar het oude. Voor name is er een nieuw adres in het geheugen vrijgemaakt om "Davis" op te slaan, er daar wijst de variabele nu naar. Voor naam is er niets veranderd, deze wijst nog naar hetzelfde adres.

Ja, x is nog beschikbaar in de scope. Als ik x type in de evaluation bar en op enter druk, krijg ik "2" te zien.

Name is niet meer beschikbaar in de module scope.

De waarde van x staat nog steeds op 2. Dit komt omdat het statement "x = 4" in de init van Student een lokale variabele x aanmaakt en deze op 4 zet. Wanneer we uit de init steppen wordt deze variabele weggegooid. Dit is makkelijk te zien door een watch op id(x) toe te voegen en de lokale x-variabele te renamen naar bijvoorbeeld x_2 en daar met id(x_2) ook een watch op toe te voegen.

Nu wordt er geen lokale variabele x aangemaakt door "x = 4", maar wordt de globale variabele x aangepast naar 4.

### Oefening 6.
De waarde van what_am_i is 2.2254363327930515, na 72 iteraties. v1 en v2 zijn op dat moment "["

De code loopt nu niet meer vast in de oneindige while-loop.