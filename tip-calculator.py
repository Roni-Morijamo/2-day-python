print("Welcome to the tip calculator!")
bill = float(input("How much is your order bill?\n$"))
people = int(input("How many people do you want to split the bill between?\n"))
tips = int(input("What percentage of tip do you want to leave? 10, 12, 15\n"))

tips_as_precent = tips / 100
total_tip_amount = bill * tips_as_precent
total_bill = bill + total_tip_amount
bill_per_persone = (total_bill / people)
final_amount = round(bill_per_persone, 2)

print(f"From each person ${final_amount:.2f}.")
