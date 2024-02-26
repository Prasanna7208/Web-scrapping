import csv

output_file = 'college_data1.csv'
email_output_file = 'Emails_Columnwise.csv'

# Read the output_file CSV file and check for email addresses in each row
email_addresses = []
with open(output_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        for cell in row:
            if '@' in cell:
                email_addresses.append(cell)

# Save the email addresses in another CSV file in column-wise format
with open(email_output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Email Addresses'])  # Write the header row
    writer.writerows(zip(email_addresses))  # Write the data rows in column-wise format
