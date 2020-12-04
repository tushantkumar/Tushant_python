def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open('wordLineCount.txt', 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

if __name__ == '__main__':
    countWords('wordLineCount.txt')
   