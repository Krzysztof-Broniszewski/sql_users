import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# cursor.execute("create table users (Birth integer, Name text, City text , Function text)")

users = [
    (1980, "Krzysztof Broniszewski", "Kraków", "Administrator"),
    (1979, "Agnieszka Pietrzyk", "Kraków", "Użytkownik"),
    (2006, "Nikola Broniszewska", "Kraków", "Użytkownik"),
    (1956, "Barbara Broniszewska", "Muszyna", "Uczeń"),
    (2011, "Tiger", "Kraków", "Kot"),
    (2019, "Lucyfer", "Kraków", "Kot"),
]

cursor.executemany("insert into users values (?,?,?,?)", users)

#print specific values
print("*****************************************************************")
cursor.execute("select * from users where Function=:c", {"c": "Kot"})
search_by_cities = cursor.fetchall()
for row in search_by_cities:
    print(row)

cursor.execute("create table new_function (Function text, New_function text)")

cursor.execute("insert into new_function values (?, ?)", ("Kot", "Animal"))
cursor.execute("select * from new_function where Function=:c", {"c": "Kot"})
new_function_animal = cursor.fetchall()
print(new_function_animal)

cursor.execute("insert into new_function values (?, ?)", ("Użytkownik", "User"))
cursor.execute("select * from new_function where Function=:c", {"c": "Użytkownik"})
new_function_user = cursor.fetchall()
print(new_function_user)

# manipulate database
print("*****************************************************************")
for i in new_function_animal:
    new_animal = [new_function_animal[0][1] if value==new_function_animal[0][0] else value for value in i]
    print(new_animal)


# print database rows
for row in cursor.execute("select * from users"):
    print(row)

# for user in users:
#     print(user)

connection.close()