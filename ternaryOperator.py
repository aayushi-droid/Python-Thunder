'''
Problem Task : Write a function as minimalist as possible that returns the strings :

1. "both" if both given booleans a and b are true.
2. "first" if only a is true.
3. "second" if only b is true .
4. "neither" if both a and b are false.

Problem Link : https://edabit.com/challenge/j3aeuun5WDXFsTYAK
'''
Solution : 

 const areTrue=(a,b)=>a?(b?'both':'first'):(b?'second':'neither');

                         (or)
        
const areTrue = (a, b) => ["neither", "first", "second", "both"][a + b * 2];
