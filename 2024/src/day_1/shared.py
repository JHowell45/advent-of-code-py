from __future__ import annotations

from pydantic import BaseModel


class LocationSearch(BaseModel):
    left: list[int]
    right: list[int]

    def add_left(self, index: int, value: int):
        self.left[index] = value

    def add_right(self, index: int, value: int):
        self.right[index] = value

    @classmethod
    def parse_locations(cls, data: str) -> LocationSearch:
        instance = LocationSearch(left=[0] * 1000, right=[0] * 1000)
        for index, line in enumerate(data.splitlines()):
            left, right = line.split("   ")
            instance.add_left(index, int(left))
            instance.add_right(index, int(right))

        return instance
