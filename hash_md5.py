import hashlib


def main():
    digester = hashlib.md5()
    with open('文件路径', 'rb') as file_stream:
        data = file_stream.read(1024)  # 每次只读1024个字节，防止文件过大一次性读入
        while data:
            digester.update(data)  # 要转成二进制码才能进行MD5
            data = file_stream.read(1024)
    print(digester.hexdigest())


if __name__ == '__main__':
    main()
