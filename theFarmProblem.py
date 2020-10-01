# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals
# https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT


def legs(chickens, cows, pigs):
    # adding the amount of chicken legs to a new variable for the total amount of legs.
    totalLegs = (chickens*2)
    
    # doing the same for cows 
    totalLegs = totalLegs + (cows*4)

    # lastly i do it for pigs.
    totalLegs = totalLegs + (pigs*4)

    return(totalLegs)

print(legs(2, 3, 5))
