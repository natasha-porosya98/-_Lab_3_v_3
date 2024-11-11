def only_num(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int):
            result.append(item)
    return result
def input_list():
    user_list = input("Введіть список, розділяючи комами: ")
    input_items = user_list.split(",")
    proccesed_list = []
    for item in input_items:
        item = item.strip()
        try:
            proccesed_list.append(int(item))
        except:
            pass
    return proccesed_list
user_list = input_list()
filtered_list = only_num(user_list)
print(f"Відфільтрований список: {filtered_list}")