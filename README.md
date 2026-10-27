# Host- und Broadcast-Rechner

Ein Python-Konsolenprogramm, das für ein IPv4-Netzwerk in CIDR-Schreibweise (z. B. `192.168.10.0/24`) die **Anzahl der nutzbaren Hostadressen** und die **Broadcastadresse** berechnet.

Die Berechnung erfolgt bewusst „zu Fuß“ über die Binärdarstellung der IP-Adresse, ohne Hilfsbibliotheken wie `ipaddress`. So lässt sich jeder Rechenschritt nachvollziehen.

## Aufgabenstellung

### 3. Host-Adressen

Mit einem Pythonprogramm soll die Anzahl der Host-Adressen für `/8` bzw. `/12` ermittelt werden.

| Netzwerk | Erwartetes Ergebnis |
|---|---|
| `10.0.0.0/8` | 16.777.214 nutzbare Host-Adressen |
| `10.0.0.0/12` | 1.048.574 nutzbare Host-Adressen |

### 4. Broadcast

Es soll ein Pythonprogramm zur Berechnung der Broadcast-Adresse erstellt werden.

| Netzwerk | Erwartetes Ergebnis |
|---|---|
| `10.0.0.0/24` | 10.0.0.255 |
| `10.0.0.0/23` | 10.0.1.255 |
| `192.168.1.0/25` | 192.168.1.127 |

Das Programm löst beide Teilaufgaben in einem Durchlauf: Es liest eine IPv4-Adresse oktettweise samt CIDR-Wert ein, berechnet die Anzahl der Hostadressen und ermittelt anschließend über die Binärdarstellung die Broadcastadresse.

## Funktionsweise

| Funktion | Aufgabe |
|---|---|
| `main()` | Steuert den Ablauf und ruft die Funktionen nacheinander auf |
| `ip_eingeben()` | Liest die vier Oktette (je 0–255) und den CIDR-Wert ein, wiederholt die Eingabe bei ungültigen Werten und gibt die Adresse im Format `a.b.c.d/n` zurück |
| `hostanteilrechner()` | Berechnet die Hostadressen: `2^(32 − CIDR) − 2` (Netz- und Broadcastadresse werden abgezogen) |
| `ip_in_binaer()` | Wandelt jedes Oktett in 8 Bit um und liefert eine Liste mit 32 Bits |
| `broadcast_ermitteln()` | Setzt alle Hostbits (die letzten `32 − CIDR` Bits) auf `1` |
| `broadcast_in_dezimal()` | Rechnet die 32 Bits wieder in vier Dezimal-Oktette um und gibt die Broadcastadresse aus |

### Beispiel

Für `192.168.10.0/24`:

- Hostanteil: 32 − 24 = 8 Bit → 2⁸ − 2 = **254 Hostadressen**
- Binär: `11000000 10101000 00001010 00000000`
- Hostbits auf 1: `11000000 10101000 00001010 11111111`
- Broadcastadresse: **192.168.10.255**

## Getestete Werte aus der Aufgabe

| Eingabe | Hostadressen | Broadcast |
|---|---|---|
| `10.0.0.0/8` | 16.777.214 | 10.255.255.255 |
| `10.0.0.0/12` | 1.048.574 | 10.15.255.255 |
| `10.0.0.0/24` | 254 | 10.0.0.255 |
| `10.0.0.0/23` | 510 | 10.0.1.255 |
| `192.168.1.0/25` | 126 | 192.168.1.127 |

## Voraussetzungen

- Python 3.6 oder neuer (wegen der f-Strings)
- Ein Terminal, das ANSI-Farbcodes darstellen kann (die Ergebnisse werden gelb hervorgehoben)

Zusätzliche Pakete sind nicht nötig.

## Verwendung

Repository klonen und das Programm starten:

```bash
git clone https://github.com/pycr4m/host_broadcastrechner.git
cd host_broadcastrechner
python host_adressen.py
```

Das Programm fragt nacheinander jedes Oktett und danach den CIDR-Wert ab:

```text
Gib das 1. Oktett ein: 192
Gib das 2. Oktett ein: 168
Gib das 3. Oktett ein: 10
Gib das 4. Oktett ein: 0
Gib den Cider für 192.168.10.0/ ein: 24
Rückgabe ip_eingeben string_ip_liste: 192.168.10.0/24

Rückgabe hostanteilrechner: Für 192.168.10.0/24 mit 24er-Cider gibt es 254 Hostadressen.
...
Rückgabewert für broadcast_in_dezimal: Die Broadcastadresse des Netzwerks lautet: 192.168.10.255
```

## Eingabeprüfung

- Oktette müssen ganze Zahlen von 0 bis 255 sein.
- Der CIDR-Wert muss eine ganze Zahl sein. Bei ungültiger Eingabe erscheint eine Fehlermeldung und die Eingabe wird wiederholt.

## Bekannte Einschränkungen und Ideen für später

- Es wird nur die Broadcastadresse berechnet, nicht die Netzadresse oder die erste und letzte Hostadresse.
- Die Umrechnung von Binär nach Dezimal in `broadcast_in_dezimal()` ist mit vielen einzelnen `if`-Abfragen gelöst und könnte mit einer Schleife deutlich kürzer werden.
- `ip_in_binaer()` ließe sich ebenfalls mit einer Schleife oder `format(oktett, "08b")` vereinfachen.
- Der CIDR-Wert wird aktuell nur bis 31 akzeptiert; `/32` ist nicht möglich.

## Autor

[pycr4m](https://github.com/pycr4m)
