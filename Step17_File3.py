import os

if __name__ == "__main__":
    letter_path = os.path.join(os.getcwd(),"my_letter.txt")

    with open(letter_path, 'r', encoding='utf-8') as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline().strip())
        print(f.readline().strip())
        print(f.readline().strip())
    
    print('-----------')

    with open(letter_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
    
