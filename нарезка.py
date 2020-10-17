import cv2
vidcap = cv2.VideoCapture(r'C:\Users\Admin\Downloads\trot1test.mp4')
count = 0
success = True
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 10000))
  success, image = vidcap.read()
  if (success):
    cv2.imwrite(r"C:\Users\Admin\Pictures\frame\trot1test%d.jpg" % count, image)
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1



