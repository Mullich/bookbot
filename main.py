def main(): 
    with open("books/frankenstein.txt") as pth:
        file_contents = pth.read()
    print(file_contents)
    
main()