import difflib as df

import mysql.connector as ac

con = ac.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database")


def findMeaning(word):
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression= '%s' " % word)
    result = cursor.fetchall()
    if result:
        return result
    else:
        qury2 = cursor.execute("select Expression from Dictionary")
        result = cursor.fetchall()
        listWord = []
        for i in result:
            listWord.append(i[0])
        if len(df.get_close_matches(word, listWord, n=5, cutoff=0.7)) > 0:
            x = df.get_close_matches(word, listWord, n=5, cutoff=0.7)
            y = ""
            for i in x:
                y = y + " -- " + i + " -- "
            choice = input(
                "Do you mean to find the meaning if the follwing words" + y + "Then type Yes or No\nYes\\No --> ")
            if choice.lower() == "yes":
                newWord = input("Enter the word again --> ")
                return findMeaning(newWord)
            elif choice.lower() == "no":
                newWords = input("Reenter the word --> ")
                return findMeaning(newWords)
            else:
                return "We can't understand "


word = input("Enter The Word To Find Its Meaning --> ")
print()
result = findMeaning(word)

if result:
    print("The Meaning Of The Word -->")
    for i in result:
        print(" " * len("The Meaning Of The Word -->") + "--> " + i[1] + "\n")
else:
    print("There Is No Such Word In The Dictionary")
