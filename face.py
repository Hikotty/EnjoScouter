import cv2

def showana(ana1,height,width,ORG_WINDOW_NAME):
    cap = cv2.VideoCapture(ana1)
    while(True):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame , (width,height))
            cv2.imshow(ORG_WINDOW_NAME, frame)
        else:
            cap.release()
            break

    cap.release()
if __name__ == '__main__':
    # 定数定義
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "Enjoy"

    DEVICE_ID = 0

    path = r'video/skr2203c_b.mp4'
    path2 = r'video/steamA.mp4'
    path3 = r'video/fiem_b.mp4'
    path4 = r'video/xpfire_CD.mp4'
    path5 = r'video/nc84025.mp4'
    C = [path,path2,path3,path4,path5]

    ana1 = r'video/level1_a.mp4'
    ana2 = r'video/level2_a.mp4'
    ana3 = r'video/level3_a.mp4'
    ana4 = r'video/level4_a.mp4'
    ana = [ana1,ana2,ana4,ana4]

    sen = ['Peace','Fire...?','Fire!!','Fire!Fire!Fire!','Good luck...']

    # 分類器の指定
    cascade_file = "xml/haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)

    # 初期フレームの読込
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    # GAUSSIAN_WINDOW_NAME = "gaussian"
    # cv2.namedWindow(GAUSSIAN_WINDOW_NAME)
    P = C[0]
    sentense =sen[0]
    cap2 = cv2.VideoCapture(P)
    # 変換処理ループ

    while end_flag == True:
        #textfile
        f = open('text/aiai.txt', 'r')
        power = f.read()
        print(power)
        f.close()

        if power == '':
            continue
        elif int(power) >= 0 and int(power) <= 25 and P != C[0]:
            P = C[0]
            cap2.release()
            cap2 = cv2.VideoCapture(C[0])
            sentense =sen[0]

        elif int(power) > 25 and int(power) <=50 and P != C[1]:
            P = C[1]
            cap2.release()
            cap2  = cv2.VideoCapture(C[1])
            sentense =sen[1]

        elif int(power) > 50 and int(power) <=75 and P !=C[2]:
            P = C[2]
            cap2.release()
            cap2 = cv2.VideoCapture(C[2])
            sentense =sen[2]

        elif int(power) > 75 and int(power) <=90 and P!=C[3]:
            P = C[3]
            cap2.release()
            showana(ana[3],height,width,ORG_WINDOW_NAME)
            cap2 = cv2.VideoCapture(C[3])
            sentense =sen[3]

        elif int(power) <= 100 and int(power) >90 and P!=C[4]:
            P = C[4]
            cap2.release()
            showana(ana[3],height,width,ORG_WINDOW_NAME)
            cap2 = cv2.VideoCapture(C[4])
            sentense =sen[4]

        # 画像の取得と顔の検出
        img = c_frame
        height, width = img.shape[:2]

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_list = cascade.detectMultiScale(img_gray, minSize=(100, 100))
        #print(face_list)

        #背景動画の読み込み
        ret, frame = cap2.read()
        if not ret:
            cap2.set(cv2.CAP_PROP_POS_FRAMES, 10)
            continue

        frame = cv2.resize(frame , (width,height))
        cv2.putText(frame,sentense, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.putText(frame,power, (width-150,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)

        if len(face_list) == 1:
            x = face_list[0][0]-50
            w = face_list[0][1]+100
            y = face_list[0][2]-50
            h = face_list[0][3]+100
            if x <0 or y <0 or h <0 or w <0:
                cv2.imshow(ORG_WINDOW_NAME, frame)
            else:
                face_img = img[y:h+y,x:x+w]
                height, width = face_img.shape[:2]
                frame[y:y +height ,x:x+width] = face_img

            # フレーム表示
            cv2.imshow(ORG_WINDOW_NAME, frame)

        else:
            cv2.imshow(ORG_WINDOW_NAME, frame)

        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
