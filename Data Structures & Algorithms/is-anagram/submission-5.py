class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def _count_char(s: str) -> dict:
            char_to_count = dict()
            for c in s:
                if c not in char_to_count:
                    char_to_count[c] = 0
                char_to_count[c] += 1
            return char_to_count
            
        s_char_to_count = _count_char(s)
        t_char_to_count = _count_char(t)
        return s_char_to_count == t_char_to_count
    
    """
    - クラスの関数定義の順序｡関数呼び出しの後ろに定義があっても大丈夫か?
        - ｢大丈夫か?｣の意味: 言語仕様レベル､コーディング規約レベルそれぞれでどうか｡
    - sortedでkeyでソートするイディオム
        - 組の集まりに対して､組の特定の要素でソートしたい､という需要はよくありそうなので､簡単にできるようになっていてもおかしくない｡
        - dict のキーでソートしたい場合どうするか?
            - これはできない: `sorted(s_char_to_count, key=lambda x: x.items()[0])`
    - dict, Counterの == の実装を見てみる
        - 要素の順序が違っても同一と判定することを確認する
    - dictと､dict.items() の違いを調べる
        - sorted(dict.items()が可能なのはどのようにしてか?)
            - sorted(dict) は何をしているのか
    """
    """ フォローアップ
    - 文字の制約を変えてみる
        - 同一扱いしたい文字がある場合どうするか?: 大文字と小文字､スペース･タブ､改行コード(LF, CR)
        - エンコーディングが UTF-8 ならどうするか?
    """

    # だめ回答: Counter, dict は sort() できません
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s_char_to_count = Counter(s)
    #     t_char_to_count = Counter(t)
    #     dict(s_char_to_count).sort()
    #     dict(t_char_to_count).sort()
    #     return s == t
    """
    - 確認する事項
        - Counter, dict のドキュメントでsort() がサポートされていないこと
        - Counter, dict の実装でsort() がサポートされていないこと
    """