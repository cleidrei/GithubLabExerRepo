import random

def getWords(filename):
    return tuple(line.strip().upper() for line in open(filename) if line.strip())

articles = getWords("generator-articles.txt")
nouns = getWords("generator-nouns.txt")
verbs = getWords("generator-verbs.txt")
prepositions = getWords("generator-prepositions.txt")

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def sentence():
    return nounPhrase() + " " + verbPhrase()

def main():
    number = int(input("Enter number of sentences: "))
    for _ in range(number):
        print(sentence())
      
main()
