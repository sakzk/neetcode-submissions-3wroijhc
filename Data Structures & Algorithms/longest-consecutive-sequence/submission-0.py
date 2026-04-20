class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        seen_nums = set()
        print(nums)
        for num in nums:
            i = 1
            j = 1
            while num - i in nums and num - i not in seen_nums:
                # nums - i がすでみたものなら､前の for num で見つけているやつなのでbreak
                seen_nums.add(num - i)
                i += 1
            i = i - 1
            # assert i = less_count + 1
            while num + j in nums and num + j not in seen_nums:
                seen_nums.add(num + j)
                j += 1
            # assert j = more_count + 1
            j = j - 1
            run = i + j + 1 # これだめですねー｡ 2になっちゃうなー
            max_len = max(run, max_len)
        return max_len

#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = set(nums)
#         max_len = 0
#         seen_num = set()
#         for num in nums:
#             i = 1
#             j = 1
#             while num - i in nums:
#                 nums.remove(num - i)
#                 i += 1
#             # assert i = less_count + 1
#             while num - j in nums:
#                 nums.remove(num - j)
#                 j += 1
#             # assert j = more_count + 1
#             run = i + j - 1
#             max_len = max(run, max_len)
#         return max_len
#
"""
setに変換して､
num in num_set に対して､
num を起点に､ num - 1, num - 2, num - 3 の長さを見る
num を起点に､ num + 1, num + 2, num + 3 の長さを調べる
num_count_less + num_count_more を足す!

あ､
 3, 4, 5, 6, 7 はどれが起点でも､それ以上･それ以下の連続がおなじになる｡
 -> 調べたら､removeで取り除くので良さそう｡
すべての要素を一回だけ見るので､O(N)になる

ただ､ループしながらループの要素を削除するのは大丈夫だっけ?
-> listは結構危険な操作だったはず｡
set を for で回すときって､何に対してforを回しているんだろう?

assert: set から削除しながらremoveすると､その時点の残りに対してforのループが継続する
-> うーん､結構危ないなぁ｡
-> 普通に駄目でした｡
```
Traceback (most recent call last):
  File "/box/main.py", line 49, in main
    output = solution.longestConsecutive(input)
  File "/box/main.py", line 5, in longestConsecutive
    for num in nums:
               ^^^^
RuntimeError: Set changed size during iteration
```

デバッグ: remove(i) ではなく remove(num - i)｡ i は存在することをassertしていない｡
list -> set で順序が保存されるか怪しいので､テストがランダムになる｡｡｡
"""