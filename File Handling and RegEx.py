"""
LABORATORY EXERCISE 2
"""

import re

# Create an empty list to store selected lines from the CSV file
members = []

with open("BSCPE1-5.csv", 'r') as file:
    # Iterate over each line in the file, keeping track of line numbers
    for i, line in enumerate(file, start=1):
        # If the current line number is 11, 18, or 37, store the line in 'members' list
        if i in {11, 18, 37}:
            members.append(line)
        if i == 37:  # Stop reading after line 37 (since it's the last one we need)
            break

# Extract surnames from specific lines
surnames = []
for member in members:
    details = member.split(',')
    if len(details) > 1:
        surnames.append(details[1].strip().capitalize())  # Capitalize the surname properly

# Generate the output filename using extracted surnames
surname_placeholder = "_".join(surnames)
output_filename = f"output_{surname_placeholder}.txt"

# Open a new file in write mode to store extracted data
with open(output_filename, 'w') as file:
    # Loop through each selected member's details
    for member in members:
        details = member.split(',')

        # Extract surname, middle initial, and first name manually
        surname = details[1].strip().capitalize()
        middle_initial = details[3].strip().capitalize()[0]
        first_name = details[2].strip().title()

        # Format full name
        whole_name = f"{surname} {middle_initial}. {first_name}"

        # Extract student number and email address
        student_number = details[0].strip()
        email_address = details[6].strip()

        # Write the formatted details to the output file
        file.write(f"Full name: {whole_name}\n")
        file.write(f"Student number: {student_number}\n")
        file.write(f"Email address: {email_address}\n\n")

# Open another file named "cool_man.txt" in read mode and append its contents
with open("cool_man.txt", 'r') as file:
    lines = file.readlines()

with open(output_filename, 'a') as file:
    for line in lines:
        file.write(line)  # Append each line from "cool_man.txt" to the output file

'''
####################################################
#################  BONUS POINTS  ###################
####################################################
'''

pattern = r',S\w+O,J\w+O'
matched_lines = []

with open("BSCPE1-5.csv", 'r') as file:
    for i, line in enumerate(file, start=1):
        if re.search(pattern, line):  # Check if the line matches the pattern
            matched_lines.append((i, line.strip()))  # Store line number and data

with open(output_filename, 'a') as file:
    file.write("\n--- RESULTS ---\n")
    if matched_lines:
        for line_num, data in matched_lines:
            file.write(f"Line {line_num}: {data}\n")
    else:
        file.write("No matching data found. \n")

print(f"Output file saved as {output_filename}")