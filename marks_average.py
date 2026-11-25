"""Calculate the average of five subject marks and show Pass or Fail.

This beginner-friendly program assumes each mark is from 0 to 100.
"""

NUMBER_OF_SUBJECTS = 5
PASS_MARK = 40

marks = []

for subject_number in range(1, NUMBER_OF_SUBJECTS + 1):
    while True:
        mark_text = input(f"Enter the mark for subject {subject_number} (0-100): ")

        try:
            mark = float(mark_text)
        except ValueError:
            print("Please enter a number, such as 75 or 82.5.")
            continue

        if 0 <= mark <= 100:
            marks.append(mark)
            break

        print("The mark must be between 0 and 100. Please try again.")

average = sum(marks) / NUMBER_OF_SUBJECTS

print(f"Average mark: {average:.2f}")

if average >= PASS_MARK:
    print("Pass")
else:
    print("Fail")
