from bs4 import BeautifulSoup, NavigableString, Tag
from collections import Counter
# from CrawlExceptions import InvalidCrawlParameters, CrawlError
import requests
import Constants
from typing import Dict, List, Set



class InvalidCrawlParameters(Exception):
    def __init__(self):
        pass


class CrawlError(Exception):
    def __init__(self):
        pass

def process_words(words: List[str], excludedWordList: List[str], numberOfWordsToReturn):

    wordList = words
    processedWords = []
    excludeThis = excludedWordList
    # print(excludeThis)
    # processedWords = [x for x in wordList]
    split_it = wordList.split()
    processedWords = [x for x in split_it if x not in excludeThis]
    # print(split_it)

    # Pass the split_it list to instance of Counter class.
    # Logic to handle excluded words
    # for items in split_it:
    #     if split_it[items] not in excludedWordList:
    #         processedWords.append(split_it[items])
    #     else:
    #         processedWords.append(split_it[items])

    Counters_found = Counter(processedWords)
    # Counters_found = Counter(split_it)

    #print(Counters)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = Counters_found.most_common(numberOfWordsToReturn)
    
   
    return most_occur

   
# This function accepts the parameters: Url, Excluded Words, and the number of words to return in the result.
def crawl(url: str,numberOfWordsToReturn: int,excludedWords: Set = None,localPath: str = None) -> Dict:
   
   # region Validation
    if url != None and len(url) > 0:
        if not(url.startswith('https://')):
            raise InvalidCrawlParameters('Invalid URL.')
    elif localPath == None:
        raise InvalidCrawlParameters('Invalid URL.')

    if excludedWords != None:
        for word in excludedWords:
            if not isinstance(word, str):
                raise InvalidCrawlParameters('Invalid list of excluded words.')

    if numberOfWordsToReturn == None:
        numberOfWordsToReturn = Constants.getDefaultNumberOfWordsToReturn()

    if numberOfWordsToReturn < 0:
        raise InvalidCrawlParameters('Invalid number of words to return.')
    # endregion

    try:
        historyText = []
        # get the source code of the url
        source = None
        if localPath != None:
            source = open(localPath, encoding="utf8")
        else:
            source = requests.get(url).text

        # create the b.s. object
        if localPath != None:
            soupObj = BeautifulSoup(source.read(), 'html.parser')
            historySection = soupObj.find_all('h2')
            for items in historySection:
                print(items.get_text())
                # print(historySection[1])
        else:
            soupObj = BeautifulSoup(source, 'html.parser')
            historySection = soupObj.find(id='History')

            for items in historySection.parent.nextSiblingGenerator():
                if items.name == "h2":
                    break
                if hasattr(items, "text"):
                    historyText.append(items.text)
            resultsHistory = "".join(historyText)
            # print("".join(historyText))
            # print((resultsHistory[1]))
            # split_it = resultsHistory.split()

            # Pass the split_it list to instance of Counter class.
            # Counters_found = Counter(split_it)
            #print(Counters)

            # most_common() produces k frequently encountered
            # input values and their respective counts.
            # most_occur = Counters_found.most_common(10)
            # print(most_occur)

           

        # get all of the words
        # test22 = ["The"]
        words = process_words(resultsHistory, excludedWords, numberOfWordsToReturn)

        return words 
        # count the occurence of the words
        # counts = Counter(words)

        # return the top most common words
        # return counts.most_common(numberOfWordsToReturn)

    except Exception as e:
        # notify system of unhandled error
        raise CrawlError(e)
