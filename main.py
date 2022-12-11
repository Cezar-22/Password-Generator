import random
password = ""
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "&", "?", "@", "*", "$", "%", "#"]
n1 = characters[random.randint(1, 69)]
n2 = characters[random.randint(1, 69)]
n3 = characters[random.randint(1, 69)]
n4 = characters[random.randint(1, 69)]
n5 = characters[random.randint(1, 69)]
n6 = characters[random.randint(1, 69)]
n7 = characters[random.randint(1, 69)]
n8 = characters[random.randint(1, 69)]
n9 = characters[random.randint(1, 69)]
n10 =characters[random.randint(1, 69)]
password = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
print(password)