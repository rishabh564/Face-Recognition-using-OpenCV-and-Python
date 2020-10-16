import cv2
import os

#  projectPath variable is the absolute path of the directory where this file resides
projectPath = os.path.dirname(os.path.abspath(__file__))
faceClassifier = cv2.CascadeClassifier(projectPath+'/haarcascade_frontalface_default.xml')

count = 0                  # it is used to count the no of frames
size = 50                  # offset is used for fixed size of images which are captured

name = input('enter your id')
camera = cv2.VideoCapture(0)

while True: