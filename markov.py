import os
import markovify
import MeCab


def main():
    print("\nMarkov連鎖を用いたAIモデル\n")

    input_file = "japan.txt"
    cleaned_file = "japan_clean.txt"

    if not os.path.exists(input_file):
        print(f"{input_file} が見つかりません。")
        return

    # 1. テキストファイル整形
    if not os.path.exists("corpus"):
        print("1. テキストファイル整形")
        encodings = ["utf-8", "shift_jis", "cp932", "euc_jp"]
        text_content = ""
        for enc in encodings:
            try:
                with open(input_file, "r", encoding=enc) as f:
                    text_content = f.read()
                break
            except Exception:
                continue

        text_content = text_content.replace("「", "").replace("」", "").replace("『", "").replace("』", "")
        lines = text_content.split("。")
        with open(cleaned_file, "w", encoding="utf-8") as f:
            for line in lines:
                if line.strip():
                    f.write(line.strip() + "。\n")

    # 2. MeCab (Pythonパッケージ版を用いる)
    print("2. MeCabを用いてAIモデルを生成")
    tagger = MeCab.Tagger("-Owakati")
    try:
        with open(cleaned_file, "r", encoding="utf-8") as infile, open("corpus", "w", encoding="utf-8") as outfile:
            for line in infile:
                parsed = tagger.parse(line)
                outfile.write(parsed)
    except Exception as e:
        print(f"MeCabの処理に失敗　理由: {e}")
        return

    # 3. corpusを読み込む
    with open("corpus", "r", encoding="utf-8") as f:
        corpus_text = f.read()

    # 初期設定案内
    target_length = 300
    current_state_size = 2

    # AIモデル作成
    text_model = markovify.NewlineText(corpus_text, state_size=current_state_size)
    print(f"3. AIモデルの準備が完了しました。現在のstate_size: {current_state_size}）")

    while True:
        print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ")
        print(f"現在の設定 ➔ 目標: {target_length}文字以上 / state_size: {current_state_size}】")
        user_input = input("単語を入力するか、そのままEnterでランダム生成を開始します。）\n>> ").strip()
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

        if user_input.lower() == 'n':
            print("\n終了しました。\n")
            break

        elif user_input.lower() == 'c':
            try:
                new_length = input("新しく設定したい文字数を数字で入力してください\n>> ")
                target_length = int(new_length)
                print(f"➔ 目標文字数を 【{target_length}文字】 に変更しました。")
            except ValueError:
                print("無効な数字です。元の文字数のまま続けます。")
            continue

        elif user_input.lower() == 's':
            try:
                new_state = input("新しく設定したいstate_sizeを1〜3の数字で入力してください\n>> ")
                new_state_int = int(new_state)
                if new_state_int in [1, 2, 3]:
                    current_state_size = new_state_int
                    # ここでAIモデルを新しく作り直す（再学習）
                    text_model = markovify.NewlineText(corpus_text, state_size=current_state_size)
                    print(f"➔ state_sizeを{current_state_size}に変更してAIを再構築しました。")
                else:
                    print("state_sizeは1、2、3のいずれかを入力してください。")
            except ValueError:
                print("無効な数字です。元の設定のまま続けます。")
            continue

        print(f"\n目標文字数{target_length}文字以上の返答を生成\n")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        generated_story = []
        total_chars = 0

        # 1発目の文章生成
        first_sentence = None
        if user_input:
            # 単語が指定されている場合は、その単語からスタートを試みる
            try:
                first_sentence = text_model.make_sentence_with_start(user_input, max_chars=200, strict=False)
            except Exception:
                first_sentence = text_model.make_sentence(max_chars=200)
        else:
            # 空欄（そのままEnter）の場合は完全ランダムで1文目を作る
            first_sentence = text_model.make_sentence(max_chars=200)

        if first_sentence:
            clean_sentence = first_sentence.replace(' ', '')
            generated_story.append(clean_sentence)
            total_chars += len(clean_sentence)

        # 2発目以降の文章を繋げて目標文字数まで引き伸ばす
        for _ in range(200):
            if total_chars >= target_length:
                break

            sentence = text_model.make_sentence(max_chars=200)
            if sentence:
                clean_sentence = sentence.replace(' ', '')
                generated_story.append(clean_sentence)
                total_chars += len(clean_sentence)

        # 画面に出力
        if generated_story:
            print("".join(generated_story))
        else:
            print("(エラー：もう一度Enterを押すか、別の単語を試してください)")

        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n")
        print("※ 終了: 'n' ｜ 文字数変更: 'c' ｜ state_size変更: 's'")


if __name__ == '__main__':
    main()
