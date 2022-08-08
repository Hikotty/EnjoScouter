import gensim
from pprint import pprint
from janome.tokenizer import Tokenizer
import re
import trans as ts

eval = 0


def main():
    # modelの読み込みに時間がかかる，事前に読んでデモするといいかも
    model_path = "model/chive-1.2-mc5.kv"

    # モデルの読み込み
    print("読み込み中")
    model = gensim.models.KeyedVectors.load(model_path)
    print("あああああああああああああああああああ")

    while(1):
        text = ts.main()
        if(text == -1):
            continue
        # text = "今日はいい天気ですね"
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
    fire_words = ['炎上', '人権', '動画', '拡散', '不正', '歌い手', '喧嘩','女','男']
    # ,'女','男','家事','結婚','年齢','離婚','身長'

    for n in malist:
        if(regex.match(n.part_of_speech)):
            word_list.append(n.surface)

    for tmp_word in word_list:
        max_fire = 0
        for eval_word in fire_words:
            try:
                max_fire = model.similarity(eval_word, tmp_word)
            except:
                # max_fire = 0.1
                # max_fire = max_fire
                print(eval_word,tmp_word)
        if (max_fire >= 0.2):
            # eval += max_fire*100
            eval += 12.5
        else:
            eval -= 10
    if(eval < 0):
        eval = 0
    if(eval >=100):
        eval = 100
    print(eval)
    f = open('text/aiai.txt', 'w')
    f.write(str(eval))
    f.close()


if __name__ == "__main__":
    main()
