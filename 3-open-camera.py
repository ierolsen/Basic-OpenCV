import cv2

# capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Width: {width}, Height: {height}")

# record
writer = cv2.VideoWriter("recording.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True:
    
    ret, frame = cap.read()
    cv2.imshow("video")
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(0) & 0xFF == ord(c): break
    
cap.release()
writer.release()
cv2.destroyAllWindows()