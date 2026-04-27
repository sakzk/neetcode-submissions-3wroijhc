# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) < 3:
#             return 0
#         # とりあえず全探索で書いてみる
#         total = 0
#         for i in range(1, len(height) - 1):
#             trapped = min(max(height[:i]), max(height[i+1:])) - height[i]
#             if trapped > 0:
#                 total += trapped
#         return total

"""
Test Cases:
- [1, 2 ,3]
- [2, 1, 3]
- [2, 3, 1]
-> OK.
- ドライランデバッグ:
    - trapped < 0 のパターンの考慮漏れを見つける
    - len(height) - 1 で正しいことを再確認 (range(1, 1) でターミナル実行して､range(a, b) が､[a, b)であることを確認
Approach:
Idea
- given i (0 <= i < len(height), min(max[0:j], max[j+1:]) is water amount stored height[i]
全探索で､O(N^2)
    - 1-pass
        - i に対して､max_so_far を覚えておく

分析:
max() の探索は､O(N) かかるので､全体として､O(N^2) time complexity になる｡
space complexity O(1)

"""

# step 2
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # construct max so far from left list
        m = 0
        max_so_far_from_left = [0]
        for i in range(1, len(height)):
            max_so_far_from_left.append(max(m, height[i-1]))
            m = max(m, height[i-1])
        m = 0
        max_so_far_from_right = [0]
        for i in range(len(height) - 2, -1, -1):
            max_so_far_from_right.append(max(m, height[i+1]))
            m = max(m, height[i+1])
        max_so_far_from_right.reverse()
        total = 0
        for i in range(1, len(height) - 1): # 両端はスキップ
            trapped = min(max_so_far_from_left[i], 
                          max_so_far_from_right[i]) - height[i]
            if trapped > 0:
                total += trapped
        return total
"""
Test Cases:
- [1, 2 ,3]
    max_from_left
  [1, 2] <- あれ､これ0が入っていないのは想定通りだっけ? 違う｡ trappedの計算でmax_so_far_from_left/rightは0がいることを期待している｡
  [0, 1, 2] 0入れたバージョン
  max_from_right
  [0, 3, 3] 
  [3, 3, 0] (reversed)
  -> OK
- [2, 1, 3]
    [0, 2, 2]
    [0, 3, 3]
    -> score: 1
- [2, 3, 1]

# デバッグ
- class Solution: 配下の docstring のインデント
- trapped の計算｡ カッコの対応がおかしくて､_left が数値型担っていた｡
- _rightが_leftのママ残っていた(コピペの温存ミス) -> コピペする前に､何を温存するのか､何を変えるのか意図をコメントしたほうがいいなー｡
    - max がゴミ｡一つ前の解法の残骸
        # trapped = min(max(max_so_far_from_left[i], 
        #               max_so_far_from_right[i])) - height[i]
```
Traceback (most recent call last):
  File "/box/main.py", line 99, in main
    output = solution.trap(input)
  File "/box/main.py", line 54, in trap
    trapped = min(max(max_so_far_from_left[i],
              ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      max_so_far_from_right[i])) - height[i]
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'int' object is not iterable
```

# リファクタ
- m をいちいち置かなくていい気がする｡
- mのアップデートと更新は､更新してアップデートがいい気がする｡

# アイデア
一度､left_maxs, right_maxsを構築する｡ suffix_arrayの要領で｡
そうすれば､ max(height[]) の検索が､O(1)になるので､全体として､O(N)になる｡
l, r, rの逆転で､O(3N) -> O(N) + O(N) -> O(N) time complexity
配列の長さNに比例する長さの補助配列を2本作るので､ O(N) space complexity

"""