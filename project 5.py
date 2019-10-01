#Veronica Stureborg
#Project 5

def main():
    #inputting a sentence
    sentence = input("Please enter a sentence:").lower()

    #number of characters

    characters= len(sentence)
    print ("Number of characters:" , characters)

    #number of words
    words=len(sentence.split())
    print ("Number of words:", words)

    #average word length
    length= float(characters/words)
    print("Average word length:", length)

main()
