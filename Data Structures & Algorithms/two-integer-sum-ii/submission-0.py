class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # assert(2 <= numbers.length <= 1000)
        # init l, r
        l = 0
        r = len(numbers) - 1
        # search index1, index2 pair
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total < target:
                l += 1
                continue
            # total > target
            r -= 1
        # if valid [index1, index2] doesn't exist
        return []
"""
- [1, 2, 3, 4], target 3 -> OK 
- [1, 2, 3, 4], target 7 -> OK
いちおう､､､異常な入力で止まること
- [1, 2], target -1 -> OK
- [1, 2], target 4 ->
"""


"""
アプローチ:
- l = 0, r = len(numbers) - 1 で狭めていこう
    - sum < target -> l+=1
    - sum > target -> r-=1
    - sum == target -> return [l+1, r+1]

テストケース:
- [1, 2, 3]
- [1, 2, 3, 4] : この例でドライランせずにバグを見落とした｡
- [1, 1, 1, 2, 3]

制約:
- exactly one valid solution
    - 答えがない､答えが2つ以上ある､は異常としてあつかうとよさそー
- 今回は値のオーバーフローは気にしなくて良さそう

デバッグ:
"""
