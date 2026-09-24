sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total_marks / 500) * 100

print(f"\n--- Results ---")
print(f"Total Marks Obtained: {total_marks:.2f} / 500.00")
print(f"Percentage: {percentage:.2f}%")
