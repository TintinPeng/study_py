import cv2
import sys

str = "/home/tintin/Workspaces/VSCode/python/"
if __name__ == "__main__":
    img = cv2.imread(str+"pictures/grapedisease/1/image1.JPG")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
