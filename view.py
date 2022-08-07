import cv2
path = r'movie/steamA.mp4'
path2 = r'movie/nc84025.mp4'
path3 = r'movie/xpfire_CD.mp4'
path4 = r'movie/nc274684.mp4'
path5 = r'movie/skr2203c_b.mp4'

C = [path5,path,path2,path3,path4]
sentence = ['Peace','Fire...?','Fire!!','Fire!Fire!Fire!','Good luck...']

for i in range(5):
    PATH = C[i]
    cap = cv2.VideoCapture(PATH)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame , (1920,1080))
            cv2.putText(frame,sentence[i], (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5, cv2.LINE_AA)
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        #    if not ret:
        #     cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
        #     continue

        else:
            break

    cap.release()
cv2.destroyAllWindows()
