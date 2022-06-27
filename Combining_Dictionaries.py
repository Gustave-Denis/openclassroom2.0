dict_a = {'name': 'Amos'}
dict_b = {'age': 100}

def dictionary_masher(dict_a, dict_b):
    mash = {**dict_a, **dict_b}
    return mash


# Test your function using the code below
if __name__ == '__main__':
    print(dictionary_masher({"name": "Amos"}, {"age": 100}))