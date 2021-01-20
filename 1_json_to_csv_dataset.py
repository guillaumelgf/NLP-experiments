import json

src_file_name = 'News_Category_Dataset_v2.json'
dst_file_name = 'News_Category_Dataset.csv'

with open(src_file_name, 'r') as r_file, open(dst_file_name, 'w') as w_file:
    line = r_file.readline()
    headline = ','.join(json.loads(line).keys()) + '\n'
    w_file.write(headline)
    
line_nbr = 0
max_line = 200000

def process_line(line, nbr):
    line = json.loads(line)
    line = list(line.values())
    line = ['"' + x.replace('"', '""') + '"' for x in line]
    line = ','.join(line)
    line = f'{line}\n'
    return line

with open(src_file_name, 'r') as r_file, open(dst_file_name, 'a', encoding="utf-8") as w_file:
    line = r_file.readline()
    
    while line:
        line = process_line(line, line_nbr)
        w_file.write(line)
        line_nbr += 1
        line = r_file.readline()
        
        print(f'{line_nbr}/200000', end='\r')