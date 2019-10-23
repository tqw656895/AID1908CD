# f = open('dict.txt', "r")
# a = input("输入单词:")
# while True:
#     date = f.readlines(1)
#     if (date[0].split("  "))[0] > a:
#         print("无单词")
#         break
#     if a == (date[0].split("  "))[0]:
#         print(date[0].split("  ")[-1])
#         break
#
# f.close()
# x = {"0", 1, 3, 4, 8}
# max(len(x))

# def mk():
#     a = input("输入文件名:")
#     b = input("输入w或者wb:")
#     c = input("输入路径或者使用默认路径:")
#     if c == "":
#         c = '/home/tarena/桌面/%s'
#     open(c % (a), b)
# mk()
filename = input("File:")
try:
    fr = open(filename, "rb")
except FileNotFoundError as e:
    print(e)
else:
    file = filename.split("/")[-1]
    fw = open("/home/tarena/" + file, "wb")
    while True:
        date = fr.read(1024)
        if not date:
            break
        fw.write(date)
fr.close()
fw.close()
