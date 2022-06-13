from random import random, randrange
def rozdej():
    def nahodny_balicek():
        #makes and shuffles the card deck
        import random
        hodnota = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        barva = ['♥', '♦', '♠', '♣']
        balicek = []
        for y in range(len(barva)):
            for x in range(len(hodnota)):
                karta = hodnota[x], barva[y] 
                balicek.append(karta)
        random.shuffle(balicek)
        nahodny_balicek.variable = balicek


    def rozdej_hracum():
        #deals cards to players and sets the number of players at the table
        balicek = nahodny_balicek.variable
        global pocet_hracu
        while True:
            pocet_hracu = int(input("Zadej počet hráčů: "))
            if pocet_hracu > 9 or pocet_hracu < 2:
                print("To nejde, můžou být minimálně 2 hráči a maximálně 9")
            else:
                global hrac
                hrac = dict()
                global x
                for x in range(pocet_hracu):
                    karta1 = balicek.pop(randrange(len(balicek)))
                    karta2 = balicek.pop(randrange(len(balicek)))
                    hrac[x] = [karta1, karta2]
                    print("Hráč", x + 1, "má", hrac[x])
                    rozdej_hracum.variable = hrac[x]
                break


    def rozdej_dealer():
        #deals cards to the dealer and asks you how many cards you want to be dealed
        balicek = nahodny_balicek.variable
        global dealer
        odpoved = "ano"
        dealer = []
        pocet = 3
        kolo = 0
        
        while odpoved == "ano":
            odpoved = input("Chceš hrát dál? ")
            if odpoved == "ano":
                for x in range(pocet):
                    dealer.append(balicek.pop(randrange(len(balicek))))
                    pocet = 1
                print("dealer má", dealer)
            kolo = kolo + 1
            if kolo == 3:
                break
            

    nahodny_balicek()
    rozdej_hracum()
    rozdej_dealer()
rozdej()
