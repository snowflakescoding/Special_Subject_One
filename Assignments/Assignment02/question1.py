class AuthorSet:
    def __init__(self, sentence: str) -> None:
        self.authorDict = {}
        self.process_sentence(sentence)
    
    def process_sentence(self, sentence: str) -> None:
        parts = sentence.split(" by ")
        if len(parts) >= 2:
            authorPart = parts[1]
            authorName = authorPart.split(" in ")[0].strip()

            if authorName in self.authorDict:
                self.authorDict[authorName] += 1
            else:
                self.authorDict[authorName] = 1
    
    def feed(self, sentence: str) -> None:
        self.process_sentence(sentence)
    
    def countForAuthor(self, name: str) -> int:
        return self.authorDict.get(name, 0)

def main():
    aset = AuthorSet("harry potter by rowling in 1997")
    aset.feed("the casual vacancy by rowling in 2012")
    aset.feed("the hobbit by tolkien in 1937")
    
    print(aset.countForAuthor("rowling"))  # 2
    print(aset.countForAuthor("tolkien"))  # 1
    print(aset.countForAuthor("asimov"))   # 0

if __name__ == '__main__':
    main()