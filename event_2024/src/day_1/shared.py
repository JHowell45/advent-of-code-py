from __future__ import annotations

from collections import defaultdict

from pydantic import BaseModel


class LocationSearch(BaseModel):
    left: list[int]
    right: list[int]

    @classmethod
    def new(cls) -> LocationSearch:
        return LocationSearch(left=[0] * 1000, right=[0] * 1000)

    @classmethod
    def parse_locations(cls, data: str) -> LocationSearch:
        instance = LocationSearch(left=[0] * 1000, right=[0] * 1000)
        for index, line in enumerate(data.splitlines()):
            left, right = line.split("   ")
            instance.add_left(index, int(left))
            instance.add_right(index, int(right))

        return instance

    def add_left(self, index: int, value: int):
        self.left[index] = value

    def add_right(self, index: int, value: int):
        self.right[index] = value

    def add_location_pair(self, index: int, line: str):
        left, right = line.split("   ")
        self.add_left(index, int(left))
        self.add_right(index, int(right))

    def total_distance(self) -> int:
        distance = 0
        self.left.sort()
        self.right.sort()
        for left, right in zip(self.left, self.right):
            distance += abs(left - right)
        return distance

    def similarity_score(self) -> int:
        score: int = 0
        lookup = defaultdict(int)
        for v in self.right:
            lookup[v] += 1

        for v in self.left:
            score += v * lookup[v] or 0
        return score
