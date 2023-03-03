num = int(input("Please enter the Francois number: "))
assert num > 0, "the number must be greater than 0"

index = 2
num_list = [2, 1]

while index < num:
    new_num = num_list[index-2] + num_list[index-1]
    num_list.append(new_num)
    index += 1
    
print(num_list[-1])
