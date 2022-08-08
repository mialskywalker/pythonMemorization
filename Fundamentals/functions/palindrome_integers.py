def palindrome(nums_list):

    numbers = nums_list.split(', ')

    for el in numbers:
        if el == el[::-1]:
            print("True")
        else:
            print("False")


palindrome(input())
