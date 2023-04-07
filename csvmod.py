import csv

# specify the input and output file paths
input_file = 'input.csv'
output_file = 'output.csv'

# specify the column index that needs to be converted
column_index = 5

# read the input CSV file
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        # skip the header row
        if reader.line_num == 1:
            data.append(row)
            continue
        else:
            # convert the date format to american format
            row[column_index] = row[column_index].split("/")[1] + "/" + row[column_index].split("/")[0] + "/" + row[column_index].split("/")[2]
            data.append(row)

# write the modified data into a new CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)