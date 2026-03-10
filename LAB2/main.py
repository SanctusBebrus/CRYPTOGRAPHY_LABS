import random

global FILEPATH


def gamma_onebit(data, key, work_mode, view_mode):
    key_bytes = key.encode("utf-8")

    if work_mode == "1":
        data_bytes = data.encode("utf-8")
        encrypted = bytearray()
        for i in range(len(data_bytes)):
            encrypted.append(data_bytes[i] ^ key_bytes[0])

        if view_mode == "1":
            print(f"\n!encrypted successfully!\n{encrypted.hex()}")
        else:
            result = encrypted.hex()
            write_file(result, FILEPATH)
            print("\n!encrypted successfully!")

    elif work_mode == "2":
        try:
            data = data.strip().replace(' ', '').lower()
            data_bytes = bytes.fromhex(data)
            print(f"\n!decoded to hex!\n{data_bytes}")
        except Exception:
            print("\n*dies from cringe*\n")
            return
        decrypted = bytearray()
        for i in range(len(data_bytes)):
            decrypted.append(data_bytes[i] ^ key_bytes[0])
        try:
            result = decrypted.decode("utf-8")
            if view_mode == "1":
                print(f"!decrypted successfully!\n{result}")
            else:
                write_file(result, FILEPATH)
                print("\n!decrypted successfully!")
        except Exception:
            print("\n*dies from cringe*\n")
            return


def gamma_repeat(data, key, work_mode, view_mode):
    key_bytes = key.encode("utf-8")

    if work_mode == "1":
        data_bytes = data.encode("utf-8")
        encrypted = bytearray()
        for i in range(len(data_bytes)):
            encrypted.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])

        if view_mode == "1":
            print(f"\n!encrypted successfully!\n{encrypted.hex()}")
        else:
            result = encrypted.hex()
            write_file(result, FILEPATH)
            print("\n!encrypted successfully!")

    elif work_mode == "2":
        try:
            data = data.strip().replace(' ', '').lower()
            data_bytes = bytes.fromhex(data)
            print(f"\n!decoded to hex!\n{data_bytes}")
        except Exception:
            print("\n*dies from cringe*\n")
            return
        decrypted = bytearray()
        for i in range(len(data_bytes)):
            decrypted.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])
        try:
            result = decrypted.decode("utf-8")
            if view_mode == "1":
                print(f"!decrypted successfully!\n{result}")
            else:
                write_file(result, FILEPATH)
                print("\n!decrypted successfully!")
        except Exception:
            print("\n*dies from cringe*\n")
            return


def gamma_random(data, key, work_mode, view_mode):
    random.seed(int(key))
    gamma_key = str(random.random()).split(".")[-1].encode("utf-8")

    if work_mode == "1":
        data_bytes = data.encode("utf-8")
        encrypted = bytearray()
        for i in range(len(data_bytes)):
            encrypted.append(data_bytes[i] ^ gamma_key[i % len(gamma_key)])

        if view_mode == "1":
            print(f"\n!encrypted successfully!\n{encrypted.hex()}")
        else:
            result = encrypted.hex()
            write_file(result, FILEPATH)
            print("\n!encrypted successfully!")

    elif work_mode == "2":
        try:
            data = data.strip().replace(' ', '').lower()
            data_bytes = bytes.fromhex(data)
            print(f"\n!decoded to hex!\n{data_bytes}")
        except Exception:
            print("\n*dies from cringe*\n")
            return
        decrypted = bytearray()
        for i in range(len(data_bytes)):
            decrypted.append(data_bytes[i] ^ gamma_key[i % len(gamma_key)])
        try:
            result = decrypted.decode("utf-8")
            if view_mode == "1":
                print(f"!decrypted successfully!\n{result}")
            else:
                write_file(result, FILEPATH)
                print("\n!decrypted successfully!")
        except Exception:
            print("\n*dies from cringe*\n")
            return


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
            if work_mode == "1":
                data = input("type something\n").lower()
            else:
                data = input("type hex string to decrypt: for example - 190a140a16110004\n").lower()
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
            FILEPATH = input("type a file path: for example - C:\\Users\\User\\Desktop\\File.txt\n")
        case "1":
            pass
        case _:
            print("\nnevermind...")
            continue

    mode = input("choose mode:\n1 - Gamma with 1 bit key\n2 - Gamma with key repeating\n3 - Gamma with Random\n")

    match mode:
        case "1":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input("type a key\nfor example: a\n").lower()
                case "2":
                    key_v = read_file()
                    if key_v == 0:
                        continue
                case _:
                    continue

            # Вызываем функцию с правильными параметрами
            gamma_onebit(data, key_v, work_mode, view_mode)

        case "2":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input("type a key\nfor example: key\n")
                case "2":
                    key_v = read_file()
                    if key_v == 0:
                        continue
                case _:
                    continue
            gamma_repeat(data, key_v, work_mode, view_mode)

        case "3":
            key_mode = input("choose key input mode:\n1 - from console\n2 - from file\n")
            match key_mode:
                case "1":
                    key_v = input("type an integer sequence\nfor example: 35174\n")
                case "2":
                    key_v = read_file()
                    if key_v == 0:
                        continue
                case _:
                    continue
            gamma_repeat(data, key_v, work_mode, view_mode)

        case _:
            print("\nnevermind...")
            continue
