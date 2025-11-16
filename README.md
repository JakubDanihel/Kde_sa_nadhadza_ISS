# Kde_sa_nadhadza_ISS
Kratky program ktory zasle mail kde sa bude nachadzat ISS nad zadanou plohou v kode. Tento mail bude poslany na zadanu adresu.

## 1. Účel skriptu

Tento Python skript slúži ako automatizovaný nástroj na sledovanie polohy ISS. Jeho hlavnou úlohou je:

1.  Zistiť aktuálnu polohu ISS pomocou verejného API.
2.  Zistiť, či je na vašej polohe noc (keďže ISS je viditeľná iba v tme).
3.  Porovnať polohu ISS s vašou geografickou polohou.
4.  Ak je ISS vo vašej blízkosti a zároveň je noc, odoslať vám e-mailové upozornenie.

Skript je navrhnutý tak, aby bol ľahko konfigurovateľný.

## 2. Príprava a inštalácia

Pred spustením skriptu je potrebné vykonať nasledujúce kroky:

### a) Inštalácia potrebných knižníc

Skript vyžaduje knižnicu `requests`. Nainštalujte ju pomocou príkazu `pip`:

```sh
pip install requests
```

-   `requests`: Na odosielanie HTTP požiadaviek a komunikáciu s API.

### b) Konfigurácia v súbore `main.py`

Priamo v kóde je potrebné nastaviť niekoľko konštánt:

-   `MY_LAT`: Vaša zemepisná šírka (napr. `48.1478`).
-   `MY_LONG`: Vaša zemepisná dĺžka (napr. `17.1072`).
-   `MY_MAIL`: Vaša e-mailová adresa, z ktorej sa bude posielať upozornenie (napr. Gmail).
-   `MY_PW`: **Heslo pre aplikáciu**, nie vaše bežné heslo k e-mailu. Z bezpečnostných dôvodov poskytovatelia ako Gmail vyžadujú vygenerovanie jedinečného hesla pre externé aplikácie, ktoré pristupujú k vášmu účtu.

```python
# Moja poloha
MY_LAT = 48.1478
MY_LONG = 17.1072

# Prihlasovacie údaje do emailu
MY_MAIL = "vas_email@gmail.com"
MY_PW = "vase_heslo_pre_aplikaciu"
```

## 3. Štruktúra kódu

Kód je rozdelený do niekoľkých logických častí pre lepšiu prehľadnosť.

### a) Importy a Konštanty

Na začiatku sa importujú potrebné knižnice (`requests`, `datetime`, `smtplib`) a definujú sa konštanty pre geografickú polohu a prihlasovacie údaje.

### b) Funkcia `is_iss_overhead()`

```python
def is_iss_overhead():
    # ...
```

Táto funkcia zisťuje aktuálnu polohu ISS z API `http://api.open-notify.org/iss-now.json`.
-   **Výstup:** Vráti `True`, ak sa ISS nachádza v tolerancii +/- 5 stupňov od vašej polohy. V opačnom prípade vráti `False`.

### c) Funkcia `is_night()`

```python
def is_night():
    # ...
```

Táto funkcia zisťuje, či je na vašej polohe noc. Používa na to API `https://api.sunrise-sunset.org/json`, z ktorého získa časy východu a západu slnka.
-   **Výstup:** Vráti `True`, ak je aktuálny čas po západe slnka alebo pred jeho východom. V opačnom prípade vráti `False`.

### d) Hlavná logika

```python
if is_iss_overhead() and is_night():
    # ...
```

Táto časť sa vykoná, iba ak sú obe podmienky splnené (ISS je blízko a je noc). Spojí sa so SMTP serverom (v tomto prípade Gmail), prihlási sa a odošle e-mailové upozornenie.

## 4. Ako spustiť skript

1.  Otvorte terminál alebo príkazový riadok.
2.  Prejdite do priečinka, kde máte uložený projekt.
3.  Spustite skript príkazom:
    ```sh
    python main.py
    ```

Skript vykoná jednu kontrolu a následne sa ukončí. Pre pravidelné monitorovanie by bolo potrebné tento skript spúšťať automaticky v určitých intervaloch (napr. pomocou Cron job na Linuxe/macOS alebo Plánovača úloh vo Windows).
