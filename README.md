# 42_python_exam

Practice repo for 42 School's Exam Rank 05 / 06 under the Python
curriculum, plus the original LeetCode problems that exam3/exam4 turn
out to be reskins of.

---

## English

### Background

No public source documents Exam Rank 05 / 06 for 42's Python-based
curriculum yet. The one unofficial tracker site (42exam.net) is
currently down, and every GitHub repository claiming to cover "exam
rank 05/06" turns out to be leftover material from the old C++
curriculum.

### What's in here

- The problems from my own `exam_rank03_practice-python-` and
  `42_exam_rank04_simulator_python` repos, rewritten to run entirely
  without `sorted()` / `.sort()` / `set()` / `heapq` /
  `Counter`/`deque` — the same constraints the real exam enforces.
- Since exam3/exam4's problems are, more often than not, well-known
  LeetCode problems renamed and lightly reworded, the LeetCode
  problems they appear to be based on are collected separately under
  `leetcode/`, with each exam question file cross-referencing which
  LeetCode problem it's likely adapted from (see the mapping table
  below).
- On top of that, this repo is being extended with the **NeetCode
  150** list, worked the same way (no banned built-ins), on the
  assumption that Rank 5/6 follows the same "reskinned LeetCode"
  pattern as Rank 3/4.

### Directory layout

Subfolders are split by source (`exam3` / `exam4` / `leetcode`).
`exam3` uses `level1`-`level6`, `exam4` uses `level1`-`level3` — these
are two different difficulty scales from two different source repos,
not merged into one numbering.

```
Ans/
  exam3/level1-level6/<problem>.py   # 14 exam3 problems, no banned built-ins
  exam4/level1-level3/<problem>.py   # 7 exam4 problems, same rule
  leetcode/<problem>.py               # LeetCode-sourced problems, same rule
question/
  exam3/level1-level6/<problem>.txt
  exam4/level1-level3/<problem>.txt
  leetcode/<problem>.txt              # "Based on: LeetCode ###. Title" noted
pra/
  exam3/level1-level6/py_<problem>.py
  exam4/level1-level3/py_<problem>.py
  leetcode/py_<problem>.py
  _template.py                         # copy this to start a new problem
```

- **`Ans/`**: solutions. No `sorted()`/`.sort()`/`set()`/`heapq`/
  `Counter`/`deque` anywhere — everything is written out by hand
  (manual sorting, manual hashing via plain `dict`, manual stacks/
  queues via plain `list`).
- **`question/`**: problem statements. exam3/exam4 ones are rewritten
  from the source repos' `Subject/`/`questions/`; `leetcode/` ones are
  paraphrased from LeetCode's problem text (not copied verbatim, for
  copyright reasons) and start with a `Based on: LeetCode ###. Title`
  line.
- **`pra/`**: self-practice stubs. The target function starts as
  `pass`; a `check(label, actual, expected)` helper prints `[OK]`/
  `[NG]` per test case. Copy `pra/_template.py` for new problems.

### Rules for `Ans/`

Treat these as banned the same way the real moulinette bans them:

- `sorted()`, `list.sort()`
- `set()`, set literals
- the `heapq` module
- `collections.Counter`, `collections.deque`
- equivalent standard-library shortcuts (e.g. `itertools` aggregation
  helpers)

Comparison, swapping, searching, and ordering are all written with
plain loops, indexing, and recursion (hand-rolled insertion sort,
linear search, hand-rolled binary heaps, manual hash maps via `dict`,
etc). Note: a `sorted()`/`set()` used purely inside a test's `check()`
call to normalize order-independent output for comparison is fine —
the ban applies to the solution itself, not to test-harness code.

### Using `pra/`

```sh
python3 pra/exam3/level1/py_cryptic_sorter.py
python3 pra/exam4/level2/py_merge_sorted_list.py
python3 pra/leetcode/lc001_two_sum.py
```

Each file is self-contained; implement the function, run it directly,
and confirm every case prints `[OK]`.

### Exam problem to LeetCode mapping

| Source | Problem | Likely LeetCode source | Confidence |
|---|---|---|---|
| exam3/level1 | cryptic_sorter | none found (closest: 179. Largest Number's custom-comparator idea) | low |
| exam3/level1 | inter | 349. Intersection of Two Arrays | medium |
| exam3/level2 | echo_validator | **125. Valid Palindrome** | high |
| exam3/level2 | mirror_matrix | none found (row-reversal is a building block of 48. Rotate Image) | low |
| exam3/level3 | hidenp | **392. Is Subsequence** | high |
| exam3/level3 | number_base_converter | none found (loosely related to 504. Base 7) | low |
| exam3/level3 | pattern_tracker | none found | - |
| exam3/level4 | anagram | **242. Valid Anagram** | high |
| exam3/level4 | shadow_merge | **21. Merge Two Sorted Lists** | high |
| exam3/level4 | string_permutation_checker | **242. Valid Anagram** (case-sensitive variant) | high |
| exam3/level5 | string_sculptor | none found | - |
| exam3/level5 | twist_sequence | **189. Rotate Array** | high |
| exam3/level6 | bracket_validator | **20. Valid Parentheses** | high |
| exam3/level6 | whisper_cipher | none found (loosely related to 2325. Decode the Message) | low |
| exam4/level1 | array_rotation_detector | **796. Rotate String** (array version) | high |
| exam4/level1 | constellation_mapper | none found | - |
| exam4/level1 | list_intersection_finder | **349. Intersection of Two Arrays** (generalized to N lists) | medium |
| exam4/level2 | merge_sorted_list | **23. Merge k Sorted Lists** | high |
| exam4/level2 | palindrome_partitioner | **132. Palindrome Partitioning II** | high |
| exam4/level2 | sliding_window_maximium | **239. Sliding Window Maximum** | high |
| exam4/level3 | package_dependency_resolver | **210. Course Schedule II** (+ the wave tie-break resembles 1203.) | high |

Rows marked "low"/"none found" have no file under `leetcode/` since no
real problem number was found — those aren't guessed or invented.

---

## 日本語

### 背景

42のPythonカリキュラムにおけるExam Rank 05/06の情報は、今のところネット上のどこにも公開されていません。唯一の非公式まとめサイト（42exam.net）は現在ダウンしており、GitHub上で「exam rank 05/06」を名乗るリポジトリは調べる限り全て旧C++カリキュラムの名残でした。

### このリポジトリの中身

- 自分の`exam_rank03_practice-python-`と`42_exam_rank04_simulator_python`にある問題を、本番のexamと同じ制約（`sorted()`/`.sort()`/`set()`/`heapq`/`Counter`/`deque`全面禁止）で解き直したもの。
- exam3/exam4の問題は実態としてLeetCodeの有名問題をリネーム・軽い改変したものであることが多いため、元ネタと思われるLeetCode問題を`leetcode/`に別途収録し、各exam問題のquestionファイルからどのLeetCode問題に対応するかを参照できるようにしてある（下の対応表を参照）。
- それに加えて、Rank5/6もexam3/4と同じ「LeetCodeのリネーム」パターンを踏襲している可能性が高いという想定のもと、**NeetCode 150**のリストも同じ方式（禁止built-inなし）で拡張中。

### ディレクトリ構成

出典（`exam3` / `exam4` / `leetcode`）ごとにサブフォルダを分けている。`exam3`は`level1`〜`level6`、`exam4`は`level1`〜`level3`と、そもそも難易度レベルの基準が別物の2つの出典リポジトリなので、統一のlevel番号にはマージしていない。

```
Ans/
  exam3/level1〜level6/<problem>.py   # exam3の14問。禁止built-inなし
  exam4/level1〜level3/<problem>.py   # exam4の7問。同上
  leetcode/<problem>.py                # LeetCode由来の問題。同上
question/
  exam3/level1〜level6/<problem>.txt
  exam4/level1〜level3/<problem>.txt
  leetcode/<problem>.txt               # 先頭に "Based on: LeetCode ###. Title" を明記
pra/
  exam3/level1〜level6/py_<problem>.py
  exam4/level1〜level3/py_<problem>.py
  leetcode/py_<problem>.py
  _template.py                          # 新しい問題を追加する時はこれをコピー
```

- **`Ans/`**: 解答。`sorted()`/`.sort()`/`set()`/`heapq`/`Counter`/`deque`は一切使わず、全部手で書く（挿入ソート、dictを使った手動ハッシュ、素のlistによるスタック/キューなど）。
- **`question/`**: 問題文。exam3/exam4は元リポジトリの`Subject/`・`questions/`を基にリライトし、`leetcode/`はLeetCodeの文章をそのまま転載せず（著作権配慮）パラフレーズして書いてあり、冒頭に`Based on: LeetCode ###. Title`と明記してある。
- **`pra/`**: 自己練習用スタブ。関数本体は`pass`から始め、`check(label, actual, expected)`で`[OK]`/`[NG]`を出しながら自己採点する。新しい問題を足すときは`pra/_template.py`をコピーする。

### `Ans/`に書くときのルール

本番のmoulinetteが弾くのと同じ扱いで、以下を全面禁止する：

- `sorted()`, `list.sort()`
- `set()`, setリテラル
- `heapq`モジュール
- `collections.Counter`, `collections.deque`
- 上記に相当する標準ライブラリの糖衣構文（`itertools`の集約系関数など）

比較・交換・探索・整列はすべて素のループ・インデックス操作・再帰で書く（挿入ソート、線形探索、手書き二分ヒープ、dictによる手動ハッシュマップなど）。なお、出力の順序が問われない問題で`check()`呼び出し側（テストコード側）が比較のために`sorted()`/`set()`を使うのは問題ない。禁止対象はあくまで解答（Ans）そのものであり、テストハーネス側のコードではない。

### `pra/`の使い方

```sh
python3 pra/exam3/level1/py_cryptic_sorter.py
python3 pra/exam4/level2/py_merge_sorted_list.py
python3 pra/leetcode/lc001_two_sum.py
```

各ファイルは自己完結型。関数を実装して直接実行し、全ケースで`[OK]`が出ることを確認する。

### exam問題 ⇔ 元ネタLeetCode 対応表

| 出典 | 問題 | 対応するLeetCode | 確信度 |
|---|---|---|---|
| exam3/level1 | cryptic_sorter | 対応なし（近いのは179. Largest Numberの発想） | 低 |
| exam3/level1 | inter | 349. Intersection of Two Arrays | 中 |
| exam3/level2 | echo_validator | **125. Valid Palindrome** | 高 |
| exam3/level2 | mirror_matrix | 対応なし（48. Rotate Imageの部品に近い） | 低 |
| exam3/level3 | hidenp | **392. Is Subsequence** | 高 |
| exam3/level3 | number_base_converter | 対応なし（504. Base 7を汎用化した発想） | 低 |
| exam3/level3 | pattern_tracker | 対応なし | - |
| exam3/level4 | anagram | **242. Valid Anagram** | 高 |
| exam3/level4 | shadow_merge | **21. Merge Two Sorted Lists** | 高 |
| exam3/level4 | string_permutation_checker | **242. Valid Anagram**（大文字小文字区別版） | 高 |
| exam3/level5 | string_sculptor | 対応なし | - |
| exam3/level5 | twist_sequence | **189. Rotate Array** | 高 |
| exam3/level6 | bracket_validator | **20. Valid Parentheses** | 高 |
| exam3/level6 | whisper_cipher | 対応なし（2325. Decode the Messageに近い発想） | 低 |
| exam4/level1 | array_rotation_detector | **796. Rotate String**（配列版） | 高 |
| exam4/level1 | constellation_mapper | 対応なし | - |
| exam4/level1 | list_intersection_finder | **349. Intersection of Two Arrays**（複数リストに一般化） | 中 |
| exam4/level2 | merge_sorted_list | **23. Merge k Sorted Lists** | 高 |
| exam4/level2 | palindrome_partitioner | **132. Palindrome Partitioning II** | 高 |
| exam4/level2 | sliding_window_maximium | **239. Sliding Window Maximum** | 高 |
| exam4/level3 | package_dependency_resolver | **210. Course Schedule II**（+ 波ごとのタイブレークが1203.に近い） | 高 |

「確信度: 低」「対応なし」の問題はLeetCodeに直接の元ネタが見当たらなかったもの。存在しない問題番号は書いていないので、`leetcode/`フォルダにはこれら対応なしの問題は収録していない。
