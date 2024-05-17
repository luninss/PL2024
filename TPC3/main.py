import re
import sys

def parse_and_process(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    pattern = r'\bon\b|\d+|off|='
    tokens = re.findall(pattern, content, flags=re.IGNORECASE)

    is_active = False
    sum_total = 0
    results = []

    for token in tokens:
        token_lower = token.lower()
        if token_lower == 'on':
            is_active = True
        elif token_lower == 'off':
            is_active = False
        elif token.isdigit() and is_active:
            sum_total += int(token)
        elif token == '=':
            results.append(f'Soma: {sum_total}')

    with open(output_file, 'w') as file:
        file.write('\n'.join(results) + '\n')

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    input_filepath = sys.argv[1]
    output_filepath = "out.txt"

    parse_and_process(input_filepath, output_filepath)

if __name__ == "__main__":
    main()
