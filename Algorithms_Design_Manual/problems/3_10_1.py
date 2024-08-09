def parenthesis(s):
    hashmap = {"(": ")",
               "{": "}",
               "[": "]"}
    
    
    stack = []
    for i in range(len(s)):
        if s[i] in hashmap:
            stack.append(hashmap[s[i]])
        elif len(stack) == 0 or s[i] != stack.pop():
            return f"Error: {i}"
    return "fine" if len(stack) == 0 else "ugh"


print(parenthesis("(({[]}))"))
print(parenthesis("(({[]})"))