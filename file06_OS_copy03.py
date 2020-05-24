# 升级版复制函数：无论源文件下有什么，复制就完事了
import os

path_original = r'C:\测试'
path_target = r'E:\test'


def copy(path_original, path_target):
    '''
    :param path_original: 源文件路径
    :param path_target: 目标文件路径
    :return: None
    '''
    if not os.path.exists(path_target):  # 检查目标文件是否存在，如果不存在，就创建
        os.mkdir(path_target)
    if os.path.isdir(path_original):  # 检查传进来的源文件路径是否是一个目录
        list_name = os.listdir(path_original)  # 列出源文件目录下的所有文件，以列表方式存储
        for name in list_name:  # 遍历文件列表
            if os.path.isdir(os.path.join(path_original, name)):  # 将源文件路径与文件名组合起来，判断一下是具体的路径还是目录，如果还是目录，说明源文件下面还套着一个文件夹
                path_target_next = os.path.join(path_target, name)  # 组合起来成为目标路径下的一个文件夹
                # path_target_next = os.mkdir(os.path.join(path_target, name))  #这样子path_target_next得到的值为None，根本不是路径，就会造成后面传参出现报错
                # 因为mkdir没有返回值，所以用变量去接也没有用
                copy(os.path.join(path_original, name), path_target_next)  # 递归调用copy函数
            else:  # 如果不是目录，而是具体的文件，就可以进行复制的操作
                with open(os.path.join(path_original, name), 'rb') as rstream:
                    container = rstream.read()
                    with open(os.path.join(path_target, name), 'wb') as wstream:
                        wstream.write(container)
        else:
            print("复制完成！")

#调用函数
copy(path_original, path_target)
