#Today I learned...

birthYear = int(input("Which year were you born?"))
if  birthYear <= 1946:
  print("You're a Traditionalist dude.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Wssup, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! The age of tech!")
elif birthYear >= 1996:
  print("Hey, Gen Z! Your just like me!")
else: 
  print("Try again!")
