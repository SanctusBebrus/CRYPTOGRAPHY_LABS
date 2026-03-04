from string import ascii_lowercase
import os

global FILEPATH


def prostoi(datas, strokis, wm, vm):
    if len(strokis) == len(ascii_lowercase):
        res = ""
        for elem in datas:
            if wm == "1" and elem in ascii_lowercase:
                res += strokis[ascii_lowercase.index(elem)]
            elif wm == "2" and elem in strokis:
                res += ascii_lowercase[strokis.index(elem)]
            else:
                res += elem
        if vm == "1":
            print(res)
        elif vm == "2":
            write_file(res, FILEPATH)

        print("\n!encrypted successfully!") if wm == "1" else print("\n!decrypted successfully!")
    else:
        print(f"key string length must be equal to {len(ascii_lowercase)}\n")
    return


def caesar(datas, strokis, wm, vm):
    res = ""
    for elem in datas:
        if wm == "1" and elem in ascii_lowercase:
            sdvig_id = (ascii_lowercase.index(elem) - int(strokis)) % len(ascii_lowercase)
            res += ascii_lowercase[sdvig_id]
        elif wm == "2" and elem in ascii_lowercase:
            sdvig_id = (ascii_lowercase.index(elem) + int(strokis)) % len(ascii_lowercase)
            res += ascii_lowercase[sdvig_id]
        else:
            res += elem

    if vm == "1":
        print(res)
    elif vm == "2":
        write_file(res, FILEPATH)
    print("\n!encrypted successfully!") if wm == "1" else print("\n!decrypted successfully!")


def afinniy(datas, strokis, wm, vm):
    a, b = strokis
    slovar = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
        "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
        "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
        "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25
    }
    res = ""
    for elem in datas:
        if wm == "1" and elem in ascii_lowercase:
            res += ascii_lowercase[(a * slovar.get(elem) + b) % len(ascii_lowercase)]
        elif wm == "2" and elem in ascii_lowercase:
            a_minus1 = pow(a, -1, len(ascii_lowercase))
            res += ascii_lowercase[a_minus1 * (slovar.get(elem) + len(ascii_lowercase) - b) % len(ascii_lowercase)]
        else:
            res += elem
    if vm == "1":
        print(res)
    elif vm == "2":
        write_file(res, FILEPATH)

    print("\n!encrypted successfully!") if wm == "1" else print("\n!decrypted successfully!")


def vertical(datas, k_rows, k_cols, kkey, wm, vm):
    table = [[""] * k_cols for _ in range(k_rows)]

    # print(table)
    indx_kkey = -1
    for i in range(k_rows):
        for j in range(k_cols):
            indx_kkey += 1
            try:
                table[i][j] = datas[indx_kkey]
            except Exception:
                continue

    #print(table)
    res = ""
    if wm == "1":
        for col in kkey:
            for row in range(k_rows):
                if table[row][int(col)] in ascii_lowercase:
                    res += table[row][int(col)]

    elif wm == "2":
        L = len(datas)
        full_rows = L // k_cols
        r = L % k_cols

        col_len = [full_rows + 1 if i < r else full_rows for i in range(k_cols)]
        #print(col_len)

        idx = 0
        for col_key in kkey:
            col = int(col_key)
            for row in range(col_len[col]):
                if idx < L:
                    table[row][col] = datas[idx]
                    idx += 1

        res = ""
        for row in range(k_rows):
            for col in range(k_cols):
                if table[row][col] != "":
                    res += table[row][col]

    if vm == "1":
        print(res)
    elif vm == "2":
        write_file(res, FILEPATH)

    print("\n!encrypted successfully!") if wm == "1" else print("\n!decrypted successfully!")


def read_file():
    file_path = input("type a file path: for example - C:\\Users\\User\\Desktop\\File.txt\n")
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            datas = file.read().lower()
        return datas
    except Exception:
        print("uuuuuuh... looks like you need another try...")
        return 0


def write_file(datas, path):
    try:
        with open(path, "w", encoding="UTF-8") as file:
            file.write(datas)
            print(f"check your file {path}")
    except Exception:
        print("an error occurred during writing :(")


with open("yacrypt.txt", "r", encoding="UTF-8") as intro:
    print(intro.read())

while True:
    work_mode = input("choose program mode:\n1 - encrypt\n2 - decrypt\n3 - exit\n")
    match work_mode:
        case "1":
            print("encryption mode has been set")
        case "2":
            print("decryption mode has been set")
        case "3":
            print("bye!")
            exit()
        case _:
            print("\nnevermind...")
            continue

    input_mode = input("choose input mode:\n1 - from console\n2 - from file\n3 - exit\n")

    match input_mode:
        case "1":
            data = input("type something\n").lower()
        case "2":
            res = read_file()
            if res == 0:
                continue
            else:
                data = res
        case "3":
            print("bye!")
            exit()
        case _:
            print("\nnevermind...")
            continue
    print("success")
    view_mode = input("choose view mode:\n1 - show in console\n2 - write in file\n")
    match view_mode:
        case "2":
            FILEPATH = input("type a file path: for example - C:\\Users\\User\\Desktop\\File.txt\n\n")
        case "1":
            pass
        case _:
            print("\nnevermind...")
            continue

    mode = input("choose mode:\n1 - Prostoi\n2 - Caesar\n3 - Afinniy\n4 - Vertical\n")

    match mode:
        case "1":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input("type a key\nfor example: QWERTYUIOPASDFGHJKLZXCVBNM\n").lower()
                case "2":
                    key_v = read_file().lower()
                case _:
                    continue
            prostoi(data, key_v, work_mode, view_mode)

        case "2":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input("type an integer key\nfor example: 17\n")
                case "2":
                    key_v = read_file()
                case _:
                    continue
            caesar(data, key_v, work_mode, view_mode)
        case "3":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = tuple(int(x) for x in input("type two integers key\nfor example: 3 4\n").split())
                case "2":
                    key_v = tuple(int(x) for x in read_file().split())
                case _:
                    continue
            afinniy(data, key_v, work_mode, view_mode)
        case "4":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input(
                        "type table size and key\nfor example: 43 120\nwhere\n\t4 - rows\n\t3 - cols\n\t120 - key\n").split()
                case "2":
                    key_v = read_file().split()
                case _:
                    continue
            key_r, key_c = key_v[0]
            key_key = key_v[1]
            vertical(data, int(key_r), int(key_c), key_key, work_mode, view_mode)
        case _:
            print("\nnevermind...")
            continue

