from concurrent import futures
import time
import random
import cv2
import view
import eval
import re
from janome.tokenizer import Tokenizer
import gensim
from pprint import pprint
import trans as ts


path = r'movie/steamA.mp4'
path2 = r'movie/nc84025.mp4'
path3 = r'movie/xpfire_CD.mp4'
path4 = r'movie/nc274684.mp4'
path5 = r'movie/skr2203c_b.mp4'

C = [path5, path, path2, path3, path4]
sentence = ['Peace', 'Fire...?', 'Fire!!', 'Fire!Fire!Fire!', 'Good luck...']
eval = 0

def main():
    # modelの読み込みに時間がかかる，事前に読んでデモするといいかも
    model_path = "model/chive-1.2-mc90.kv"

    # モデルの読み込み
    model = gensim.models.KeyedVectors.load(model_path)
    while(1):
        text = ts.main()
        if(text == -1):
            continue
        # text = "今日はいい天気ですね"
        calc(text, model)

def viewer():
    global eval
    # for i in range(5):

    PATH = C[eval]
    cap = cv2.VideoCapture(PATH)
    while(True):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (1920, 1080))
            cv2.putText(frame, sentence[0], (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5, cv2.LINE_AA)
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    print("AAAAAAAAAAA")
    cap.release()
    # cv2.destroyAllWindows()

def calc(text, model):
    global eval
    # 正規表現
    pat = r'名詞'
    regex = re.compile(pat)

    t = Tokenizer()
    malist = t.tokenize(text)

    word_list = []

    # 炎上しそうなワード
    fire_words = ['炎上', '人権', '動画', '拡散', '不正', '歌い手', '喧嘩']

    eval = 0

    for n in malist:
        if(regex.match(n.part_of_speech)):
            word_list.append(n.surface)

    # for tmp_word in word_list:
    #     if(tmp_word)

    for tmp_word in word_list:
        max_fire = 0
        for eval_word in fire_words:
            max_fire = model.similarity(eval_word, tmp_word)
        if (max_fire >= 0.2):
            eval += max_fire*100
        else:
            eval /= 2
    print(eval)


future_list = []
with futures.ThreadPoolExecutor(max_workers=4) as executor:
    future1 = executor.submit(viewer(), index=1)
    future_list.append(future1)
    future2 = executor.submit(main(), index=2)
    future_list.append(future2)
    _ = futures.as_completed(fs=future_list)

print('completed.')
