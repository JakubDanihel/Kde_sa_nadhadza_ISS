import requests
from datetime import datetime
import smtplib

MY_LAT = 48.1478 # GPS vyska
MY_LONG = 17.1072 # GPS sirka

#ulozenie mailovej adresy a hesla pre dalsie pozuzitie
MY_MAIL = "mail_na_testovanie@gmail.com"
MY_PW = "heslo_pre_mail_z_nastaveni"

#zistenie ci je ISS nad suradnicou
def is_iss_overhead():

    #ziskanie API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    #ziskanie suradnic ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Moja pozicia  +-5 stupnou od ISS
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#urcenie ci je noc
def is_night():
    #zistenie mojich parametrov
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    #pomocou API zistit kedy je na mojich suradniciach vychod a zapad slnka
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #zistenie sucasneho casu
    time_now = datetime.now().hour

    #porovnanie ci je prave teraz noc (ISS si nevsimnes vobec na dennej oblohe je potrebna nocna obloha)
    if time_now >= sunset or time_now <=sunrise:
        return True

#spustenie samotneho kodu
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL, MY_PW)
    connection.sendmail(
        from_addr=MY_MAIL,
        to_addrs=MY_MAIL,
        msg="Subject: Look Up\n\nThis is ISS nad tebou na oblohe"
    )


