# 42_python_exam

## Why this repo exists

No public source documents Exam Rank 05 / 06 for 42's Python-based
curriculum yet. The one unofficial tracker site (42exam.net) is
currently down, and every GitHub repository claiming to cover "exam
rank 05/06" turns out to be leftover material from the old C++
curriculum. Rather than wait for that information to show up, the plan
here is simple: get good enough to solve **every algorithm in this
repository** — the actual exam3/exam4 problems, plus the original
LeetCode problems they were reskinned from — entirely under the real
exam's constraints (no `sorted()`, no `set()`, no `heapq`, no
`Counter`/`deque`). Exam 3 and 4 both turned out to be renamed LeetCode
problems; if Rank 5/6 follows the same pattern, this should be enough
prep regardless of what the exact problems end up being.

If you're a 42 student who landed here searching for Exam Rank 05/06
Python material and found nothing else either — same boat. Feel free to
open an issue/PR if you find real information.

## なぜこのリポジトリを作ったか

42のPythonカリキュラムにおけるExam Rank 05/06の情報は、今のところネット上のどこにも公開されていません。唯一の非公式まとめサイト（42exam.net）は現在ダウンしており、GitHub上で「exam rank 05/06」を名乗るリポジトリは調べる限り全て旧C++カリキュラムの名残でした。情報が出回るのを待つのではなく、方針はシンプルにする：**このリポジトリにある問題を全部解けるようになる**——exam3/exam4本体の問題に加えて、その元ネタと思われるLeetCode問題も含めて、全部を本番のexam同様の制約（`sorted()`禁止・`set()`禁止・`heapq`禁止・`Counter`/`deque`禁止）で解けるようにする。exam3もexam4も実態はLeetCodeのリネーム問題だったので、Rank5/6も同じパターンを踏襲しているなら、具体的な出題内容が分からなくてもこれで十分な対策になるはず。

同じようにExam Rank 05/06のPython版情報を探してここに辿り着いた42生がいたら、境遇は同じです。本物の情報を見つけたらissue/PRで教えてください。

---

Exam Rank 05 / 06 対策用のリポジトリ。42のPythonイグザムでは `sorted()` / `.sort()` / `set` / `heapq` などの「便利メソッド」が軒並み禁止されるため、`exam_rank03_practice-python-` や `42_exam_rank04_simulator_python`（[anju0618](https://github.com/anju0618)）で使っていた問題を、**全部自前実装で解けるように**練習し直すためのもの。

Rank5/6自体の公式・非公式の問題情報が現状ネット上に存在しない（42exam.netがダウン中、GitHub上のrank05/06系リポジトリは全部旧C++カリキュラムのもの）ため、当面はexam3/4の問題を「禁止built-inなし」で解き直す形で練習する。加えて、exam3/4の各問題は元々LeetCodeの有名問題のリネーム・改変であることが多いため、**元ネタと思われるLeetCode問題も`leetcode/`に別途収録**し、どのexam問題がどのLeetCode問題に対応するか分かるようにしてある。

## ディレクトリ構成

出典（exam3 / exam4 / leetcode）ごとにサブフォルダを分けている。exam3は`Level1`〜`Level6`、exam4は`level1`〜`level3`と、そもそも難易度レベルの基準が別物なので統一のlevel番号にはマージしていない。

```
Ans/
  exam3/level1〜level6/<problem>.py   # exam3の14問。Ans_normalスタイル固定
  exam4/level1〜level3/<problem>.py   # exam4の7問。同上
  leetcode/<problem>.py                # 元ネタLeetCode問題。同じ制約で統一
question/
  exam3/level1〜level6/<problem>.txt
  exam4/level1〜level3/<problem>.txt
  leetcode/<problem>.txt               # "Based on: LeetCode ###. Title" を明記
pra/
  exam3/level1〜level6/py_<problem>.py
  exam4/level1〜level3/py_<problem>.py
  leetcode/py_<problem>.py
  _template.py                          # 新しい問題を追加する時のひな形
```

- **`Ans/`**: 解答。`Ans_normal`スタイル固定 ＝ `sorted()` / `.sort()` / `set` / `heapq` などの「魔法の1行」に頼らず、処理を手で書き下す。
- **`question/`**: 問題文。exam3/exam4は元リポジトリの`Subject/`・`questions/`を基にリライトし、末尾に対応するLeetCode問題への `Similar to (probably): ...` 行を追加してある（確信が持てないものは正直に「対応なし」と書いてある）。`leetcode/`側の問題文はLeetCode公式の文章を転載せず、パラフレーズして書いてある。
- **`pra/`**: 自己練習用のスタブファイル。関数本体は `pass` から始め、`check(label, actual, expected)` で自己採点しながら解く。`pra/_template.py` をコピーして使う。

## ルール（Ans/に書くときの制約）

以下は全面禁止。使った場合、本番のmoulinetteで弾かれるものとして扱う（`leetcode/`のAnsも同じ制約で統一している）。

- `sorted()`, `list.sort()`
- `set()`, `set` リテラル
- `heapq` モジュール全般
- `collections.Counter` / `collections.deque` などの標準ライブラリの「便利データ構造」
- 上記に相当する標準ライブラリの糖衣構文全般（`itertools` の集約系関数なども含む）

比較・交換・探索・整列はすべて素のループ・インデックス操作・再帰で書く（挿入ソート、線形探索、手書きKahnのアルゴリズムなど）。

## pra/ の使い方

```sh
python3 pra/exam3/level1/py_cryptic_sorter.py
python3 pra/exam4/level2/py_merge_sorted_list.py
python3 pra/leetcode/lc020_valid_parentheses.py
```

各ファイルは自己完結型で、`if __name__ == "__main__":` にテストケースが並んでいる。実装したら直接実行して `[OK]` が並ぶか確認する。

## exam問題 ⇔ 元ネタLeetCode 対応表

| 出典 | 問題 | 対応するLeetCode | 確信度 |
|---|---|---|---|
| exam3/level1 | cryptic_sorter | 対応なし（近いのは179. Largest Number の発想） | 低（参考程度） |
| exam3/level1 | inter | 349. Intersection of Two Arrays | 中 |
| exam3/level2 | echo_validator | **125. Valid Palindrome** | 高 |
| exam3/level2 | mirror_matrix | 対応なし（48. Rotate Imageの部品に近い） | 低（参考程度） |
| exam3/level3 | hidenp | **392. Is Subsequence** | 高 |
| exam3/level3 | number_base_converter | 対応なし（504. Base 7を汎用化した発想） | 低（参考程度） |
| exam3/level3 | pattern_tracker | 対応なし | - |
| exam3/level4 | anagram | **242. Valid Anagram** | 高 |
| exam3/level4 | shadow_merge | **21. Merge Two Sorted Lists** | 高 |
| exam3/level4 | string_permutation_checker | **242. Valid Anagram**（大文字小文字区別版） | 高 |
| exam3/level5 | string_sculptor | 対応なし | - |
| exam3/level5 | twist_sequence | **189. Rotate Array** | 高 |
| exam3/level6 | bracket_validator | **20. Valid Parentheses** | 高 |
| exam3/level6 | whisper_cipher | 対応なし（2325. Decode the Messageに近い発想） | 低（参考程度） |
| exam4/level1 | array_rotation_detector | **796. Rotate String**（配列版） | 高 |
| exam4/level1 | constellation_mapper | 対応なし | - |
| exam4/level1 | list_intersection_finder | **349. Intersection of Two Arrays**（複数リストに一般化） | 中 |
| exam4/level2 | merge_sorted_list | **23. Merge k Sorted Lists** | 高 |
| exam4/level2 | palindrome_partitioner | **132. Palindrome Partitioning II** | 高 |
| exam4/level2 | sliding_window_maximium | **239. Sliding Window Maximum** | 高 |
| exam4/level3 | package_dependency_resolver | **210. Course Schedule II**（+ 波ごとのタイブレークが1203.に近い） | 高 |

「確信度: 低」の問題はLeetCodeに直接の元ネタが見当たらなかったもの。存在しない問題番号は書いていないので、`leetcode/`フォルダにはこれら対応なしの問題は収録していない。
