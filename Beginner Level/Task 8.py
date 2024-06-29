#Task 2 :Calculate the total expenses for each of you and print the results. Determine who spent more money overall and print the result. 
your_expenses = {
    "Hotel": 1300,
    "Food": 500,
    "Transportation": 500,
    "Attractions": 600,
    "Miscellaneous": 300
}
partner_expenses = {
    "Hotel": 1300,
    "Food": 600,
    "Transportation": 500,
    "Attractions": 600,
    "Miscellaneous": 400
}
your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())
print("Your total expenses:", your_total_expenses)
print("Your partner's total expenses:", partner_total_expenses)
if your_total_expenses > partner_total_expenses:
    print("You spent more money overall.")
elif your_total_expenses < partner_total_expenses:
    print("Your partner spent more money overall.")
else:
    print("Both of you spent the same amount of money.")
significant_difference_category = None
significant_difference_amount = 0
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > significant_difference_amount:
        significant_difference_amount = difference
        significant_difference_category = category
if significant_difference_category:
    print("The category with the significant difference in spending is",significant_difference_category,"with a difference of",significant_difference_amount)
else:
    print("There is no significant difference in any category.")