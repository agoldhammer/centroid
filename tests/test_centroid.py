from centroid.centroid import Point
from math import sqrt


def test_point():
    p1 = Point('p1', 1, 1)
    p2 = Point('p2', 0, 0)
    assert(p1.dist(p2) == sqrt(2))
