def main(): 
    with open("books/frankenstein.txt") as pth:
        file_contents = pth.read()
    print(file_contents)

def wordcount(str):
    words = str.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(word_count)
    return(word_count)

with open("books/frankenstein.txt") as pth:
    file_contents = pth.read()
    wordcount(file_contents)