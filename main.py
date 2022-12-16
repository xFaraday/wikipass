import re
import os
import pyfiglet
import wikipedia
from pick import pick

class WordList:
    def __init__(self, RootNode):
        self.RootNode = RootNode
        self.links = []
        self.counter = 0
        self.wordcounter = 0

    def AddWordlist(self, wordlist):
        if os.path.exists("wordlist.txt"):
            #open file in append mode for wordlist.txt
            with open("wordlist.txt", "a") as f:
                for word in wordlist:
                    f.write(word+"\n")
                    self.wordcounter += 1
                f.close()
        else:
            #create file in write mode for wordlist.txt
            file = open("wordlist.txt", "w")
            for word in wordlist:
                file.write(word+"\n")
                self.wordcounter += 1
            file.close()

    def AddLink(self, link):
        self.links.append(link)

    def IncrementCounter(self):
        self.counter += 1

def banner():
    ascii_banner = pyfiglet.figlet_format("Wikipass")
    print(ascii_banner)

def NormalizeText(text):
    pattern = r"\s+"
    words = re.split(pattern, text)
    setofwords = set(words)
    if os.path.exists("wordlist.txt"):
        with open("wordlist.txt", "r") as f:
            for line in f:
                unique_items = setofwords.symmetric_difference(line)
                unique_items = list(unique_items)
                setofwords = set(unique_items)
            f.close()
        return unique_items
    else:
        return words

def GetWikiPediaSearch():
    searchterm = str(input("Enter search term: "))

    results = wikipedia.search(searchterm)

    title = 'Please choose root Wikipedia Node: '
    options = []
    # print the search results
    for result in results:
        options.append(result)

    option, index = pick(options, title, indicator='=>', default_index=0)
    return option

def GetWikiPediaData(wordlistObj):
    for link in wordlistObj.links:
        try:
            page = wikipedia.page(link)
            try:
                page_links = page.links
                #remove link from list
                wordlistObj.links.remove(link)
                for link in page_links:
                    wordlistObj.AddLink(link)
                wordlistObj.IncrementCounter()
                text = NormalizeText(page.content)
                wordlistObj.AddWordlist(text)
                PrintStatus(wordlistObj)
            except KeyboardInterrupt:
                exit(1)
            except:
                wordlistObj.links.remove(link)
                wordlistObj.IncrementCounter()
                text = NormalizeText(page.content)
                wordlistObj.AddWordlist(text)
                PrintStatus(wordlistObj)
        except KeyboardInterrupt:
            exit(1)
        except:
            wordlistObj.links.remove(link)
            pass

def PrintStatus(wordlistObj):
    print("Root Node: " + wordlistObj.RootNode)
    print("Total Links: " + str(len(wordlistObj.links)))
    print("Total Pages Indexed: " + str(wordlistObj.counter))
    #get the size of the wordlist file
    print("Total Words in WordList: " + str(wordlistObj.wordcounter))
    print("Size of Wordlist: " + str(os.path.getsize("wordlist.txt")) + " K")

if __name__ == '__main__':
    wikipedia.set_lang("en")
    banner()
    rootNode = GetWikiPediaSearch()
    print(rootNode)
    
    page = wikipedia.page(rootNode)
    
    wordlistObj = WordList(page.title)
    try:
        page_links = page.links
        for link in page_links:
            wordlistObj.AddLink(link)
        wordlistObj.IncrementCounter()
        text = NormalizeText(page.content)
        wordlistObj.AddWordlist(text)
        PrintStatus(wordlistObj)
    except:
        print("Error, Please Select different Root Node: " + rootNode)
        pass
    
    while True:
        GetWikiPediaData(wordlistObj)