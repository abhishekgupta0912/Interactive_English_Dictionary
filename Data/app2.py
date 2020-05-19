import mysql.connector as ac

con = ac.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database")

cursor = con.cursor()

word = input("Input The Word To find Its Meaning --> ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression= '%s' " % word)

result = cursor.fetchall()

if result:
    print("The Meaning Of The Word -->")
    for i in result:
        print(" " * len("The Meaning Of The Word -->") + "--> " + i[1] + "\n")
else:
    print("There Is No Such Word In The Dictionary")
