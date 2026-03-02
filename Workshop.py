# Create a variable named running_total and assign it the value 0.

running_total = 0

# Create a variable named num_of_friends and assign it the value of 4. 
# This will be used later in the workshop to calculate the final split.

num_of_friends = 4

# Create four variables: appetizers set to 37.89, main_courses set to 57.34, desserts set to 39.39, and drinks set to 64.21.

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Update the running_total variable by adding appetizers, main_courses, desserts, and drinks together.
# Finally, use print() to display the string Total bill so far: followed by a space and the value of running_total.
# Note: You might notice that the output has more decimal digits than expected. 
# As you learned in a previous lesson, this happens because numbers are stored in binary, and many decimal values cannot be represented exactly in this format, which leads to rounding errors.

running_total = appetizers + main_courses + desserts + drinks
print(f"Total bill so far: {running_total}")

# Create a variable named tip and assign it the result of multiplying running_total by 0.25.
# Finally, use print() to display the string Tip amount: followed by a space and the value of your tip variable.

tip = running_total * 0.25
print(f"Tip amount: {tip}")

# Use the += operator to add the value of tip to your running_total. 
# Finally, use print() to display the string Total with tip: followed by a space and the value of running_total.

running_total += tip
print(f"Total with tip: {running_total}")

# Create a variable named final_bill and assign it the result of dividing running_total by num_of_friends.
# Finally, use the print() function to display the string Bill per person: followed by a space and the value of final_bill.

final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

# Use the round() function to round final_bill to two decimal places and assign the result to a new variable named each_pays.
# Finally, use print() to display the string Each person pays: followed by a space and your each_pays variable.
# With that, the bill splitter workshop is complete.

each_pays = round(final_bill, 2)
print(f"Each person pays: {each_pays}")