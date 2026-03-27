import os

if __name__ == '__main__':

    letter_path = os.path.join(os.getcwd(),"my_letter.txt")

    with open(letter_path, 'w', encoding='utf=8') as f:
        f.write('To my Friend\n')
        f.write('Hello\n')
        f.write('Bye\n')


    with open(letter_path, 'a', encoding='utf-8') as f:
        f.write("Blah...blah...\n")
        f.write("Blah...blah...\n")
        f.write("Blah...blah...\n")





    print('my_letter.txt file written text complete')