'''
    Probem Task : War of Numbers #235
    Problem Link : https://edabit.com/challenge/Aofd78q72sAtgCyEY
'''


def war_of_numbers(num_list):
    even_list = []
    odd_list = []
    for num in num_list:
        if num % 2 == 0: even_list.append(num)
        else: odd_list.append(num)
    if sum(even_list) > sum(odd_list): max_sum = sum(even_list)
    else: max_sum = sum(odd_list)
    return max_sum

max_sum = war_of_numbers([1,3,4,5,6])
print(max_sum)