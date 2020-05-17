import difflib as df
import json as j

data = j.load(open("data.json"))


def translate(word):
    if word.lower() in data:
        return data[word]
    elif len(df.get_close_matches(word, data.keys(), n=5, cutoff=0.7)):
        x = df.get_close_matches(word, data.keys(), n=5, cutoff=0.7)
        y = ""
        for i in x:
            y = y + " -- " + i + " -- "
        choice = input(
            "Do you mean to find the meaning if the follwing words" + y + "Then type Yes or No\nYes\\No --> ")
        if choice.lower() == "yes":
            newWord = input("Enter the word again --> ")
            return translate(newWord)
        elif choice.lower() == "no":
            newWords = input("Reenter the word --> ")
            return translate(newWords)
        else:
            return "We can't understand "

    else:
        return "\"" + word + "\" Has no meaning in the dictionary"


word = input("Enter the word to find its meaning --> ")
output = translate(word)
if type(output) == list:
    print("Meaning of the word is " + " ==>")
    for i in output:
        print(" " * len("Meaning of the word is ") + "-->" + i + "\n")
else:
    print(output)
