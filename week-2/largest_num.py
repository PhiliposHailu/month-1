# a program to find the largest number in a list.
def largestNum(given_list):
    largest = given_list[0]
    for num in given_list:
        if num > largest:
            largest = num
    
    return largest