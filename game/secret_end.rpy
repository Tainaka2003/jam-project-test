# init python:
#     def safeProgress(X):
#         if os.path.exists("progress.p"):
#             f = open("progress.p","r")
#             a=f.read(1)
#             b=f.read(1)
#             c=f.read(1)
#             d=f.read(1)
#         else:
#             f = open("progress.p","w")
#             f.write("0000")
#             a="0"
#             b="0"
#             c="0"
#             d="0"
#             f.close()
#         f = open("progress.p","w")
#         if X=="1":
#             f.write("1"+b+c+d)
#         if X=="2":
#             f.write(a+"1"+c+d)
#         if X=="3":
#             f.write(a+b+"1"+d)
#         if X=="4":
#             f.write(a+b+c+"1")
#         f.close()
#
#     def readProgress():
#         if os.path.exists("progress.p"):
#             f = open("progress.p","r")
#             return f.read(4)
#             f.close()
# $safeProgress("1") #рут пройден
# $safeProgress("2") #рут пройден
# $safeProgress("3") #рут пройден
# $safeProgress("4") #рут пройден
# if readProgress() == "1111" #считывает прогресс, если все единички - открывает секретный рут
