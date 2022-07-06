from WikiCrawler import crawl
import Constants
import argparse
import Constants
# import sys

class CommandLine:
    def __init__(self):
        self.Parser = argparse.ArgumentParser(
            description='This is a web crawler which will visit a URL and return the top number of words (by frequency).')
        self.Parser.add_argument('-mf', metavar='--most-frequent-number-of-words', type=int, default=Constants.getDefaultNumberOfWordsToReturn,
                                 help='the most frequent number of words to be returned.')
        self.Parser.add_argument(
            '-ew', '--excluded-words', nargs='+', default=[], help="the words to be excluded within the count.")
        self.Parser.add_argument(
            '-url', '--url', type=str, default=Constants.getDefaultUrl(), help="the url to the page to be crawled.")
        self.Args = self.Parser.parse_args()



# try: 
#     numberOfWordsToReturn = int(sys.argv[1])
#     url = sys.argv[2]
#     excludedWords = list(sys.argv[3])
#     l = len(excludedWords)
#     print(excludedWords[1][1:l-1].split("''"))
#     result = crawl(
#         url=url,
#         numberOfWordsToReturn=numberOfWordsToReturn,
#         excludedWords=excludedWords
#     )

    # print(result)

try:
    cmdLine = CommandLine()

    numberOfWordsToReturn = cmdLine.Args.mf if cmdLine.Args.mf > 0 else CrawlConstants.getDefaultNumberOfWordsToReturn()
    excludedWords = cmdLine.Args.excluded_words
    # print(excludedWords)
    url = cmdLine.Args.url

    result = crawl(
        url=url,
        numberOfWordsToReturn=numberOfWordsToReturn,
        excludedWords=excludedWords
    )

    print(result)


except Exception as e:
    raise e



