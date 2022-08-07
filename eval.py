import gensim
from pprint import pprint
from janome.tokenizer import Tokenizer
import re
import transcription as ts


def calc(text):
    # chiVeデータのPATH（kv:KeyedVectors）
    # modelの読み込みに時間がかかる，事前に読んでデモするといいかも
    model_path = "model/chive-1.2-mc90.kv"

    # モデルの読み込み
    model = gensim.models.KeyedVectors.load(model_path)

    # 類似度上位10件を取得
    # match = wv.most_similar(positive=['姪', '男性'], negative=['女性'],topn=20)

    # match = model.most_similar("炎上", topn=20)

    # 見やすい形式で表示
    # pprint(match)

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

    for tmp_word in word_list:
        max_fire = 0
        for eval_word in fire_words:
            max_fire = model.similarity(eval_word, tmp_word)
        if (max_fire >= 0.2):
            eval += max_fire*100
        else:
            eval /= 2

    print(eval)

if __name__ == "__main__":
    text = ts.main()
    # text = "今日はいい天気ですね"
    calc(text)
