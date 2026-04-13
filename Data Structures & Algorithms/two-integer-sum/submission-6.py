class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i in range(len(nums)):
            if target - nums[i] in num_to_index:
                return [num_to_index[target - nums[i]], i]
            num_to_index[nums[i]] = i
        return []

"""
関数のインタフェース
- インデックスの組を返す
- 見つからなかったときどーするか?
    -> ひとまず[] を返せばいいかー｡
    -> 具体的な処理によっては､例外､Noneもあり? Noneだとreturn書き忘れ特別するのに実装を見る必要がある｡
    -> List[int] で決めているので､[] か [-1, -1]とかか｡ Pythonだと､インデックスの-1に意味があるので､[]がいいかなー｡
        - TODO: list[-1] のときに何が起きているか?要素指定の仕組み
アプローチ
- ソートして左端･右端から狭めていく
    - nums[left] + nums[right] が､>targetならright--､ =targetならreturn, <targetならleft++｡
    - left >= right になったら脱出｡ 
- num_to_indexで､これまでに出た値とそのインデックスを覚えていく
    -> 今回はこれでやる

入力いろいろ
- 一つの要素を2つと見ていい場合はどうしますか?
    - 方法1) nums[i] == target/2 のアーリーリターンを追加する
    - 方法2) 今は､補数の判定->num_to_indexに入れる､の順でやっている｡これを､｢dictに入れる->補数の判定｣にすると､1要素のダブルカウントにも対応できる

そういえば...
- dictの初期化方法は2つ思いつく｡それぞれ何をやっているのか?
    - {}, dict()
    - dict() はキャストにも使われるので､初期化以外にも処理が走ってそう?オーバーヘッドはどれぐらい
"""
"""
- フォローアップ
    - numsの要素が1T個だったらどうします?
    - nums がソート済だったらどうします?
"""