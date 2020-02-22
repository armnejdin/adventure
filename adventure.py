import time


#terminal start
def start():
    for x in range(23):
        print("")
    print("Hej välkommen, vad heter du?")
    namn = input()
    if namn == "q":
        return
    print("Hej "+ namn + "!")
    time.sleep(2)

    print("Vill du på äventyr???")
    time.sleep(0.5)

    beslut = input("ja/nej:  ").lower()

    if beslut == "ja":
        print("Är du säker?")
        time.sleep(0.2)
        print("ja/nej:  ")
        time.sleep(1)
        print("Skämta för sent ändå")
        import adventure_screen
    elif beslut == "nej":
        print("Ah, okej jag förstår :(")
        time.sleep(3)
    else:
        print("Är du efterbliven?? Kan du inte stava till ja eller nej?")
        time.sleep(2)

        print("Hmm Vi testar igen")
        time.sleep(0.2)
        b_igen = input("ja/nej:  ").lower()

        if b_igen == "ja":
            print("Är du säker?")
            time.sleep(0.2)
            print("ja/nej:  ")
            time.sleep(1)
            print("Skämta för sent ändå")
            import adventure_screen
        elif b_igen == "nej":
            time.sleep(0.5)
            print("Ah, okej jag förstår :(")
            time.sleep(3)
        else:
            time.sleep(0.5)
            list = ["Vet du vad? ", "Nu är jag ", "jävligt ", "trött ", "på ", "dig"]
            for x in range(len(list)):
                print(list[x])
                time.sleep(0.3)
            time.sleep(1)
            print("" +namn+ "!!!!")



start()