long_list = list(range(1000000))
file_name = "my_file.txt"
opened_file = open(file_name, 'w')
for _item in long_list:
    # complete the next string to write item to my_file.txt
    command = "print(_item, file=opened_file, flush=True)"
opened_file.close()
