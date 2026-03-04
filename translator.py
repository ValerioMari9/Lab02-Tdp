from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dizionario = None

    def printMenu(self):
        print("-----------------------------------")
        print(f"    Translator Alien-Italian")
        print("-----------------------------------")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        self.dizionario = Dictionary()
        f=open(dict,"r")
        righe=f.readlines()
        for r in righe:
            r=r.split(" ")
            self.dizionario.addWord((r[0].lower(),r[1].lower()))
        # dict is a string with the filename of the dictionary


    def handleAdd(self, entry):
        self.dizionario.addWord(entry)# entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query: str):
        return self.dizionario.translate(query.lower())# query is a string <parola_aliena>

    def handleWildCard(self, query):
        return self.dizionario.translateWordWildCard(query.lower())
        # query is a string with a ? --> <par?la_aliena>
