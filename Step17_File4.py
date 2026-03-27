import os

'''
if __name__ == '__main__':
    file_path=os.path.join(os.getcwd(), 'config.txt')

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in f:
            print(line)
'''

if __name__ == '__main__':
    updated_lines=[]

    pattern=r'^SELINUX=[a-zA-Z]+'

    file_path=os.path.join(os.getcwd(), 'config.txt')

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if re.match(pattern, line):
                result=re.sub(pattern, "SELINUX=disabled", line)
                updated_lines.append(result)
            else:
                updated_lines.append(line)
    
    print(updated_lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)
    
print('Made the config.txt')

