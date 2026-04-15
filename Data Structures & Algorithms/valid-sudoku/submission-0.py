class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        空のマス-> "."
        数字はintではなくstr で格納されている
        index: 0 -> 8
        board[r][c] -> r_set, c_set, subbox_set
        r_sets[r] -> set()
        c_serts[c] -> set()
        subbox_set[r][c] -> 
            あまりで決まるはず｡
            [0][0] [0][3] [0][6]
            [3][0] [3][3] [6][3]
            [6][0] [6][3] [6][6]
            -> [0][0] [0][1] [0][2]
            -> [1,0] [1,1] [2,1]
            -> [2,0] [2,1] [2,2]
        
        考え方:
        マスを1マスずつ見ていって､r_sets, c_sets, subboc_sets に重複があるか判定
        重複があればその場でFalseする
        重複が見つからなければTrueを返す
        """
        ROW_COUNT = len(board)
        COLUMN_COUNT = len(board[0])
        # assert(ROW_COUNT == COLUMN_COUNT)
        # 出現数値を記録していくsetを用意する
        r_sets = [set() for _ in range(9)]
        c_sets = [set() for _ in range(9)]
        subbox_sets = [[set() for _ in range(3)] for _ in range(3)]
        # r_sets[0].add(1)
        # print(r_sets)
        # print(subbox_sets)
        # 重複検知
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                cell_num = board[r][c]
                # . は空
                if cell_num == ".":
                    continue
                print(f"before: {subbox_sets=}")
                # "数字"のときの重複検知処理
                # assert cell_num  in "123456789"
                if cell_num in r_sets[r] \
                  or cell_num in c_sets[c] \
                  or cell_num in subbox_sets[r//3][c//3]:
                  return False
                r_sets[r].add(cell_num)
                c_sets[c].add(cell_num)
                subbox_sets[r//3][c//3].add(cell_num)
                print(f"after: {subbox_sets=}")
        return True

"""
setの初期化｡空set()を出力すると､{}, () ではなく set() で出力される!
```
[{1}, set(), set(), set(), set(), set(), set(), set(), set()]
[[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
```

if の 条件が長いときの \ ｡

print デバッグ

// と % 
商を見たい､あまりを見たい

array[float] のときに出るエラーってなんだっけ?
"""