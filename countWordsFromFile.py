def countWordsFromFile():
    fileName = input('Enter your file name: ')
    numberOfWords = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print('number of words from '+ fileName + ' are: ')
    print(numberOfWords)
countWordsFromFile()
