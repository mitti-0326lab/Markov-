# Markov連鎖を用いたAIモデル
自由研究のときに使ったMarkov連鎖のAIモデル。Wikipedia日本版（日本：https://ja.wikipedia.org/wiki/日本 ）

## 使用方法等
### １）付属のPythonファイル（markov.py）をダウンロード後、Python環境を開く。
### ２）データアセット（japan.txt）を同じフォルダ内に置く。
※このアセットの中身はWikipedia日本版「日本」のページの文章を、あらかじめ（）や「」等学習の妨げになる不純物をなくした状態の文章です。ライセンスに関してはCC BY-SA 4.0が適応されます。また、生成された文章の著作権等は曖昧なため、個人的な使用にとどめてください。また、Pythonコードのファイル名のところのjapan.txtの名前を変え、別途データを用意すれば学習させるデータを変えることができます。
### ３）MeCab導入
```python
pip install mecab-python3 unidic-lite
```
### ４）markov.pyを実行

