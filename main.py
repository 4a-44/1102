f = open("three_digit_numbers.txt")
three_digit_numbers = f.read()

cols = three_digit_numbers.split()
num_list = []
for col in cols:
    num =int(col)
    num_list.append(num)

start = min(num_list)
end = max(num_list)
for count in range(start, end):
    if count in num_list:
        pass
    else:
        print(f"{count} is missing")
#done bbg
