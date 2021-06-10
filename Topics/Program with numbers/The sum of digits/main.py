# put your python code here
three_digit_integer = int(input())
a = three_digit_integer // 100
b = (three_digit_integer - (a * 100)) // 10
c = three_digit_integer % 10
print(a + b + c)