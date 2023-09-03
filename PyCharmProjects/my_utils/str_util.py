def str_reverse(s):
    return s[::-1]

def substr(s,x,y):
    return s[x:y]
if __name__ == '__main__':
    print(str_reverse('abcd'))
    print(substr('abcd',1,2))