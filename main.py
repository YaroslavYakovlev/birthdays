def read_base():
    birthday_base_file = open("birthday_base.txt", "r", encoding="UTF-8")
    tmp_list_base = birthday_base_file.read()
    print(tmp_list_base)

    print(tmp_list_base[1])

        # tmp_list_base = birthday_base_file.read()


read_base()
