import csv

input_file = 'Arts_data.csv'
output_file = 'college2.csv'
encoding = 'utf-8'  # Replace with the appropriate encoding of your CSV file

# Read the CSV file
with open(input_file, 'r', encoding=encoding) as file:
    reader = csv.reader(file)
    header = next(reader)  # Extract the header row

    # Find the row with all column headers
    try:
        while not all(col_header in header for col_header in ['College Name', 'Contact no', 'Email', 'Website', 'Address']):
            header += next(reader)  # Concatenate the next row if headers are split
    except StopIteration:
        print("Column headers not found in the CSV file.")
        exit(1)

    # Write the header row to the output file
    with open(output_file, 'w', newline='', encoding=encoding) as output:
        writer = csv.writer(output)
        writer.writerow(header)

        last_row = []  # Initialize last_row as an empty list

        # Continue processing the data rows and write to the output file
        for row in reader:
            if len(row) > 0 and row[0] != '':  # Skip empty rows
                if len(row) < len(header):  # Handle multiple rows in a single row
                    last_row = row
                    continue
                elif len(row) > len(header):
                    row = last_row + row[len(header):]
                    last_row = []

                cleaned_row = [cell.strip() if '\n' not in cell else cell.replace('\n', ' ') for cell in row]
                # Replace newline character with a space in multi-line cells

                writer.writerow(cleaned_row)
