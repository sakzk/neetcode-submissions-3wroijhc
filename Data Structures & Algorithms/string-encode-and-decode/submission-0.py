# 息も絶え絶え実装
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
            if i + j + word_length <= len(s): #ここは含める｡
                word = s[i+j: i+j+word_length]
                print(word)
                words.append(word)
            print(f"{i=}")
            print(f"{i+j+word_length=}")
            i = i + j + word_length
        return words


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