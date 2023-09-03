def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,'r',encoding='UTF-8')
    except Exception as e:
        print(f"异常{e}")
    else:
        print(f.read())
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f = open(file_name,'a',encoding='UTF-8')
    f.write(data)
    f.close()

if __name__ == '__main__':
    print_file_info('E:/PyCharmProjects/word.txt')
    append_to_file('E:/PyCharmProjects/word.txt','哈哈哈哈哈')
    print_file_info('E:/PyCharmProjects/word.txt')
