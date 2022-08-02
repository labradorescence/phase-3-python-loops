#!/usr/bin/env python3

def happy_new_year():
    # code goes here

    # while loop
    # i = 10
    # while i > 0:
    #     print(i)
    #     i -= 1
    # print("Happy New Year!")

    # for loop
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here
    square = [num * num for num in int_list]
    print(square)
    return square
    pass

# def test():
#     nums = [1,2,3,4,5]

    # new_nums = list()
    # for each_num in nums:
    #     each_new_num = each_num + 8
    #     new_nums.append(each_new_num)
    # print(new_nums)

#     # new_nums = [ each_num + 8 for each_num in nums]
#     # print(new_nums)
# test()


def fizzbuzz():
    # code goes here
    for i in range(1, 101):
        if i % 15 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
           i = "Buzz"
        print(i)
    pass