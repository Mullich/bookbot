def main(): 
    path = "books/frankenstein.txt"
    book_text = get_text(path)
    character_count = charactercount(book_text)
    print(character_count)

def wordcount(str):
    words = str.split()
    return len(words)

def get_text(path):
    with open(path) as pth:
        return pth.read()

def charactercount(str):
    characters = {}
    for character in str:
        lwr = character.lower()
        characters[lwr] += 1
    return characters

main()