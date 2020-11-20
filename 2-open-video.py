import cv2
import time

video_path = "data/MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(video_path)

print(f"Width: {cap.get(3)}, Height: {cap.get(4)}")

if cap.isOpened() == False:
    print("Video is not opened")

while True:
    
    # read video
    ret, frame = cap.read()

    if ret == True:

        time.sleep(0.01) # this is used for make slow video

        cv2.imshow("video",frame)
        
    else: break
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release() # stop capture
cv2.destroyAllWindows()