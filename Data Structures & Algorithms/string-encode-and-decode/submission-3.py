# 息も絶え絶え実装 -> コメント追加
class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for word in strs:
            lst.append(str(len(word)) + "#")
            lst.append(word)
        return "".join(lst)

    def decode(self, s: str) -> List[str]:
        print(f"decoder input: {s=}")
        words = []
        i = 0
        while i < len(s):
            # comsume number
            j = 0
            while i + j < len(s) and s[i+j] in "0123456789":
                j += 1
            print(i, j, s[i:j])
            # word_length = int(s[i:j]) # これは､i+jじゃないとだめ!
            word_length = int(s[i:i+j]) # i = 0 の初回だけ成立して､2回目以降のループで失敗する!
            print(i, i+j, s[i+j], word_length)
            if s[i+j] == "#":
                j += 1
            # if i + j + word_length < len(s):
            if i + j + word_length <= len(s): # ここは含める｡
                word = s[i+j: i+j+word_length]
                print(word)
                words.append(word)
            print(f"{i=}")
            print(f"{i+j+word_length=}")
            i = i + j + word_length
        return words
"""
- 変数名
    - consume number と consume # が終わった段階で､ word_head = i+j とかにしたほうがわかりやすい気はする｡
    - インデックス感を出すなら､word_length は lでもよい｡ スライスに長々書いてあるとそれはそれで見にくいと感じるので｡

- pythonのスライス
    - 確か､listの部分の浅いコピーのはず
    -> doc, cpythonで確かめよう
    - 文字列のスライスを作りまくったらどうなるか? 今回は部分文字列を見ているだけなので､実体の更新はしていない
- int()あたりの実装を見てみると良さそう
- 文字列の切り出し､ポインタ｡
    - ループのあいだ常に満たしていてほしいこと｡i < len(s), i+j+word_length <= len(s) (スライスの右端として使うので)
- 考える流れ: ループの外側から書くイメージ｡
    - sを捜査したあとに words: List[str] を返すよねー､
    - sを走査: 数値の消費､#の消費､単語の消費だよねー｡
        - それぞれ関数化すると､インデックスと文字列の受け渡しで面倒なので､i, jの2つのポインタでやるのが今回は楽そうだなー､ぐらい
- print()の埋め込みどころ
    - インデックスの初期化､更新､
    - consume XX が終わった時点
    ぐらいかなー｡
- デバッグ: ループの1回目だけうまく動く
    - 2回目以降のループで､1回目の引き継ぎがうまくできていない可能性あり｡
        - ★更新すべきところが固定値になっている

- あと､decodeに渡される入力が壊れていたらどうするのがいいのか
    - おかしなデータを見てわかる?
    - 壊れ方によっては正常なデータと見分けがつかないよなー｡

- あと､今回のやつで並列化するにはどうするか
    - ちょっと思いつかない｡
    - `<int>#`を前から見ていく
- うーん､encode, decodeの応用例ってなんだろう?
    - JSONのパースとか､decodeだよなー｡
    - dict <-> jsonとかか｡
    - 後戻りが必要になったらむずくなりそう｡1パスで後戻りなしでできる今回は簡単な部類のはず｡
        - C言語の複雑な型宣言とかは難しそう｡
"""

# 混乱の跡
        # # ちょっと大変｡ #まで読む､数値を読む､頭から数値の分文字数を切り出す
        # # slice words from s
        # words = []
        # head = 0
        # while s:
        #     hash_index = s.index("#")
        #     if not hash_index:
        #         break
        #     word_character_count = int(s[head:hash_index])
        #     print(word_character_count)
        #     word = s[hash_index+1: hash_index + word_character_count + 1]
        #     words.append(word)
        #     s = s[word_character_count +1:]
        #     head = word_character_count + 1

        #     print(word)
        # return

        # うわーん､スライスheadを見ているか､s[0]を見ているか､一貫せずに混乱しちゃう!!!
        # def _read_word_length(s_slice_head_index, s):
        #     return 
        # s_slice_head_index = 0
        # while s_slice_head_index < len(s):
        #     word_length = read_word_length(s_slice_head_index, s)
        #     word = read_word(s_slice_head_index, word_length)
        #     words.append(word)
        #     s_slice_head_index += len(str(word_length)) + word_length + 1
        # return words
        # # 文字列をトークナイズしていくのって､定石あるよなぁ｡