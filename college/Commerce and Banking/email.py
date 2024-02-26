import csv
import re

output_file = 'college.csv'
email_output_file = 'Commerce&Banking_Emails.csv'

# Read the output_file CSV file and extract the email addresses from the "Email" column
emails = []
with open(output_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['Email']
        if email:
            # Use regular expression to match and extract email addresses
            email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
            if email_matches:
                emails.extend(email_matches)

# Save the extracted email addresses in a separate CSV file with a single column
with open(email_output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Email'])  # Write the header row
    for email in emails:
        writer.writerow([email])  # Write each email in a separate row under the "Email" column
