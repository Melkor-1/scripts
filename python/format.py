#!/usr/bin/env python3

import re

def convert_single_line_comments(input_file, output_file):
    with open(input_file, 'r') as infile:
        source_code = infile.read()

    # Use regular expression to match // comments and convert them to /* */ comments
    converted_code = re.sub(r'//(.+?)\n', r'/* \1 */\n', source_code)

    with open(output_file, 'w') as outfile:
        outfile.write(converted_code)

if __name__ == '__main__':
    input_file = 'c.c'  # Replace with the path to your C source file
    output_file = 'c.c'  # Replace with the desired output file path
    convert_single_line_comments(input_file, output_file)
