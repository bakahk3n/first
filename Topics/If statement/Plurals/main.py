number = int(input())
word = input()

# write a condition for plurals

if number != 1:
    word += "s"
    if number == 1:
        pass
print(number, word)
