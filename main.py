"""
Full Name: Safal R Regmi
Class-Section: IS 250-01
Assignment Title: PyCharm and GitHub Setup Activity
Submission Date: 11 - 17 - 2025
"""
"""
Write your pseudocode here.
Step 1: Asking the user to enter the first score
Step 2: Asking the user to enter the second score
Step 3: Asking the user to enter the third score
Step 4: Calculating the score average using a function 
Step 5: Add the 3 scores together
Step 6: Divide the sum by 3 to get the average 
Step 7: Returning the average 
Step 8: Print or we can say display each score
Step 9: Print or display the average score

Do not write any Python code in this section.
Your pseudocode should describe your overall approach in your own words.
"""
# Your Python code begins below this line.


# Define a function to calculate average of three scores
def find_average(score1, score2, score3):
    # Add the three scores together
     total = score1 + score2 + score3
    # Divide by 3 to get the average
     avg = total/3
     # Return the result
     return avg

# Ask the first score from the user
first = float(input("Enter the first score: "))
# Ask the second score from the user
second = float(input("Enter the second score: "))
# Ask the third score from the user
third = float(input("Enter the third score: "))

# Call the function to calculate the average
result = find_average (first, second, third)

# Display the scores
print("First score: ", first)
print("Second score: ", second)
print("Third score: ", third)

#Display the average
print("The average score is: ", result)










  
