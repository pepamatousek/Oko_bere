from random import choice
from os import system
import platform


from karty import karty
from karty import vaha_karet
import json


info = """+-----------------------------------------------------------------------+
| Stručný popis:                                                        |
| --------------                                                        |
| Ve hře inspirované hrou "Oko bere" se hráč snaží vyhrát bank,         |
| který v rukou drží bankéř a je stanoven na 1000 BTCo.                 |
| Hráč na začátku hry disponuje vkladem na kontě 500 BTCo.              |
| Minimální vklad pro spuštění jedné hry je 50 BTCo.                    |
|                                                                       |
| Průběh hry:                                                           |
| -----------                                                           |    
| Hráč obdrží první karu a potom jednu kartu obdrží bankéř.             |
| Hráč musí vložit minimální vklad a dostává druhou kartu.              |
| Nedrží-li hráč v rukou dvě esa, která představují oko bere a          |
| následně jsou automaticky vyloženy karty bankéře k porovnání,         |
| může si hráč vybrat ze tří možností:                                  |
| - navýšit vklad a dostat další kartu                                  |
| - dostat další kartu                                                  |
| - vyložit karty                                                       |
|                                                                       |
| Pravidla:                                                             |
| ---------                                                             |
| Má-li hráč vyšší skóre než bankéř, hráč vyhrává dvojnásobek vkladu.   |
| Jedná-li se o remízu skóre, vklad vyhrává bankéř.                     |
| V případě, kdy přesáhne hráč skóre 21 automaticky prohrává.           |
|                                                                       |
| Závěr:                                                                |
| ------                                                                |
| Mají-li obě strany prostředky ke hraní, hru je možné opakovat.        |
| Hra se opakuje s aktuálním stavem hráčova konta a banku.              |
| Hra probíhá, dokud hráč nebo bankéř nezbankrotují :)                  |
| Hráč vyhrává po rozbití banku. Tzn. tehdy, když hráč disponuje        |
| 1500 BTC na svém kontě.                                               |
| V případě, kdy hráč disponuje 0 BTC na kontě jedná se o "Game over!"  |
|                                                                       |
| Hodně štěstí !!!                                                      |
+-----------------------------------------------------------------------+"""


jsi_registrovan = """+------------------------------+
|      JSI ZAREGISTROVÁN?      |
|       ANO [a]   NE [n]       |
+------------------------------+"""


registrace = """+------------------------------+
|          REGISTRACE          |
+------------------------------+"""


prihlaseni = """+------------------------------+
|          PRIHLASENI          |
+------------------------------+"""


tabulka = """+------------------------------+
|           REKORDY            |
+------------------------------+
| hrac         |  vítězné kolo |
+------------------------------+"""


o_autorovi = """+-----------------------------------------------------------------------+
| O autorovi:                                                           |
| -----------                                                           |
| Ing. Josef Matoušek                                                   |
| emai: jmatousek.jobs@icloud.com                                       |
|                                                                       |
| V případě chyb ve hře, připomínek,...                                 |
| Mě prosím kontatkujte....                                             |
+-----------------------------------------------------------------------+"""


hra = True

hraci = json.load(open('hraci'))

rekordy = json.load(open('rekordy'))

if platform.system() == "Windows":
    command = "cls"
elif platform.system() == "Darwin":
    command = "clear"

elif platform.system() == "Linux":
    command = "clear"

else:
    command = "clear"


# def 1
def uvodni_menu():
    system(command)
    print(
    "+" + "-" * 37 + "+",        
    f"| Hra # OKO BERE #                    |",
    "+" + "-" * 37 + "+", 
    f"| MENU                                |",
    f"|------                               |",
    f"| - pro spuštění hry zadej [s]        |",
    f"| - pro informace o hře zadej [i]     |",
    f"| - pro tabulku rekordů zadej [t]     |",
    # f"| - pro tabulku registrovaných [d]    |",
    f"| - pro ukončení zadej [k]            |",
    f"| - pro o autorovi zadej [o]          |",
    "+" + "-" * 37 + "+", 
    sep="\n"
    )


def registrace_dinamicka():
    system(command)
    print(registrace)
    print(f"| Jméno hráče:".ljust(0), f"{jmeno_hrace} |".rjust(17))
    print(f"| Klíč hráče:".ljust(0), f"{klic} |".rjust(18))
    print("+------------------------------+")


def prihlaseni_dinamicke():
    system(command)
    print(prihlaseni)
    print(f"| Jméno hráče:".ljust(0), f"{jmeno_hrace} |".rjust(17))
    print(f"| Klíč hráče:".ljust(0), f"{klic} |".rjust(18))
    print("+------------------------------+")


def serazeni_a_tisk_tabulky():
    # serazene_rekordy = {key: value for key, value in sorted(rekordy.items(), reverse = True)}
    serazene_rekordy = {key: value for key, value in sorted(rekordy.items(), key = lambda value: value[1])}   

    # tisk tabylky
    max_hodnot = 0
    print(tabulka)
    for key, value in serazene_rekordy.items():
        max_hodnot += 1 
        print(
            f"| {key}", f"{value}. kolo |".rjust(29-len(key))
            )
        if max_hodnot == 20:
            break
    print("+------------------------------+")


while hra != "k":

# menu hry
    uvodni_menu()
    hra = input("-> ")

    # overeni zadaných hodnot
    while hra != "s":
        # system(command)
        # uvodni_menu()

        if hra == "i":
            system(command)
            print(info)
            print(f"- pro návrat do menu zadej [z]")
            hra = input("-> ")
            while hra != "z":
                system(command)
                print(info)
                print(f"- pro návrat do menu zadej [z]")
                print(f"- zadal jsi neplatnou hodnotu...")
                hra = input("-> ")

        elif hra == "t":
            system(command)
            serazeni_a_tisk_tabulky()
            print(f"- pro návrat do menu zadej [z]")
            hra = input("-> ")
            while hra != "z":
                system(command)
                serazeni_a_tisk_tabulky()
                print(f"- pro návrat do menu zadej [z]")
                print(f"- zadal jsi neplatnou hodnotu...")
                hra = input("-> ")       

        # elif hra == "d":
        #     system(command)
        #     print(hraci)
        #     print(f"- pro návrat do menu zadej [z]")
        #     hra = input("-> ")
        #     while hra != "z":
        #         system(command)
        #         print(hraci)
        #         print(f"- pro návrat do menu zadej [z]")
        #         print(f"- zadal jsi neplatnou hodnotu...")
        #         hra = input("-> ")     

        elif hra == "k":
            system(command)
            quit()

        elif hra == "o":
            system(command)
            print(o_autorovi)
            print(f"- pro návrat do menu zadej [z]")
            hra = input("-> ")
            while hra != "z":
                system(command)
                print(o_autorovi)
                print(f"- pro návrat do menu zadej [z]")
                print(f"- zadal jsi neplatnou hodnotu...")
                hra = input("-> ")

        elif hra == "z":
            uvodni_menu()
            hra = input("-> ")

        else:
            uvodni_menu()
            print(f"Zadal jsi neplatnou hodnotu...")
            hra = input("-> ")

    # registrace
    jmeno_hrace = ""
    klic = ""

    # výběr ano/ne  
    system(command)
    print(jsi_registrovan)
    host = input("-> ")     
              
    while True:  

        # ověření zadání z váběru ano/ne u registrován
        if host == "n":
            break

        elif host == "a":
            break
        
        else:
            system(command)
            print(jsi_registrovan)

            print(
                f"Vyber z možností [a] nebo [n]"
                )

            host = input("-> ")

    if host == "n":  

        # porovnání registrace s registrovanými a kontrola max. počtu znaků 7

        while True:
            registrace_dinamicka()
            host = input("-> ")

            while True:

                if host in hraci.keys():
                    registrace_dinamicka()
                    print("Jméno jiš je registrováno...")
                    host = input("-> ")

                elif len(host) > 7:
                    registrace_dinamicka()
                    print("Jméno může mít max. 7 znaků...")
                    host = input("-> ")

                else:
                    jmeno_hrace = host
                    registrace_dinamicka()
                    break
            
            host = input("-> ")
            
            while True:
                if len (host) > 7:
                    registrace_dinamicka()
                    print("Klíč může mít max. 7 znaků...")
                    host = input("-> ")
                else:
                    klic = host
                    break
                    
            while True:
                registrace_dinamicka()
                print(
                    f"- pro potvrzení stiskni [enter]",
                    f"- pro návrat do menu zadej [z]",
                    sep ="\n"
                    )
                host = input("-> ")
                
                if host == "":
                    break
                elif host == "z":
                    break
            
            if host == "z":
                break
            
            if host == "":
                hraci.update({jmeno_hrace: klic})
                if jmeno_hrace in hraci:
                    registrace_dinamicka()
                    # uložení uživatele
                    j = json.dumps(hraci)
                    with open("hraci", 'w') as f:
                        f.write(j)
                        f.close()

                    print(
                        f"Úspěšně zaregistrován!",
                        f"- pro vstup do hry stiskni [enter]",
                        sep ="\n"
                        )
                    host = input("-> ")

                    while host != "":
                        registrace_dinamicka()
                        print(
                            f"Úspěšně zaregistrován!",
                            f"- pro vstup do hry stiskni [enter]",
                            sep="\n"
                            )
                        host = input("-> ")
                else:
                    print("ERROR")            
            
            if host == "":
                break                        

        if host == "z":
            continue

    elif host == "a":
            prihlaseni_dinamicke()
            host = input("-> ")
            
            while True:
                prihlaseni_dinamicke()
                if host in hraci:
                    jmeno_hrace = host
                    break
                else:
                    print(
                        f"Neplatný úživatel {host}...",
                        f"- zadej znovu nebo...",
                        f"- pro návrat do menu zadej [z]",
                        sep="\n")
                    host = input("-> ")
                    if host == "z":
                        break
            if host == "z":
                continue

            while True:
                prihlaseni_dinamicke()
                host = input("-> ")          
                
                while True:
                    prihlaseni_dinamicke()
                    if len(host) <= 7:
                        klic = host
                        break
                    else:
                        print(f"Klíč může mít max. 7 znaků...")
                        host = input("-> ")           
                
                while True:
                    if hraci.get(jmeno_hrace) == klic:
                        break
                    else:
                        prihlaseni_dinamicke()
                        print(
                            f"Nesprávné heslo...",
                            f"- pro opravu hesla zadej [o]",
                            f"- pro návrat do menu zadej [z]",
                            sep ="\n"
                            )
                        host = input("-> ") 
                        if host == "o" or host == "z":
                            break

                # při opravě klíče, odebrání hesla
                if host == "o":
                    klic = ""
                    continue
                else:
                    break

            if host == "z":
                continue

            prihlaseni_dinamicke()
            print(
                f"Úspěšně přihlášen!",
                f"- pro vstup do hry stiskni [enter]",
                sep="\n"
                )
            host = input("-> ")

            while host != "":
                prihlaseni_dinamicke()
                print(
                    f"Úspěšně přihlášen!",
                    f"- pro vstup do hry stiskni [enter]",
                    sep="\n"
                    )
                host = input("-> ")

    # j = json.dumps(hraci)
    # with open("Hraci", 'w') as f:
    #     f.write(j)
    #     f.close()

    # nastaveni hry
    bank = 1000
    hracovo_konto = 500
    kolo = 0

    while True:
        delka_oddelovace = 54
        oddelovac = "+" + ("-" * delka_oddelovace) + "+"
        minimalni_sazka = 50

        # balíček karet
        rozdane_karty = []

        # hra hráč
        hodnota_karty_hrac = []
        barva_karty_hrac = []
        vaha_karty_hrac = []
        skore_hrac = 0
        vsazeno = 0
        
        #hra bankéř
        hodnota_karty_banker = []
        barva_karty_banker = []
        vaha_karty_banker = []
        skore_banker = 0
        skore_banker_none = "##"
        prvni_karta_banker = 0

        kolo += 1
        suma_karet = 0
        status = "Hra běží..."

        # def 2

        def uvitani():
            print(oddelovac)
            print("|" + f"VÍTEJ VE HŘE OKO BERE!".center(delka_oddelovace) + "|")
        

        def stav_hry():

            # interaktivní nastavení rozměru ?? čísla ??
            print(oddelovac)
            print(
                # "|" + 
                f"| {status} |".center(delka_oddelovace)
                #  + "|"
                )

        def hrac():
            print(oddelovac)
            
            print(
                f"| Hráč: {jmeno_hrace}".ljust(0),
                f"{kolo}. kolo |".rjust(delka_oddelovace - len(jmeno_hrace) - 7)
                )
            
            print(
                f"| Konto hráče: {hracovo_konto} BTCo".ljust(0),
                f"Vsazeno: {vsazeno} BTCo |".rjust(delka_oddelovace - 19 - len(str(hracovo_konto)))
                )
            

            print(
                f"| Hráčovo skóré: {skore_hrac}".ljust(0),
                f"Minimální sázka: {minimalni_sazka} BTCo |".rjust(delka_oddelovace - 16 - len(str(skore_hrac)))
                )
            
            print(oddelovac)


        def vykresli_karty_hrace(hodnota_karty_hrac: list, barva_karty_hrac: list): 

            # výpis prvního řádku,...
            for index, hodnota in enumerate(hodnota_karty_hrac, 0):

                if index == 0 and len(hodnota_karty_hrac) > 1:
                    print("| +---+", end=" ")

                elif len(hodnota_karty_hrac) == 1:
                    print("| +---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                elif index == (len(hodnota_karty_hrac) - 1):
                    print("+---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                else:
                    print("+---+", end=" ")
            print(sep="\n")

            # výpis druhého řádku s čísly, kde může nastat varianta s dvojciferným číslem...
            for index, hodnota in enumerate(hodnota_karty_hrac, 0):
                
                if index == 0 and len(hodnota_karty_hrac) > 1:

                    if len(hodnota) == 1:
                        print(f"| |{hodnota}  |", end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"| |{hodnota} |", end=" ")

                elif len(hodnota_karty_hrac) == 1:

                    if len(hodnota) == 1:
                        print(f"| |{hodnota}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"| |{hodnota} |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                elif index == (len(hodnota_karty_hrac) - 1):

                    if len(hodnota) == 1:
                        print(f"|{hodnota}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                    elif len(str(hodnota)) == 2:
                        print(f"|{hodnota} |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                else:
                    if len(hodnota) == 1:
                        print(f"|{hodnota}  |", end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"|{hodnota} |", end=" ")

            print(sep="\n")

            # výpis třetího řádku,...
            for index, barva in enumerate(barva_karty_hrac, 0):

                if index == 0 and len(hodnota_karty_hrac) > 1:
                    print(f"| |{barva}  |", end=" ")

                elif len(hodnota_karty_hrac) == 1:
                    print(f"| |{barva}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                elif index == (len(hodnota_karty_hrac) - 1):
                    print(f"|{barva}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                else:
                    print(f"|{barva}  |", end=" ")

            print(sep="\n")

            # výpis čtvrtého řádku,...
            for index, barva in enumerate(barva_karty_hrac, 0):
                
                if index == 0 and len(hodnota_karty_hrac) > 1:
                    print("| +---+", end=" ")
                
                elif len(hodnota_karty_hrac) == 1:
                    print(f"| +---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")


                elif index == (len(hodnota_karty_hrac) - 1):
                    print(f"+---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_hrac)), end=" ")

                else:
                    print("+---+", end=" ")

            print(sep="\n")

            print(oddelovac)


        def banker_uvodni_karta():
            for _ in range(1):
                print("| +---+".ljust(0), "+-+-+---+ |".rjust(delka_oddelovace - 6))
                print("| |x  |".ljust(0), "|x|x|x  | |".rjust(delka_oddelovace - 6))
                print("| |  x|".ljust(0), "| | |  x| |".rjust(delka_oddelovace - 6))
                print("| +---+".ljust(0), "+-+-+---+ |".rjust(delka_oddelovace - 6))


        def vykresli_karty_bankere(hodnota_karty_banker: list, barva_karty_banker: list): 

            # výpis prvního řádku,...
            for index, hodnota in enumerate(hodnota_karty_banker, 0):

                if index == 0 and len(hodnota_karty_banker) > 1:
                    print("| +---+", end=" ")

                elif len(hodnota_karty_banker) == 1:
                    print("| +---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                elif index == (len(hodnota_karty_banker) - 1):
                    print("+---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                else:
                    print("+---+", end=" ")
            print(sep="\n")

            # výpis druhého řádku s čísly, kde může nastat varianta s dvojciferným číslem...
            for index, hodnota in enumerate(hodnota_karty_banker, 0):
                
                if index == 0 and len(hodnota_karty_banker) > 1:

                    if len(hodnota) == 1:
                        print(f"| |{hodnota}  |", end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"| |{hodnota} |", end=" ")

                elif len(hodnota_karty_banker) == 1:

                    if len(hodnota) == 1:
                        print(f"| |{hodnota}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"| |{hodnota} |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                elif index == (len(hodnota_karty_banker) - 1):

                    if len(hodnota) == 1:
                        print(f"|{hodnota}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                    elif len(str(hodnota)) == 2:
                        print(f"|{hodnota} |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                else:
                    if len(hodnota) == 1:
                        print(f"|{hodnota}  |", end=" ")
                
                    elif len(str(hodnota)) == 2:
                        print(f"|{hodnota} |", end=" ")

            print(sep="\n")

            # výpis třetího řádku,...
            for index, barva in enumerate(barva_karty_banker, 0):

                if index == 0 and len(hodnota_karty_banker) > 1:
                    print(f"| |{barva}  |", end=" ")

                elif len(hodnota_karty_banker) == 1:
                    print(f"| |{barva}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                elif index == (len(hodnota_karty_banker) - 1):
                    print(f"|{barva}  |","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                else:
                    print(f"|{barva}  |", end=" ")

            print(sep="\n")

            # výpis čtvrtého řádku,...
            for index, barva in enumerate(barva_karty_banker, 0):
                
                if index == 0 and len(hodnota_karty_banker) > 1:
                    print("| +---+", end=" ")
                
                elif len(hodnota_karty_banker) == 1:
                    print(f"| +---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")


                elif index == (len(hodnota_karty_banker) - 1):
                    print(f"+---+","|".rjust(delka_oddelovace - 6 * len(barva_karty_banker)), end=" ")

                else:
                    print("+---+", end=" ")

            print(sep="\n")


        def banker_footer():
            print(oddelovac)
            # print(f"| Bankéřovo skóré: /".ljust(0), f"Bank: {bank} |".rjust(delka_oddelovace-14-len(str(skore_banker))-len(str(bank))))
            print(f"| Bankéřovo skóré: {skore_banker_none}".ljust(0), f"Bank: {bank} BTCo |".rjust(delka_oddelovace - 18 - len(str(skore_banker_none))))
            print(oddelovac)


        def banker_footer_videt():
            print(oddelovac)
            print(f"| Bankéřovo skóré: {skore_banker}".ljust(0), f"Bank: {bank} BTCo |".rjust(delka_oddelovace - 18 - len(str(skore_banker))))
            print(oddelovac)


        def vyhodnoceni(skore_hrac, skore_banker, prohrano):
            if skore_hrac > 21:
                print(
                    f" Prohrál jsi {prohrano}.",
                    f" Jsi přes 21, tvoje skóre je {skore_hrac}.",
                    sep="\n")  
            
            elif skore_banker >= skore_hrac:
                print(
                    f" Prohrál jsi {prohrano}.",
                    f" Bankéřovo skóré je {skore_banker} a tvoje {skore_hrac}.",
                    sep="\n")
            
            elif skore_banker <= skore_hrac:
                print(
                    f" GRATULUJI! Vyhráváš {prohrano}.",
                    f" Bankéřovo skóré je {skore_banker} a tvoje {skore_hrac}.",
                    sep="\n")


        while True:

            suma_karet += 1

            # prní a následující karty pro hráče
            karta = choice(range(0, 32))
            
            # zajištujě jedinečnost karty
            while karta in rozdane_karty:
                karta = choice(range(0, 32))

            rozdane_karty.append(karta)
            hodnota_karty_hrac.append(karty[karta][0])
            barva_karty_hrac.append(karty[karta][1])
            vaha_karty_hrac.append(vaha_karet[karta])
            skore_hrac += vaha_karet[karta]

            # print(rozdane_karty)
            # print(hodnota_karty_hrac)
            # print(barva_karty_hrac)
            # print(vaha_karty_hrac)
            
            # eso a eso = oko bere 21
            if suma_karet == 2:
                # print("2. kolo")
                if sum (vaha_karty_hrac) == 22:
                    skore_hrac -= 1
            # print(skore_hrac)

            # při překročení skore nebo rovnosti automaticky ukončit
            if skore_hrac >= 21:
                break
            
            # print(rozdane_karty)
            # print(hodnota_karty_hrac)
            # print(barva_karty_hrac)
            # print(vaha_karty_hrac)

            # první karta bankéře
            if prvni_karta_banker == 0:
                prvni_karta_banker += 1
                karta = choice(range(0, 32))

                # zajištujě jedinečnost karty
                while karta in rozdane_karty:
                    karta = choice(range(0, 32))

                rozdane_karty.append(karta)
                hodnota_karty_banker.append(karty[karta][0])
                barva_karty_banker.append(karty[karta][1])
                vaha_karty_banker.append(vaha_karet[karta])
                skore_banker += vaha_karet[karta]

            # print(rozdane_karty)
            # print(hodnota_karty_banker)
            # print(barva_karty_banker)
            # print(vaha_karty_banker)
            
            system(command)
            uvitani()
            stav_hry()
            hrac()
            vykresli_karty_hrace(hodnota_karty_hrac, barva_karty_hrac)
            banker_uvodni_karta()
            banker_footer()

            def uvod_hry ():
                system(command)
                uvitani()
                stav_hry()
                hrac()
                vykresli_karty_hrace(hodnota_karty_hrac, barva_karty_hrac)
                banker_uvodni_karta()
                banker_footer()

            if suma_karet == 1:
                print("- zadej sázku a dostaneš další kartu")
                sazka = input("-> ")

                # overeni sazky
                while True:
                    if sazka.isnumeric():
                        sazka = int(sazka)
                        if minimalni_sazka <= sazka <= hracovo_konto and sazka <= bank and (sazka + vsazeno) <= bank:
                            break
                        else:
                            uvod_hry ()
                            print("- zadej sázku a dostaneš další kartu")
                            print(" Sázka musí být větší nebo rovna minimální sázce,\n nesmí být větší než prostředky hráče a nesmí být\n vsazeno více než je  bank...")
                            sazka = input("-> ")
                    else:
                        uvod_hry ()
                        print("- zadej sázku a dostaneš další kartu")
                        print(" Sázka musí být číslo...")
                        sazka = input("-> ")
                
                vsazeno += sazka
                hracovo_konto -= sazka

            if suma_karet != 1:

                print(
                    f"- navyš sázku zadáním hodnoty a dostaneš další kartu",
                    f"- pro další kartu zadej [d]",
                    f"- pro vyložení karet zadej [v]",
                    sep="\n"
                    )

                sazka = input("-> ")
                while True:
                    if sazka.isnumeric():
                        sazka = int(sazka)
                        if minimalni_sazka <= sazka <= hracovo_konto and sazka <= bank and (sazka + vsazeno) <= bank:
                            vsazeno += sazka
                            hracovo_konto -= sazka
                            break
                        else:
                            uvod_hry ()
                            print(
                                f"- navyš sázku zadáním hodnoty a dostaneš další kartu",
                                f"- pro další kartu zadej [d]",
                                f"- pro vyložení karet zadej [v]",
                                sep="\n"
                                )
                            print(" Sázka musí být větší nebo rovna minimální sázce,\n nesmí být větší než prostředky hráče a nesmí být\n vsazeno více než je  bank...")
                            sazka = input("-> ")
                    
                    elif sazka == "d" or sazka == "v":
                        break

                    else:
                        uvod_hry ()
                        print(
                            f"- navyš sázku zadáním hodnoty a dostaneš další kartu",
                            f"- pro další kartu zadej [d]",
                            f"- pro vyložení karet zadej [v]",
                            sep="\n"
                            )
                        print(" Zadal jsi neplatný znak. Zkuz to znovu...")
                        sazka = input("-> ")
                
            if sazka == "v":
                break

        # hra bankéře = bere si kary do komžiku kdy je přes nebo roven 21, případně kartu vrátí a vyloží karty
        while skore_banker <= 21:

            karta = choice(range(0, 32))

            # zajištujě jedinečnost karty
            while karta in rozdane_karty:
                karta = choice(range(0, 32))

            rozdane_karty.append(karta)
            hodnota_karty_banker.append(karty[karta][0])
            barva_karty_banker.append(karty[karta][1])
            vaha_karty_banker.append(vaha_karet[karta])

            # osetření výskytu dvou es tzv. oko bere 21
            if vaha_karty_banker[0] == 11 and vaha_karty_banker[1] == 11:
                vaha_karty_banker[1] = 10
            skore_banker += vaha_karty_banker[-1]
            
        # print(rozdane_karty)
        # print(hodnota_karty_banker)
        # print(barva_karty_banker)
        # print(vaha_karty_banker)

        skore_banker -= vaha_karty_banker[-1]
        rozdane_karty.pop()
        hodnota_karty_banker.pop()
        barva_karty_banker.pop()
        vaha_karty_banker.pop()

        # print(skore_banker)
        # print(rozdane_karty)
        # print(hodnota_karty_banker)
        # print(barva_karty_banker)
        # print(vaha_karty_banker)
        
        # propsání do zobrazovacích lišt
        if skore_hrac > 21:
            bank += vsazeno
            status = "PROHRA..."

        elif skore_banker >= skore_hrac:
            bank += vsazeno
            status = "PROHRA..."

        elif skore_banker < skore_hrac:
            hracovo_konto += vsazeno * 2
            bank -= vsazeno
            status = "! VÝHRA !"

        prohrano_vyhrano = vsazeno
        vsazeno = 0

        # když je prázdné konto
        if hracovo_konto < minimalni_sazka:
            status = "! GAME OVER !"

        if bank == 0:
            status = "!!! ABSOLUTNÍ VÝHRA !!!"
           
        # konečné zobrazení 
        system(command)
        uvitani()
        stav_hry()
        hrac()
        vykresli_karty_hrace(hodnota_karty_hrac, barva_karty_hrac)
        vykresli_karty_bankere(hodnota_karty_banker, barva_karty_banker)
        banker_footer_videt()
        vyhodnoceni(skore_hrac, skore_banker, prohrano_vyhrano)


        def rozcesti_hry():
            system(command)
            uvitani()
            stav_hry()
            hrac()
            vykresli_karty_hrace(hodnota_karty_hrac, barva_karty_hrac)
            vykresli_karty_bankere(hodnota_karty_banker, barva_karty_banker)
            banker_footer_videt()
            vyhodnoceni(skore_hrac, skore_banker, prohrano_vyhrano)

        if status == "! GAME OVER !":
            print(f"- pro návrat do menu zadej [z]")
            hra = input("-> ")
            while hra != "z":
                rozcesti_hry()
                print(
                    f"- pro návrat do menu zadej [z]",
                    f"- zadal jsi neplatnou hodnotu...",
                    sep="\n")
                hra = input("-> ")
            if hra == "z":
                break

        elif status == "PROHRA...":
            print(
                f"- pro pokračování ve hře zadej [p]",
                f"- pro návrat do menu zadej [z]",
                sep="\n"
                )
            hra = input("-> ")
            if hra == "p":
                continue
            elif hra =="z":
                break
            else:
                while True:
                    rozcesti_hry()
                    print(
                    f"- pro pokračování ve hře zadej [p]",
                    f"- pro návrat do menu zadej [z]",
                    f"- zadal jsi neplatnou hodnotu...",
                    sep="\n"
                    )
                    hra = input("-> ")
                    if hra == "p":
                        break
                    elif hra =="z":
                        break
            
        elif status == "! VÝHRA !":
            print(
                    f"- pro pokračování ve hře zadej [p]",
                    f"- pro návrat do menu zadej [z]",
                    sep="\n"
                    )
            hra = input("-> ")
            if hra == "p":
                continue
            elif hra =="z":
                break
            else:
                while True:
                    rozcesti_hry()
                    print(
                    f"- pro pokračování ve hře zadej [p]",
                    f"- pro návrat do menu zadej [z]",
                    f"- zadal jsi neplatnou hodnotu...",
                    sep="\n"
                    )
                    hra = input("-> ")
                    if hra == "p":
                        break
                    elif hra =="z":
                        break

        elif status == "!!! ABSOLUTNÍ VÝHRA !!!":

            # uložení do slovníku rekordů
            if jmeno_hrace in rekordy and kolo < int(rekordy.get(jmeno_hrace)):
                rekordy.update({jmeno_hrace: kolo})
                j = json.dumps(rekordy)
                
                with open("rekordy", 'w') as f:
                    f.write(j)
                    f.close()

            elif jmeno_hrace not in rekordy:
                rekordy.update({jmeno_hrace: kolo})

                j = json.dumps(rekordy)
                with open("rekordy", 'w') as f:
                    f.write(j)
                    f.close()

            print(
                    f"- pro zobrazení tabulky s rekordy [t]",
                    f"- pro návrat do menu zadej [z]",
                    sep="\n"
                    )
            hra = input("-> ")
            if hra == "t":
                break
            elif hra =="z":
                break
            else:
                while True:
                    rozcesti_hry()
                    print(
                    f"- pro zobrazení tabulky s výsledky [t]",
                    f"- pro návrat do menu zadej [z]",
                    f"- zadal jsi neplatnou hodnotu...",
                    sep="\n"
                    )
                    hra = input("-> ")
                    if hra == "t":
                        break
                    elif hra =="z":
                        break
                 
        if hra == "z":
            break

    if hra == "t":
        system(command)
        serazeni_a_tisk_tabulky()
        print(f"- pro návrat do menu zadej [z]")
        hra = input("-> ")
        while hra != "z":
            system(command)
            serazeni_a_tisk_tabulky()
            print(f"- pro návrat do menu zadej [z]")
            print(f"- zadal jsi neplatnou hodnotu...")
            hra = input("-> ") 






