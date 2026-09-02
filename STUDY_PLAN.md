# Exam Rank 05/06 学習計画（日次版）

前提: exam3/exam4は突破済み。5/6の公開情報はなし
(README.mdの通り)。「exam3→4で配列/文字列の基本から木・ヒープ・
グラフ・DPへ難化した」トレンドがそのまま続く想定で、`leetcode/`に
仕込んである NeetCode150（禁止built-inルール適用済み）を主教材にす
る。1ヶ月以上・1日4時間以上を想定し、5週間・35日で全155問+書籍の
該当章+模試をカバーする。

## 進め方（毎日共通）

1. その日のリストを`sorted()` / `.sort()` / `set()` / `heapq` /
   `Counter` / `deque` 禁止で解く
2. `python3 pra/leetcode/<file>.py` を実行し、全ケース `[OK]` を確認
3. `Ans/leetcode/<file>.py` と見比べて、禁止built-inの回避パターン
   を吸収する
4. 詰まった問題は下部の「進捗メモ」に書き足す

1日4時間なら4〜5問+見直しが目安。終わらなければ翌日に持ち越して
良い（復習日・バッファ日で吸収する設計）。

---

## Week 1（Day1-7）: 配列・ハッシュ・二分探索系の基礎を「禁止built-in
モード」で

- [ ] **Day1**: lc001_two_sum / lc217_contains_duplicate /
  lc242_valid_anagram / lc053_maximum_subarray /
  lc349_intersection_of_two_arrays
- [ ] **Day2**: lc003_longest_substring_without_repeating /
  lc128_longest_consecutive_sequence / lc167_two_sum_ii /
  lc392_is_subsequence / lc189_rotate_array
- [ ] **Day3**: lc011_container_with_most_water / lc015_3sum /
  lc125_valid_palindrome / lc567_permutation_in_string /
  lc853_car_fleet
- [ ] **Day4**: lc020_valid_parentheses / lc049_group_anagrams /
  lc739_daily_temperatures / lc042_trapping_rain_water /
  lc271_encode_and_decode_strings
- [ ] **Day5**: lc076_minimum_window_substring /
  lc424_longest_repeating_character_replacement /
  lc238_product_of_array_except_self /
  lc347_top_k_frequent_elements
- [ ] **Day6**（復習日）: Day1〜5で`[NG]`だった問題・時間がかかった
  問題を解き直す
- [ ] **Day7**（書籍+ミニ模試）: Cambridge本 *Character Strings* /
  *Sequences* / *Arrays* / *Sets* を読む → `question/exam3/level1`,
  `level2` を時間を計って解く

---

## Week 2（Day8-14）: 連結リスト・木・ヒープ（exam4 level2が示す弱点
領域）

`heapq`禁止なので、配列ベースの二分ヒープを自力で書けるようにする
のが最優先。

- [ ] **Day8**: lc206_reverse_linked_list /
  lc021_merge_two_sorted_lists / lc141_linked_list_cycle /
  lc226_invert_binary_tree
- [ ] **Day9**: lc143_reorder_list / lc146_lru_cache /
  lc100_same_tree / lc104_maximum_depth_of_binary_tree
- [ ] **Day10**: lc023_merge_k_sorted_lists /
  lc025_reverse_nodes_in_k_group / lc110_balanced_binary_tree /
  lc543_diameter_of_binary_tree
- [ ] **Day11**: lc102_binary_tree_level_order_traversal /
  lc572_subtree_of_another_tree /
  lc098_validate_binary_search_tree /
  lc230_kth_smallest_element_in_a_bst
- [ ] **Day12**: lc235_lowest_common_ancestor_of_a_bst /
  lc199_binary_tree_right_side_view /
  lc1448_count_good_nodes_in_binary_tree /
  lc105_construct_binary_tree_from_preorder_and_inorder
- [ ] **Day13**: lc124_binary_tree_maximum_path_sum /
  lc297_serialize_and_deserialize_binary_tree /
  lc208_implement_trie_prefix_tree /
  lc211_design_add_and_search_words_data_structure
- [ ] **Day14**（ヒープ/デック特訓日）:
  lc212_word_search_ii / lc215_kth_largest_element_in_an_array /
  lc703_kth_largest_element_in_a_stream /
  lc295_find_median_from_data_stream / lc1046_last_stone_weight /
  lc973_k_closest_points_to_origin / lc355_design_twitter /
  lc239_sliding_window_maximium（`deque`禁止での手動実装）

---

## Week 3（Day15-21）: グラフ（exam4 level3 = Course Schedule II の
延長線が本命）

BFS/DFS/トポロジカルソート(Kahn)/Union-Find/簡易Dijkstraを手で書け
るまで反復する。

- [ ] **Day15**: lc200_number_of_islands / lc695_max_area_of_island /
  lc994_rotting_oranges / lc286_walls_and_gates
- [ ] **Day16**: lc133_clone_graph / lc207_course_schedule /
  lc210_course_schedule_ii / lc261_graph_valid_tree
- [ ] **Day17**: lc323_number_of_connected_components /
  lc684_redundant_connection / lc417_pacific_atlantic_water_flow /
  lc130_surrounded_regions
- [ ] **Day18**: lc127_word_ladder / lc269_alien_dictionary /
  lc743_network_delay_time /
  lc787_cheapest_flights_within_k_stops
- [ ] **Day19**: lc778_swim_in_rising_water /
  lc329_longest_increasing_path_in_a_matrix /
  lc332_reconstruct_itinerary /
  lc1584_min_cost_to_connect_all_points
- [ ] **Day20**: lc875_koko_eating_bananas /
  lc287_find_the_duplicate_number / lc252_meeting_rooms /
  lc253_meeting_rooms_ii /
  lc1851_minimum_interval_to_include_each_query /
  lc202_happy_number
- [ ] **Day21**（復習+書籍+ミニ模試）: Cambridge本 *Graphs* /
  *Cycles in Graphs* / *Shortest Paths* を読む →
  `question/exam4/level3` を時間を計って解く

---

## Week 4（Day22-28）: 動的計画法

- [ ] **Day22**: lc070_climbing_stairs /
  lc746_min_cost_climbing_stairs / lc198_house_robber /
  lc213_house_robber_ii / lc121_best_time_to_buy_and_sell_stock
- [ ] **Day23**: lc322_coin_change / lc518_coin_change_ii /
  lc152_maximum_product_subarray /
  lc300_longest_increasing_subsequence
- [ ] **Day24**: lc139_word_break / lc1143_longest_common_subsequence
  / lc416_partition_equal_subset_sum / lc494_target_sum
- [ ] **Day25**: lc091_decode_ways / lc131_palindrome_partitioning /
  lc132_palindrome_partitioning_ii / lc647_palindromic_substrings
- [ ] **Day26**: lc072_edit_distance / lc115_distinct_subsequences /
  lc097_interleaving_string /
  lc153_find_minimum_in_rotated_sorted_array
- [ ] **Day27**:
  lc309_best_time_to_buy_and_sell_stock_with_cooldown /
  lc312_burst_balloons / lc134_gas_station / lc338_counting_bits
- [ ] **Day28**: lc621_task_scheduler /
  lc435_non_overlapping_intervals / lc846_hand_of_straights /
  lc1899_merge_triplets_to_form_target_triplet /
  lc2013_detect_squares / lc678_valid_parenthesis_string /
  lc763_partition_labels

---

## Week 5（Day29-35）: バックトラッキング・二分探索・残り + 総仕上げ
模試

- [ ] **Day29**: lc704_binary_search /
  lc033_search_in_rotated_sorted_array /
  lc074_search_a_2d_matrix / lc007_reverse_integer /
  lc268_missing_number
- [ ] **Day30**: lc078_subsets / lc090_subsets_ii /
  lc046_permutations / lc039_combination_sum /
  lc040_combination_sum_ii
- [ ] **Day31**: lc051_n_queens / lc079_word_search /
  lc036_valid_sudoku / lc054_spiral_matrix / lc048_rotate_image
- [ ] **Day32**: lc055_jump_game / lc056_merge_intervals /
  lc057_insert_interval / lc062_unique_paths /
  lc073_set_matrix_zeroes
- [ ] **Day33**: lc155_min_stack /
  lc150_evaluate_reverse_polish_notation /
  lc084_largest_rectangle_in_histogram / lc136_single_number /
  lc190_reverse_bits / lc191_number_of_1_bits /
  lc371_sum_of_two_integers / lc981_time_based_key_value_store /
  lc138_copy_list_with_random_pointer
- [ ] **Day34**（残り整理日）: lc002_add_two_numbers /
  lc004_median_of_two_sorted_arrays /
  lc005_longest_palindromic_substring /
  lc010_regular_expression_matching /
  lc017_letter_combinations_of_a_phone_number /
  lc019_remove_nth_node_from_end_of_list /
  lc022_generate_parentheses / lc043_multiply_strings /
  lc045_jump_game_ii / lc050_powx_n / lc066_plus_one
- [ ] **Day35**（総仕上げ模試）: `question/exam3/level1〜6` と
  `question/exam4/level1〜3` を通しで時間を計って解く（禁止
  built-in厳守・答えを見ない）。詰まったところだけ翌日以降に復習

---

## 進捗メモ

（弱点だった問題・詰まったパターンをここに書き足していく）
