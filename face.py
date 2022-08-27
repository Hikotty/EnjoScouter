import cv2
import time
import create_table

# database
session = create_table.session
Enjyo = create_table.Enjyo

# 定数定義
ESC_KEY = 27     # Escキー
INTERVAL = 33     # 待ち時間
FRAME_RATE = 30  # fps

ORG_WINDOW_NAME = "Enjoy"
DEVICE_ID = 0

path = r'video/skr2203c_b.mp4'
path2 = r'video/steamA.mp4'
path3 = r'video/fiem_b.mp4'
path4 = r'video/xpfire_CD.mp4'
path5 = r'video/nc84025.mp4'
PATHS = [path, path2, path3, path4, path5]
sen = ['Peace', 'Fire...?', 'Fire!!', 'Fire!Fire!Fire!', 'Good luck...']

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
P = PATHS[0]
sentense = sen[0]
cap2 = cv2.VideoCapture(P)

# 変換処理ループ
while end_flag == True:

    enjyo = session.query(Enjyo).order_by(Enjyo.id.desc()).first()
    pow = str(enjyo.power)

    if pow == '':
        continue

    elif int(pow) >= 0 and int(pow) <= 25 and P != PATHS[0]:
        P = PATHS[0]
        cap2.release()

        img = cv2.imread('video/level1.png')
        img = cv2.resize(img, (width, height))
        cv2.imshow(ORG_WINDOW_NAME, img)
        key = cv2.waitKey(INTERVAL)
        time.sleep(3)

        cap2 = cv2.VideoCapture(PATHS[0])
        sentense = sen[0]

    elif int(pow) > 25 and int(pow) <= 50 and P != PATHS[1]:
        P = PATHS[1]
        cap2.release()

        img = cv2.imread('video/level2.png')
        img = cv2.resize(img, (width, height))
        cv2.imshow(ORG_WINDOW_NAME, img)
        key = cv2.waitKey(INTERVAL)
        time.sleep(3)

        cap2 = cv2.VideoCapture(PATHS[1])
        sentense = sen[1]

    elif int(pow) > 50 and int(pow) <= 75 and P != PATHS[2]:
        P = PATHS[2]
        cap2.release()

        img = cv2.imread('video/level3.png')
        img = cv2.resize(img, (width, height))
        cv2.imshow(ORG_WINDOW_NAME, img)
        key = cv2.waitKey(INTERVAL)
        time.sleep(3)

        cap2 = cv2.VideoCapture(PATHS[2])
        sentense = sen[2]

    elif int(pow) > 75 and int(pow) <= 90 and P != PATHS[3]:
        P = PATHS[3]
        cap2.release()

        img = cv2.imread('video/level4.png')
        img = cv2.resize(img, (width, height))
        cv2.imshow(ORG_WINDOW_NAME, img)
        key = cv2.waitKey(INTERVAL)
        time.sleep(3)

        cap2 = cv2.VideoCapture(PATHS[3])
        sentense = sen[3]

    elif int(pow) <= 100 and int(pow) > 90 and P != PATHS[4]:
        P = PATHS[4]
        cap2.release()
        cap2 = cv2.VideoCapture(PATHS[4])
        sentense = sen[4]

    # 画像の取得と顔の検出
    img = c_frame
    height, width = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(img_gray, minSize=(50, 50))
    # print(face_list)

    # 背景動画の読み込み
    ret, frame = cap2.read()
    if not ret:
        cap2.set(cv2.CAP_PROP_POS_FRAMES, 10)
        continue

    frame = cv2.resize(frame, (width, height))
    cv2.putText(frame, sentense, (100, 100), cv2.FONT_HERSHEY_SIMPLEX,
                2, (255, 255, 255), 5, cv2.LINE_AA)
    cv2.putText(frame, pow, (width-150, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)

    if len(face_list) == 1:
        x = face_list[0][0]-50
        w = face_list[0][1]+100
        y = face_list[0][2]-50
        h = face_list[0][3]+100
        if x < 0 or y < 0 or h < 0 or w < 0:
            cv2.imshow(ORG_WINDOW_NAME, frame)
        else:
            face_img = img[y:h+y, x:x+w]
            height2, width2 = face_img.shape[:2]
            frame[y:y + height2, x:x+width2] = face_img

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
