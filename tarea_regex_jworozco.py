import re
import sys

def process_file(input_file_path):
    # Define the output file name based on the input file name
    output_file_path = input_file_path.replace('.txt', '_modified.txt')

    # Regular expression to match the date and time format
    date_time_pattern = r"(\d{4})\.(\d{2})\.(\d{2})\.(\d{2})\.(\d{2})\.(\d{2})"
    # Replacement pattern using backslashes for date and colons for time
    date_time_replacement = r"\1\\\2\\\3 \4:\5:\6"

    # Regular expression to match "Gate NG45Y" with a space and remove it
    gate_pattern = r"Gate NG45Y"
    gate_replacement = "GateNG45Y"

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Substitute the date and time pattern in the line
            modified_line = re.sub(date_time_pattern, date_time_replacement, line)
            # Substitute the gate pattern in the line
            modified_line = re.sub(gate_pattern, gate_replacement, modified_line)
            # Replace newlines with a comma
            modified_line = modified_line.strip() + ","
            # Write the modified line to the output file
            output_file.write(modified_line)
        # Remove the last comma added in the file
        output_file.seek(0, 2)  # Move the cursor to the end of the file
        output_file.seek(output_file.tell() - 1, 0)  # Move back by one position
        output_file.truncate()  # Remove the last character (comma)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tarea_regex_jworozco.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)
        print(f"Processed file saved as: {input_file_path.replace('.txt', '_modified.txt')}")