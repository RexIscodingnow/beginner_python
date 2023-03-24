import os, base64

img_dir = os.path.join("D:/", '3c0b305ce5f42b027649f2cb4c22700a--zero-emilia.jpg')

with open(img_dir, mode='rb') as file:
    file = file.read()

    file = base64.b64encode(file).decode('ascii')
    # print(file)