import os   


if __name__ == '__main__':
    print(os.getcwd())
    print(os.sep)

    r'''
        current memo.txt shimshin@Shims-Macbook_Pro Junhan_infra_python_master
    '''

    path:str = os.path.join(os.getcwd(), 'memo.txt')

    print(path)

    with open(path, 'r', encoding='utf-8') as f:

        result = f.read()
        print('--- memo.txt File Contents')
        print(result)