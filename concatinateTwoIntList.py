'''
Problem statement: Concatenating Two Integer Lists
Problem Link: https://edabit.com/challenge/cCWMeiJCP9Ef8XMq8
'''
def concat_list(num_list1,num_list2):
    for i in num_list2 :
        num_list1.append(i)       //append () is used to add every element of second list to first one 
    return num_list1
n_list1=[1,2,3,4,5]
n_list2=[6,7,8,9,10]

print("Concated List is \n")
print(concat_list(n_list1,n_list2))
