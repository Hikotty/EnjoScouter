# 炎上スカウター

## 炎上という社会問題
炎上とは，インターネットやラジオ，テレビなど，公共の場でなされた言動について，インターネット上で批判・擁護・誹謗中傷が繰り広げられるイベントである．

近年，この「炎上」が大きな社会問題となりつつある．
  
ジェンダー，性差別，犯罪擁護，動物の権利など．．．我々はかつてないほど，自分の発言に気をつけなければない時代の中にいる．
  
「炎上」は，仮にその発言や行動が，実は問題のないものであったとしても，人々には社会を騒がせたという印象が残り続ける．
  
我々一般市民はもちろんのこと，著名人・芸能人にとって，自らの発言が炎上した場合には，その名声だけでなく，生活すらも抜き差しならないものとなるのである．
  
## 炎上スカウター
そこで我々は，炎上度をスマートグラス上で可視化してユーザに分かりやすくフィードバックするシステムである「炎上スカウター」を提案する．

炎上スカウターは，鳥山明作「ドラゴンボール超」で「ラディッツ」や「フリーザ」などの敵役が使用するデバイスから着想を得て開発した．

炎上スカウター越しにテレビを見ることで，テレビに出演する芸能人の発言が炎上する可能性が高いのかどうか，数字と分かりやすいアニメーションで確かめることができ,
これにより，視聴者は安心してテレビを見ることができる．

テレビ収録の場面では，出演者が炎上スカウターを装着し，自分の顔をモニター越しに見ることで，自分の発言の炎上度を確かめ，注意することができる．

## システム詳細
炎上スカウターはスマートグラス・PCから構成される．

図１に示すように，ユーザから発された言葉は，PCのマイクを通じて収集され，Azure speech2text APIと呼ばれる音声データから文字起こしを行うAPIに送られる．

文字起こしされたテキストデータは，形態素分析によって単語レベルまで分解され，word2vecによって，ベクトルに変換される．

ベクトル化されたデータは，事前に定義された炎上度推定モデルに入力され，ある発言がどの程度炎上する可能性があるのか，数値化される．

炎上度に応じてスマートグラスに表示する画面をCV２を用いて動的に生成し，ユーザに提示する．

## 謝辞
本システムはYTVハッカソンへ提出した．

## メンバー
伊勢田氷琴*

後藤逸兵*

三嶋佑輝*

*奈良先端科学技術大学院大学先端科学技術研究科情報科学領域ユビキタス・コンピューティングシステム研究室Μ１

http://ubi-lab.naist.jp/ja/

# Enjo Scouter

## Background
"Enjo" is a phenomenon that criticism, defense, and slander of words and deeds in public, such as on the Internet, radio, and television, are spread on the Internet.

In recent years, "Enjo" have become a major social issue.
  
Gender, sexism, criminal advocacy, animal rights, etc.... We are living in an era where we have to be more careful about what we say than ever before.
  
Even if what is said or done in a is actually harmless, people are left with the impression that it has caused a social uproar.
  
For celebrities and entertainers, not to mention the general public, their fame and even their lives are at stake if their comments come under fire.

## Our Proposal "Enjo Scouter"
We propose the "Enjo Scouter," a system that visualizes the degree of "Enjo" on smart glasses and provides users with easy-to-understand feedback.

The Enjo scouter was inspired by the device used by the antagonists "Raditz" and "Freeza" in "Dragon Ball Super" by Akira Toriyama.

By watching TV through the Enjo Scouter, viewers can check whether or not a TV celebrity's comments are likely to cause a Enjo, using numbers and easy-to-understand animations. This enable viewers to watch TV with peace of mind.

In the TV recording scene, the actors wear the Enjo scouter and look at their own faces through the monitor to check the degree of Enjo of their statements and.

## System 
The flame scouter consists of smart glasses and a PC.

As shown in Figure 1, words uttered by the user are collected through the PC's microphone and sent to the Azure speech2text API, which performs transcription from speech data.

The transcribed text data is broken down to the word level by morphological analysis and converted into vectors by word2vec.

The vectorized data is then input into a pre-defined "Enjo estimation model" to quantify the likelihood of a certain statement becoming flammable.

Depending on the degree of inflammability, the screen displayed on the smart glasses is dynamically generated using CV2 and presented to the user.

## Acknowledge
This system was submitted on YTV Hackathon.

## Member 
Iseda Hikoto(M1 Student of Ubiquitous Computing Syatem Lab, at Nara Institute of Science and Technology, Nara, Ikoma)  
Goto Ippei(M1 Student of Ubiquitous Computing System Lab, at Nara Institute of Science and Technology, Nara, Ikoma)  
Mishima Yuki(M1 Student of Ubiquitous Computing System Lab, at Nara Institute of Science and Technology, Nara, Ikoma)  
http://ubi-lab.naist.jp/ja/
