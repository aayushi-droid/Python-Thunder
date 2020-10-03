'''

Problem statement: Write a function that takes a string "a + bi" and returns a tuple (a, b).
Problem Link: https://edabit.com/challenge/oFNJeSzzcTgMwLFy5

'''

def realImaginary(str1):

    arr=str1.split("i")

    strnew=arr[0]

    if(strnew.count("+")==1):       
        resultArr=strnew.split("+")
        result=(int(resultArr[0]),int(resultArr[1]))
        return result
    else:
        if(strnew.index("-")!=0):
            resultArr=strnew.split("-")
            result=(int(resultArr[0]),-int(resultArr[1]))
            return result
        
        else:
            resultArr=strnew.split("-")
            result=(-int(resultArr[1]),-int(resultArr[2]))
            return result
            