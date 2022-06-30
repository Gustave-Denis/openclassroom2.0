def package_enumerator(string):
    for i in dir(string):
        print (i)

if __name__ == '__main__':
    import string
    package_enumerator(string)
