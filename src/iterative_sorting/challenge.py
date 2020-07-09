# Add up and print the sum of the all of the minimum elements of each inner array:
sum_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

##
adder = 0
for sub_arr in sum_arr:
    min_num = sub_arr[0]
    for j in sub_arr:
        if j < min_num:
            min_num = j
    adder += min_num
print(adder)
