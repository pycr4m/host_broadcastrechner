def main():
    cidr_wert, string_ip_liste, ip_liste = ip_eingeben()
    hostanteilrechner(cidr_wert, string_ip_liste)
    liste_binaer, string_liste_binaer = ip_in_binaer(ip_liste)
    liste_broadcast_binaer = broadcast_ermitteln(liste_binaer, cidr_wert)
    broadcast_in_dezimal(liste_broadcast_binaer)

def ip_eingeben():
    oktett_range = []
    for i in range(256):
        oktett_range.append(i)
        i += 1

    ip_liste = []
    for oktett in range(4):
        while True:
            try:
                oktett_wert = input(f"Gib das {oktett+1}. Oktett ein: ")
                if int(oktett_wert) in oktett_range:
                    ip_liste.append(oktett_wert)
                    ip_liste.append(".")
                    break
                else:
                    print("Gibt einen Wert zwischen 0 und 255 ein!")
                    continue
            except ValueError:
                print("Gibt einen Wert zwischen 0 und 255 ein!")

    ip_liste[7] = "/"

    string_ip_liste = ""
    for element in ip_liste:
        string_ip_liste += element

    cidr_range = []
    for i in range(32):
        cidr_range.append(i)
        i += 1

    while True:
        try:
            cidr_wert = input(f"Gib den cidr für {string_ip_liste} ein: ")
            if int(cidr_wert) in cidr_range:
                ip_liste.append(cidr_wert)
                break
            else:
                print("Gibt einen Wert zwischen 1 und 31 ein!")
                continue
        except ValueError:
            print("Gibt einen Wert zwischen 1 und 31 ein!")
    string_ip_liste = ""
    for element in ip_liste:
        string_ip_liste += element
    print(f"Rückgabe ip_eingeben string_ip_liste: \033[1;1;33m{string_ip_liste}\033[0m")
    return cidr_wert, string_ip_liste, ip_liste

def hostanteilrechner(cidr_wert, string_ip_liste):
    hostanteil = 32 - int(cidr_wert)
    hostadressen = 1
    for exponent in range(0,hostanteil):
        hostadressen = 2* hostadressen
    hostadressen = hostadressen -2
    print()
    print(f"Rückgabe hostanteilrechner: Für {string_ip_liste} mit {cidr_wert}er-cidr gibt es \033[1;1;33m{hostadressen:,} Hostadressen\033[0m.".replace(",", "."))
    return hostadressen

def ip_in_binaer(ip_liste):
    erstes_oktett = ip_liste[0]
    zweites_oktett = ip_liste[2]
    drittes_oktett = ip_liste[4]
    viertes_oktett = ip_liste[6]

    ip_int_list = [erstes_oktett] + [zweites_oktett] + [drittes_oktett] + [viertes_oktett]
    anhaenger = [0, 0, 0, 0, 0, 0, 0, 0]
    liste_binaer = []
    
    for oktett in ip_int_list:
        oktett = int(oktett)
        if oktett >= 128:
            anhaenger[0] = 1
            oktett = oktett -128
        if oktett >= 64:
            anhaenger[1] = 1
            oktett = oktett -64
        if oktett >= 32:
            anhaenger[2] = 1
            oktett = oktett -32
        if oktett >= 16:
            anhaenger[3] = 1
            oktett = oktett -16
        if oktett >= 8:
            anhaenger[4] = 1
            oktett = oktett -8
        if oktett >= 4:
            anhaenger[5] = 1
            oktett = oktett -4
        if oktett >= 2:
            anhaenger[6] = 1
            oktett = oktett -2
        if oktett >= 1:
            anhaenger[7] = 1
            oktett = oktett -1
        liste_binaer = liste_binaer + anhaenger
        anhaenger = [0, 0, 0, 0, 0, 0, 0, 0]

    string_liste_binaer = ""
    for i in liste_binaer:
        string_liste_binaer = string_liste_binaer + str(i)
    print()
    print(f"Rückgabe ip_in_binaer string_liste_binaer: {string_liste_binaer}")
    print(f"Rückgabe ip_in_binaer liste_binaer: {liste_binaer}")
    return liste_binaer, string_liste_binaer

def broadcast_ermitteln(liste_binaer, cidr_wert):
    hostanteil = (len(liste_binaer) - int(cidr_wert))
    
    for host_bit in range(hostanteil):
        liste_binaer[32 -hostanteil + host_bit] = 1
    liste_broadcast_binaer = liste_binaer
    print()
    print(f"Rückgabe broadcast_ermitteln liste_binaer: {liste_broadcast_binaer}")
    return liste_broadcast_binaer

def broadcast_in_dezimal(liste_broadcast_binaer):
    # for oktett in liste_broadcast_binaer                       VERBESSERUNGSPOTENTIAL
    # liste_broadcast_dezimal = 0
    erstes_oktett = 0
    zweites_oktett = 0
    drittes_oktett = 0
    viertes_oktett = 0

    if liste_broadcast_binaer[0] == 1:
        erstes_oktett += 128
    if liste_broadcast_binaer[1] == 1:
        erstes_oktett += 64
    if liste_broadcast_binaer[2] == 1:
        erstes_oktett += 32
    if liste_broadcast_binaer[3] == 1:
        erstes_oktett += 16
    if liste_broadcast_binaer[4] == 1:
        erstes_oktett += 8
    if liste_broadcast_binaer[5] == 1:
        erstes_oktett += 4
    if liste_broadcast_binaer[6] == 1:
        erstes_oktett += 2
    if liste_broadcast_binaer[7] == 1:
        erstes_oktett += 1

    if liste_broadcast_binaer[8] == 1:
        zweites_oktett += 128
    if liste_broadcast_binaer[9] == 1:
        zweites_oktett += 64
    if liste_broadcast_binaer[10] == 1:
        zweites_oktett += 32
    if liste_broadcast_binaer[11] == 1:
        zweites_oktett += 16
    if liste_broadcast_binaer[12] == 1:
        zweites_oktett += 8
    if liste_broadcast_binaer[13] == 1:
        zweites_oktett += 4
    if liste_broadcast_binaer[14] == 1:
        zweites_oktett += 2
    if liste_broadcast_binaer[15] == 1:
        zweites_oktett += 1

    if liste_broadcast_binaer[16] == 1:
        drittes_oktett += 128
    if liste_broadcast_binaer[17] == 1:
        drittes_oktett += 64
    if liste_broadcast_binaer[18] == 1:
        drittes_oktett += 32
    if liste_broadcast_binaer[19] == 1:
        drittes_oktett += 16
    if liste_broadcast_binaer[20] == 1:
        drittes_oktett += 8
    if liste_broadcast_binaer[21] == 1:
        drittes_oktett += 4
    if liste_broadcast_binaer[22] == 1:
        drittes_oktett += 2
    if liste_broadcast_binaer[23] == 1:
        drittes_oktett += 1

    if liste_broadcast_binaer[24] == 1:
        viertes_oktett += 128
    if liste_broadcast_binaer[25] == 1:
        viertes_oktett += 64
    if liste_broadcast_binaer[26] == 1:
        viertes_oktett += 32
    if liste_broadcast_binaer[27] == 1:
        viertes_oktett += 16
    if liste_broadcast_binaer[28] == 1:
        viertes_oktett += 8
    if liste_broadcast_binaer[29] == 1:
        viertes_oktett += 4
    if liste_broadcast_binaer[30] == 1:
        viertes_oktett += 2
    if liste_broadcast_binaer[31] == 1:
        viertes_oktett += 1

    liste_broadcast_dezimal = str(erstes_oktett) + "." + str(zweites_oktett) + "." + str(drittes_oktett) + "." + str(viertes_oktett)
    print()
    print(f"Rückgabewert für broadcast_in_dezimal: Die Broadcastadresse des Netzwerks lautet: \033[1;1;33m{erstes_oktett}.{zweites_oktett}.{drittes_oktett}.{viertes_oktett}\033[0m")
    return liste_broadcast_dezimal

main()