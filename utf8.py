import csv
import sys

def reformat_csv_to_utf8(input_file, output_file):
    """
    Reads a CSV file, converts non-UTF-8 characters to UTF-8, and writes to a new CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        csv.field_size_limit(sys.maxsize)

        with open(input_file, mode='r', encoding='utf-8', errors='replace') as infile, \
             open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                reformatted_row = [cell.encode('utf-8', errors='replace').decode('utf-8') for cell in row]
                writer.writerow(reformatted_row)

        print(f"Reformatted CSV saved to {output_file}")
    except Exception as e:
        print(f"Error processing file: {e}")

input_csv = "" 
output_csv = "" 
reformat_csv_to_utf8(input_csv, output_csv)
