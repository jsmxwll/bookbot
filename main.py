path = "./books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()
    words = file_contents.split()
    #print(len(words))
    
    letters = {}

    for c in file_contents.lower():
        if c.isalpha():
            letters[c] = letters.get(c,0) + 1

    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    ### begin report printing ###

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in document\n")
    
    for l in sorted_letters:
        print(f"The '{l[0]}' character was found {l[1]} times")
