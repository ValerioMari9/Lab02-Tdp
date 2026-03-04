import string
class Dictionary:

    def __init__(self):
        self.dizionario = dict()

    def addWord(self, word: tuple[str, str]):
        if word[0] in self.dizionario:
            if word[1] not in self.dizionario[word[0]]:
                self.dizionario[word[0]].append(word[1])
        else:
            self.dizionario[word[0]]=[word[1].replace("\n", "")]


    def translate(self, word:str):
        if word in self.dizionario:
            return self.dizionario[word]
        else:
            return None

    def translateWordWildCard(self, word:str):
        l=[]
        alf=list(string.ascii_lowercase)
        for i in alf:
            a=self.translate(word.replace("?", i))
            if a!=None:
                l.append(a)
        if len(l)==0:
            return None
        else:
            return l