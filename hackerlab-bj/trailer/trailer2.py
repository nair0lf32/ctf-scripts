#!/usr/bin/python3

def swap_bytes_in_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
        fixed_data = bytearray()
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                fixed_data.append(data[i + 1])
            fixed_data.append(data[i])
        with open(output_file, 'wb') as f:
            f.write(fixed_data)

input_file = 'output-data'
output_file = 'fixed_image.jpg'
swap_bytes_in_file(input_file, output_file)
print("Done")
