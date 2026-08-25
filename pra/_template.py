"""
pra/level<N>/py_<problem_name>.py 用テンプレート。
コピーしてファイル名を変え、関数名・シグネチャをquestion/level<N>/の問題文に合わせて書き換える。

制約: sorted(), .sort(), set(), heapq, collections.Counter/deque などは使用禁止。
      Ans/に書くのと同じ「手書き実装」ルールで解くこと。
"""


def problem_name(arg1, arg2=None):
    # TODO: 実装する。sorted()/set()/heapq などは使わない。
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    # question/level<N>/py_problem_name の Examples をそのまま貼り付ける
    check("example 1", problem_name(...), ...)
    check("example 2", problem_name(...), ...)
