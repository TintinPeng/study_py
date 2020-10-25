import cv2
import sys

str = "/home/tintin/Workspaces/VSCode/python/"
if __name__ == "__main__":
    img = cv2.imread(str+"pictures/grapedisease/1/image1.JPG")
    # cv2.imshow("Image", img)

    print(img.shape)  # 打印图像的高，宽，通道数（返回一个3元素的tuple）
    height = img.shape[0]  # 将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]
    print("height:%s,width:%s,channels:%s" % (height, width, channels))
    print(img.size)  # 打印图像数组内总的元素数目（总数=高X宽X通道数）

    cv2.waitKey(0)
    cv2.destroyAllWindows()
