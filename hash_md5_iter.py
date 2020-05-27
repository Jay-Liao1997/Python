def main():
    digester = hashlib.md5()
    with open('文件路径', 'rb') as file_stream:
        file_iter = iter(lambda:file_stream.read(1024),b'')# lambda 表达式的意思是：每次读1024字节，当为空字节时结束，b''--->空字节
        for data in file_iter:
        	digester.update(data)
    print(digester.hexdigest())


if __name__ == '__main__':
    main()
