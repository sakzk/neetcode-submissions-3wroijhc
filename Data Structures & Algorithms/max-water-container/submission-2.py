# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         l = 0
#         r = len(heights) - 1
#         if len(heights) < 2:
#             return -1
#         max_amount = min(heights[l], heights[r]) * (len(heights) - 1)
#         while l < r:
#             if heights[l] <= heights[r]:
#                 l += 1
#             else:
#                 r -= 1
#             max_amount = max(max_amount,
#                              min(heights[l], heights[r]) * (r - l))
#         return max_amount

# step1
# ポインタのアップデートのタイミングを､max_amountの計算後にした｡
# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         l = 0
#         r = len(heights) - 1
#         if len(heights) < 2:
#             return -1
#         max_amount = min(heights[l], heights[r]) * (r - l)
#         while l < r:
#             max_amount = max(max_amount,
#                             min(heights[l], heights[r]) * (r - l))
#             if heights[l] <= heights[r]:
#                 l += 1
#             else:
#                 r -= 1
#         return max_amount
"""
ロジック検討
- ポインタをアップデートしてから､max_amount をupdateするか､max_amountをアップデートしてからポインタを更新するか｡
    - 今回は先 max_amountのアプデ､あとl, r のアプデのほうがよい!
        - ループの最後で､l=rとなるパターンを除外するため｡
        - 一般に､どっちがいいとかあるのだろうか?今回は､ポインタのアプデはあとのほうがいい気がする
            - 単純に､max_amount = ... が2箇所から1箇所に減るのでコピペミスもしにくくなる｡
バグ検討
- コピペする際のポインタの更新
- = いれるか､いれないか
- エッジケース
    - 配列サイズ
    - ループの前､ループ1周目､中､ループ脱出直前､あと
    - 変数名のtypo
    - if/else
Edge Cases 検討
    # 脱出直前の最後のループでは､r-l = 0 となる
    # 大きい方をとるので､今回はこれで問題ない (問題バリエーションとして､min_amountとかだと問題になるので､一致ケースは弾く必要がある)
コアのアイデア
    - 絶対勝つやつを見つける or 勝つかもしれないやつと今のやつを比べる
        - 絶対勝つ条件を探すのは､処理が複雑になる
        - 勝つかもしれない条件を満たしているやつを､今のやつと比べて､勝ったやつで上書きするほうが実装が楽
    - ｢勝つかもしれないやつを見つける｣ -> ｢現時点で絶対に勝てないやつを捨てる｣
        - 半分捨てられれば､ O(logn).
        - 一つずつすてられれば､O(n).
        - 1つずつ捨てるのを､最適化してもO(long)にはならない｡定数倍ずつ捨てていくから｡
            - 条件がかなり自明であったり､l += 1と同じ程度には簡単ではないと､コードが複雑になることと速度向上のトレードオフになる
                - 今回はかなり複雑なのでやめる｡
    - 条件を満たすやつを見つける <-> 条件を必ず満たさないやつを捨てて､残りに注目する
        - ここまで抽象化すると､二分探索と同じ考え方だとわかる｡
    - 比較可能な2つのものの比較は､>, =, < の3つしかない｡
# デバッグ!
- max_amount を2つから1つに減らしたあとに､横幅のポインタを更新していなかった｡｡｡トホホ｡｡｡
"""


# step 3
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2: # こいつを忘れていた｡
            return 0
        l = 0
        r = len(heights) - 1
        max_amount = 0
        while l < r: # ここはちょっと考える
            # calc current amount and update max
            max_amount = max(max_amount,
                            min(heights[l], heights[r]) * (r - l)) # (r-l) のカッコ忘れ
            # procceed l
            if heights[l] <= heights[r]: # ここもちょっと考える
                l += 1
            # proceed r
            else:
                r -= 1
        return max_amount # return 文書き忘れていた!!!
# 書いている途中に､自分がなんでこれを選んだっけ?これって正しいんだっけ?を思い出せるようにする
# step3のデバッグ
# 配列長のassert忘れ
# r-l のかっこ忘れ｡字面通りに一回見れば気づけた
# return max_amount まるまる忘れ｡小さいケースで見落としなく走らせれば気づけた｡
"""
- 小さな例で､コードの見た目通りドライランすれば見つけられる｡見た目通りドライラン<=>意味がわかっているとしてスキップしない
    - 算術演算の優先順位
    - return文忘れ
- 探す範囲を狭める <=> 絶対勝つやつを見つけてアップデート or 絶対捨てられるところをすてて残りで勝つかもしれないアップデート
- アップデートとポインタ消費の順序
    - 初期化､アップデート､ポインタ消費
    - 初期化､ポインタ消費､アップデート
        - 最初は自然な方でやってみて､ループを通しで通る例で､エッジケースがないように調節する?
        - 初期化とアップデートをまとめられないか? で見る
- l, r の double pointerのアイデア
    - アイデア:ペアの全探索O(N^2)が､両端から狭めていけばO(N)になる
    - 何らかの条件で､l, rどっちか片方だけ､範囲が狭まるほうに1つ進められること｡
"""
