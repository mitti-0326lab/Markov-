# Markov連鎖を用いたAIモデル
自由研究のときに使ったMarkov連鎖のAIモデル。Wikipedia日本版（日本：https://ja.wikipedia.org/wiki/日本 ）
## なぜ作った？
-AIモデルを実際に構築してみたかった。

-ラムダ技術部の動画の検証もしてみたかった。
### 参考動画（ラムダ技術部）はこちらから
[![【道を開けろ】AIでコムドットやまと風の名言を作ろう（敬称略）](youtube1.jpg)](https://www.youtube.com/watch?v=x5AwzoQgt3E)
&nbsp;
[![【数値化】言葉の足し算をするAIで遊んでみた](youtube2.jpg)](https://www.youtube.com/watch?v=sK3HqLwag_w&t=1s&sttick=0)
&nbsp;
[![【自動生成】入賞作品から作文を生成したら素晴らしい文章ができる説](youtube3.jpg)](https://www.youtube.com/watch?v=1OfCyavg_ZE&t=80s)

## 使用方法等
### １）付属のPythonファイル（markov.py）をダウンロード後、Python環境を開く。
### ２）データアセット（japan.txt）を同じフォルダ内に置く。
※このアセットの中身はWikipedia日本版「日本」のページの文章を、あらかじめ（）や「」等学習の妨げになる不純物をなくした状態の文章です。ライセンスに関してはCC BY-SA 4.0が適応されます。また、生成された文章の著作権等は曖昧なため、個人的な使用にとどめてください。また、Pythonコードのファイル名のところのjapan.txtの名前を変え、別途データを用意すれば学習させるデータを変えることができます。
### ３）MeCab導入
```python
pip install mecab-python3 unidic-lite
```
### ４）markov.pyを実行
私の場合はPyCharmを使用。
⚠使い方についてはガイドがあるので基本的には大丈夫だと思います。
