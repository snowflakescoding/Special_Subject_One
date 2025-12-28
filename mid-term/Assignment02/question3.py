import json

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
    
    def feedFromFile(self, filename: str) -> None:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.feed(line)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def createJSONFile(self, filename: str) -> None:
        sortedItems = sorted(
            self.authorDict.items(),
            key=lambda x: (-x[1], x[0])
        )

        sortedDict = {author: count for author, count in sortedItems}
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(sortedDict, file, indent=0)
        except Exception as e:
            print(f"Error writing JSON file: {e}")

def main():
    aset = AuthorSet("the silmarillion by tolkien in 1977")
    aset.feedFromFile("sample.txt")
    aset.createJSONFile("sample.json")

if __name__ == '__main__':
    main()