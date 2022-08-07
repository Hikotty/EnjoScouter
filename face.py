import cv2


if __name__ == '__main__':
    # 定数定義
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "org"
    GAUSSIAN_WINDOW_NAME = "gaussian"

    DEVICE_ID = 0
    path = r'/Users/ippei-go/Downloads/steamA.mp4'
    path2 = r'/Users/ippei-go/Downloads/fiem_b.mp4'
    path3 = r'/Users/ippei-go/Downloads/xpfire_CD.mp4'
    path4 = r'/Users/ippei-go/Downloads/nc274684.mp4'
    path5 = r'/Users/ippei-go/Downloads/skr2203c_b.mp4'
    C = [path5,path,path2,path3,path4]
    sentence = ['Peace','Fire...?','Fire!!','Fire!Fire!Fire!','Good luck...']

    # 分類器の指定
    cascade_file = "/Users/ippei-go/ytvhackthon/xml/haarcascade_frontalface_alt2.xml"
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
    cap2 = cv2.VideoCapture(path2)
    # 変換処理ループ
    while end_flag == True:

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
        cv2.putText(frame,sentence[0], (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5, cv2.LINE_AA)
        cv2.putText(frame,'10000', (width-100,100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5, cv2.LINE_AA)
        frame = cv2.resize(frame , (width,height))

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
    cap.release()
