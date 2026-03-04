import translator as tr
t = tr.Translator()
t.loadDictionary("dictionary.txt")
txtIn = 0       # Add input control here!
while txtIn !=4:
    t.printMenu()
    txtIn=input()
    while not txtIn.isdigit():
        txtIn = input()
    txtIn = int(txtIn)
    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        p = input()
        if " " in p:
            p2 = p.split(" ")
            if p2[0].isalpha():
                for i in range(1, len(p2)):
                    if p2[i].isalpha():
                        t.handleAdd((p2[0], p2[i]))
                print("Aggiunta!")
            else:
                print("Errore!")
        else:
            print("Errore")
    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        p = input()
        trad=t.handleTranslate(p)
        if trad is None:
            print("Parola non trovata")
        else:
            print(trad)
    if int(txtIn) == 3:
        print("Ok, quale wildCard devo cercare?")
        p=input()
        if "?" in p:
            trad=t.handleWildCard(p)
            if trad is None:
                print("Wildcard non trovata")
            else:
                print(trad)
    if int(txtIn) == 4:
        print("Uscita dal traduttore")
        exit()
