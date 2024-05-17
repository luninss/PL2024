import re
import sys

def convert_headers(line):
    for i in range(6, 0, -1):
        line = re.sub(r'^{0} (.+)$'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), line)
    return line

def convert_bold(line):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)

def convert_italic(line):
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', line)

def convert_ordered_list(lines):
    html_lines = []
    in_list = False
    for line in lines:
        if re.match(r'^\d+\. ', line):
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            item = re.sub(r'^\d+\. (.+)', r'<li>\1</li>', line)
            html_lines.append(item)
        else:
            if in_list:
                html_lines.append('</ol>')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ol>')
    return html_lines

def convert_link(line):
    return re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

def convert_image(line):
    return re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', line)

def markdown_to_html(markdown):
    lines = markdown.split('\n')
    html_lines = []
    
    for line in lines:
        line = convert_headers(line)
        line = convert_bold(line)
        line = convert_italic(line)
        line = convert_link(line)
        line = convert_image(line)
        html_lines.append(line)
    
    html_lines = convert_ordered_list(html_lines)
    
    return '\n'.join(html_lines)

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    html_output = markdown_to_html(markdown_text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        input_file = sys.argv[1]
        output_file = "out.html"
        main(input_file, output_file)