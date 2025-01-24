def main(): 
    path = "books/frankenstein.txt"
    book_text = get_text(path)
    num_words = word_count(book_text)
    charactercount = character_count(book_text)
    sortedletterlist = letters_only(charactercount)

    print(f"--- Begin report of {path}---")
    print(F"{num_words} words found in the document")
    print()
    for letter_dict in sortedletterlist:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['occurrence']} times")
    print()
    print("--- End report ---")

def word_count(str):
    words = str.split()
    return len(words)

def get_text(path):
    with open(path) as pth:
        return pth.read()

def character_count(str):
    characters = {}
    characters_list = []
    for character in str:
        lwr = character.lower()
        if lwr not in characters:
            characters[lwr] = 1
        else:
            characters[lwr] += 1
    return characters

def letters_only(chardict):
    charlist = []
    for key, value in chardict.items():
        if key.isalpha():
            temp_dict = {"letter": key, "occurrence": value}
            charlist.append(temp_dict)
    charlist.sort(reverse=True, key=sort_it)
    return charlist

def sort_it(list):
    return list["occurrence"]

main()


