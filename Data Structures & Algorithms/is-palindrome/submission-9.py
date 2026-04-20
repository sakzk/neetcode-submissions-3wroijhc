AlphaNumericChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # assert s はASCII文字
        l, r = 0, len(s) - 1
        s = s.lower()
        print(s)
        # assert s の英字は小文字のみ
        while l < r: # l == r なら､s[l] == s[r] なので､一致判定はスキップできる｡なのでl==rの1文字手前のインデックスまでのT/Fと一致する
            # consume l
            while l < len(s) and s[l] not in AlphaNumericChars:
                l += 1
            # consume r
            while r > -1 and s[r] not in AlphaNumericChars: # r < len(s) があると､ どこかで rをインクリメントしているシグナルになっちゃうかなぁ? -> r が 0 より左に行くのをガードする必要がある｡
                r -= 1
            # 一つ前のループでは､s[l] == s[r] を保証しているので､
            # 無視すべき文字を無視しきって､文字列全体を消費した場合は､Trueを返すために脱出する
            # 無視すべき文字を無視しきったとき､以下のOR条件の少なくとも一つが成立している｡
            if l >= len(s) or r <= -1 or l >= r:
                break
            # compare s[l] with s[r]
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

        
"""
アプローチ
- ひとまず1パスでやっていくことにする｡出題意図っぽいので｡
- s_chars に入れて､ [::-1] とかで逆さ文を作るのもありだなー｡

仕様:
- s[l] == s[r] が一度も発生しなかった s を True, False どっち扱いすべきか?
    - 今の実装だと､Trueになるが｡｡｡
        - そもそも回文の判定をしたいのってどんな時だ?
        - もっと抽象的に: 文字列にたいして､Y/Nを判定するときに､空文字列はどっちにあつかうべき?
        - 実装上
            - is_x(s) and not is_empty(s) で絞れるので､空判定は別に分けるのも手だなー｡
            - パフォーマンス上､空判定もis_x() にふくめることもできる､ぐらいでいいか｡
    - Trueのほうがよいりゆう
    - False のほうが良い理由
    - 空文はNoneを返す､もあるなぁ｡

制約
- non-alphanumeric char は無視でOK
- 文字の大文字･小文字
    - lower, upper があった気がする
- ひとまず考えなくていいこと
    - s がマルチバイト文字で構成されるならどうするか

- ライブラリ: 文字がascii の alphanumericか判定する関数があったきがする
- ライブラリ: AlphaNumericCharsはどっかで定義されていそう
    - 毎回打ってたらいつかまちがえちゃうよ｡｡｡
- Python: https://docs.python.org/3/library/stdtypes.html#str.lower
    - s = s.lower()
- Python: not (x in y) と､ x not in y どっちが望ましいんだっけ?
    - and, or でつないだときにどっちが混乱しにくい?

- デバッグ:
    - 0 <= r < len(s) の反転をミスった｡
        - うーん､なんでコピペしちゃったんだろうか? 
            - break の目的を書き下す前に条件を書いちゃった｡

- 細かいところ:
    - break 条件で､ l > r とするか､ l >= r とするか
    - # この条件が混ざっていると､消費しきったのか､消費の途中なのか混ざっちゃう｡ので取りく｡
    - と､思ったが､ "a   a" のパターンがある
    - l > r はいる｡
    - l == r は次のループに任せると､l > r になって結局同じ｡=含めてもいいきはするけど､読み手への印象かなー｡


フォローアップ
- 2パス(lower() してから､parindrome の判定をする)のと､1パス(lower()しながら判定する)のとでは､どちらが早そうか?

"""