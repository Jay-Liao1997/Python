# #编码
# msg  = '编码与解码'

# encode_msg = msg.encode('utf-8')  #默认就是utf-8
# print(encode_msg)

# #解码
# msg = b'\xe7\xbc\x96\xe7\xa0\x81\xe4\xb8\x8e\xe8\xa7\xa3\xe7\xa0\x81'
# decode_msg = msg.decode()   ##默认就是utf-8
# print(decode_msg)


tplt = "{0:^10}\t{1:^10}\t{2:^10}"
    print(tplt.format("学校名称", "位置", "分数"))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2]))

tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("学校名称", "位置", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288))