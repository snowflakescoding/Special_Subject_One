class AuthorSet:
    def __init__(self, sentence: str) -> None:
        self.authorDict = {}
        self.bookToAuthor = {}  
        self.process_sentence(sentence)
    
    def process_sentence(self, sentence: str) -> None:
        parts = sentence.split(" by ")
        if len(parts) >= 2:
            bookTitle = parts[0].strip()
            authorPart = parts[1]
            authorName = authorPart.split(" in ")[0].strip()

            self.bookToAuthor[bookTitle] = authorName

            if authorName in self.authorDict:
                self.authorDict[authorName] += 1
            else:
                self.authorDict[authorName] = 1
    
    def feed(self, sentence: str) -> None:
        self.process_sentence(sentence)
    
    def countForAuthor(self, name: str) -> int:
        return self.authorDict.get(name, 0)
    
    def countForSentence(self, sentence: str) -> int:
        count = 0
        countedAuthors = set()
        
        bookTitles = sentence.split(",")
        
        for bookTitle in bookTitles:
            bookTitle = bookTitle.strip()

            if bookTitle in self.bookToAuthor:
                author = self.bookToAuthor[bookTitle]

                if author not in countedAuthors:
                    count += self.authorDict[author]
                    countedAuthors.add(author)
        
        return count
    
    def mostProductiveAuthor(self) -> str:
        if not self.authorDict:
            return ""
        
        return max(self.authorDict, key=self.authorDict.get)
    
    def topKAuthors(self, k: int) -> list:
        sortedAuthors = sorted(
            self.authorDict.items(),
            key=lambda x: (-x[1], x[0])
        )
        
        return [author for author, _ in sortedAuthors[:k]]

def main():
    aset = AuthorSet("harry potter by rowling in 1997")
    aset.feed("the casual vacancy by rowling in 2012")
    aset.feed("the hobbit by tolkien in 1937")
    aset.feed("the silmarillion by tolkien in 1977")
    aset.feed("foundation by asimov in 1951")
    
    print(aset.countForSentence("harry potter, foundation, the hobbit"))  # 5
    print(aset.mostProductiveAuthor())  # 'rowling' or 'tolkien'
    print(aset.topKAuthors(2))  # ['rowling', 'tolkien']

if __name__ == '__main__':
    main()