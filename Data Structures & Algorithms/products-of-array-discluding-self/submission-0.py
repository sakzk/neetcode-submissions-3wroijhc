# 息も絶え絶え,
# product_rl が怪しい｡

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        手でやる｡
        [1, 2, 3, 4]
        [1,  1,  2, 6]
        [24, 12, 4, 1]
        [24, 12, 9, 6]
        """
        product_lr = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            product_lr[i] = product_lr[i-1] * nums[i-1]
        product_rl = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            product_rl[i] = product_rl[i+1] * nums[i+1]
        # 一旦確認
        # print(f"{product_lr=}")
        # print(f"{product_rl=}")
        product_except_self = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            product_except_self[i] = product_lr[i] * product_rl[i]
        return product_except_self
    # 例を書くとサクッと書き下.
    """
    # エッジケース検討
    len(nums) == 0, len(nums) == 1 のときどうなるか? -> product_rl を作る時のインデックスでバグりそう
    range(0) -> range(0, 0) -> これ何ができるんだろう?
    range(1) -> range(0, 1) -> 0
    手元で確認｡
    >>> [1 for _ in range(0)]
    []
    >>> [1 for _ in range(0, 1)]
    [1]

    len(nums) == 0 のとき､[] に インデックス-2でアクセスしてエラー
        その前に､product_lrを作る [i-1]でエラーが出る｡ から配列へのアクセスなので｡
    len(nums) == 1 のときは､[1]にインデックス-1でアクセスするのでエラーは出ない｡

    エラーハンドリングをちゃんとやるなら､
    len(nums) == 0 で弾く､len(nums) == 1 で､return[1] のアーリーリターンかなー｡要素一つのときは､それ以外の積を考える意味があまりない｡
    
    別のアプローチ(というより､リファクタリング程度)
        product_rl の作成を省略して､直接 product_rl[i]をproduct_lr[i] に掛ければよい｡
    """




        # # assert(len(nums) >= 2)
        # product_lr = [1 for _ in range(len(nums))]
        # product_rl = [1 for _ in range(len(nums))]
        # # get product_lr
        # # product_lr = [1, 1, 2, 6]
        # p = 1
        # print(product_lr)
        # # get Product_rl
        # # product_rl = [24, 6, 3, 1]
        # result_product = [1 for _ in range(len(nums))]
        # for i in range(len(nums)-2, -1, -1):
        #     product_rl[i] = p * nums[i]
        #     p = p * nums[i]
        # print(product_rl)
        # # get product execept self
        # for i in range(len(result_product)):
        #     result_product[i] = product_lr[i-1] * product_rl[i+1]
        # print(result_product)
        # return result_product

"""
アプローチ
- 全部の要素の積をつくっておいて､その数 nums[i] で割る
    - nums[i] == 0 のときはどーすべきか､が気になるが制約上だめ
    - これなんでこんな制約があるんだ?
        - 割り算をできる限りやらないことで性能上有利になる状況がまぁありそう｡
    - リストに対して､i に対して､nums[i] 以外の全てで何かを作る､をしたい状況ってなんだろう?
- 右からの積､左からの積の2つの配列をかける
    - インデックス管理が面倒そう
    - あと､端の要素をどううまく設定するか?
    - -> 積なので､nums[0], nums[len(nums)-1] は1にするとまぁ良さそう
        - n = 0, 1, 2 のときエッジケース｡3以上は一般ケース
            - 制約上は､ 2 <= len(nums) <= 1000
制約
- -20 <= nums[i] <= 20
    - 20*1000をやると
        - 2**5 * 2**10 -> 2**15 < 2**16-1

"""