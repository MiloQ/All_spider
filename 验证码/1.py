import tesserocr
from PIL import Image

image = Image.open('code.jpg')
image = image.convert('L') #将图片转化为灰度图像
threshold = 140
table=[]
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')#对图片二值化处理
image.show()

result = tesserocr.image_to_text(image)
print(result)