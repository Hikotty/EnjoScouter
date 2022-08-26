import gensim
from pprint import pprint
from janome.tokenizer import Tokenizer
import re
import time
import trans as ts

eval = 0

def main():
    # modelの読み込みに時間がかかる，事前に読んでデモするといいかも
    model_path = "model/chive-1.2-mc90.kv"
    # モデルの読み込み
    print("読み込み中")
    model = gensim.models.KeyedVectors.load(model_path)
    print("読み込み完了")
    going_time = time.time()
    while(1):
        text = ts.main()
        if(text == -1):
            continue
        calc(text, model)


def calc(text, model):
    # 正規表現
    global eval
    pat = r'名詞'
    regex = re.compile(pat)

    t = Tokenizer()
    malist = t.tokenize(text)

    word_list = []

    # 炎上しそうなワード
    fire_words = ['炎上','人権','動画','拡散','不正','歌い手','喧嘩','女','男']

    for n in malist:
        if(regex.match(n.part_of_speech)):
            word_list.append(n.surface)

    for tmp_word in word_list:
        max_fire = 0
        for eval_word in fire_words:
            try:
                max_fire = max(model.similarity(eval_word, tmp_word),max_fire)
            except:
                max_fire = max(0.1,max_fire)
                #print(eval_word,tmp_word)

        if (max_fire >= 0.2):
            eval += 10
        else:
            eval -= 5

    if(eval < 0):
        eval = 0

    if(eval >=100):
        eval = 100

    eval = int(eval)
    print(eval)
    f = open('text/aiai.txt', 'w')
    f.write(str(eval))
    f.close()

if __name__ == "__main__":
    main()