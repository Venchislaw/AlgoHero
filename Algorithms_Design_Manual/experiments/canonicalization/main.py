from collections import defaultdict

# canonicalization code for finding all words containing passed letters
hashmap = defaultdict(list)

with open("words.txt") as f:
    for word in f.readlines():
        hashmap["".join(sorted(word.lower().rstrip("\n")))].append(word.lower().rstrip("\n"))
    

def find_all_words_containing_chars(charslist: list):
    charslist = [char.lower() for char in charslist]
    return hashmap["".join(sorted(charslist))]


# ['akel', 'alek', 'elka', 'kale', 'kela', 'lake', 'leak']
print(find_all_words_containing_chars(["A", "e", "k", "l"]))
