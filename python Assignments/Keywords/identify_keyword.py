import keyword
key_word=input("enter word:")
if keyword.iskeyword(key_word):
    print("word is a python keyword")
else:
    print("word is not a python keyword")