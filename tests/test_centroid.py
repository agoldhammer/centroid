from centroid.centroid import Point, Triangle
from math import sqrt


def test_dist():
    p1 = Point('p1', 1, 1)
    p2 = Point('p2', 0, 0)
    assert(p1.dist(p2) == sqrt(2))
    p1 = Point('p1', 0, 2)
    assert(p1.dist(p2) == 2)
    p2 = Point('p2', 1, 0)
    assert(p2.dist(p1) == sqrt(5))


def test_centroid():
    p1 = Point('p1', 0, 0)
    p2 = Point('p2', 1, 0)
    p3 = Point('p3', 0, 1)
    t1 = Triangle('t1', p1, p2, p3)
    assert(t1.centroid() == Point('Centroid:t1', 1/3, 1/3))


def test_index():
    p1 = Point('p1', 0, 0)
    p2 = Point('p2', 1, 3)
    p3 = Point('p3', 2, 0)
    t1 = Triangle('t1', p1, p2, p3)
    assert(t1.centroid() == Point('Centroid:t1', 1, 1))
    assert(t1.index() == 2*sqrt(2) + 2)
