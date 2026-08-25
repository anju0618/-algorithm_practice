class DetectSquares:
    def __init__(self):
        self.counts = {}  # (x, y) -> 出現回数
        self.points = []  # 一度でも追加された座標（重複は含まない）

    def add(self, point: list[int]) -> None:
        key = (point[0], point[1])
        if key not in self.counts:
            self.points.append(key)
        self.counts[key] = self.counts.get(key, 0) + 1

    def count(self, point: list[int]) -> int:
        px, py = point
        total = 0

        for x, y in self.points:
            if y != py or x == px:
                continue
            side = x - px
            c_xy = self.counts[(x, y)]
            # 正方形は上側・下側の2通りありうる
            for new_y in (py + side, py - side):
                c1 = self.counts.get((px, new_y), 0)
                c2 = self.counts.get((x, new_y), 0)
                total += c_xy * c1 * c2

        return total
