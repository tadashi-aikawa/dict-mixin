# coding: utf-8

from __future__ import division, absolute_import, unicode_literals

from owlmixin.owlenum import OwlObjectEnum


class Color(OwlObjectEnum):
    RED = (
        "red",
        {"japanese": "赤", "coloring": lambda m: "Red: " + m}
    )

    GREEN = (
        "green",
        {"japanese": "緑", "coloring": lambda m: "Green: " + m}
    )

    BLUE = (
        "blue",
        {"japanese": "青", "coloring": lambda m: "Blue: " + m}
    )

    @property
    def japanese(self):
        return self.object["japanese"]

    def coloring(self, message):
        return self.object["coloring"](message)


class TestFromSymbol:
    def test_normal(self):
        assert Color.from_symbol("blue") is Color.BLUE


class TestProperty:
    def test_normal(self):
        assert Color.BLUE.japanese == "青"


class TestFunction:
    def test_normal(self):
        assert Color.BLUE.coloring("sky") == "Blue: sky"