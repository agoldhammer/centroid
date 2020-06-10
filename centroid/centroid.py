from dataclasses import dataclass
from math import sqrt
from itertools import combinations


@dataclass
class Point:
    name: str
    x: float
    y: float

    def dist(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


@dataclass
class Triangle:
    name: str
    v1: Point
    v2: Point
    v3: Point

    def centroid(self):
        "compute the centroid of the triangle"
        return Point('Centroid:'+self.name,
                     (self.v1.x + self.v2.x + self.v3.x)/3,
                     (self.v1.y + self.v2.y + self.v3.y)/3)

    def index(self):
        """
        compute the coalition index of a triangle by summing distances
        from centroid to each vertex
        """
        cen = self.centroid()
        return cen.dist(self.v1) + cen.dist(self.v2) + cen.dist(self.v3)


def make_groups(country):
    "given country data, group by triplets"
    return combinations(country, 3)


def make_coalition(groups):
    "make coalition triangle out of 3-tuple of members"
    grp1, grp2, grp3 = groups
    coalition_name = grp1.name + '+' + grp2.name + '+' + grp3.name
    return Triangle(coalition_name, grp1, grp2, grp3)


france1990 = ("France 1990",
              [Point("M", 0.6, -0.63),
               Point("P", 0.22, 0.25),
               Point("SS", 0.03, -0.12),
               Point("LS", -0.08, -0.40),
               Point("SM", 0.03, -0.60),
               Point("LM", -0.08, -0.76),
               Point("SE", 0.28, -0.76)])

france2006 = ("France 2006",
              [Point("M", 0.36, -0.50),
               Point("P", -0.31, 0.18),
               Point("SS", -0.22, 0.29),
               Point("LS", -0.37, -0.04),
               Point("SM", -0.34, -0.25),
               Point("LM", -0.44, -0.27),
               Point("SE", -0.08, -0.31)])

france2018 = ("France 2018",
              [Point("M", 0.43, 0.60),
               Point("P", -0.13, 0.89),
               Point("SS", -0.04, 0.55),
               Point("LS", -0.19, 0.47),
               Point("SM", -0.20, 0.26),
               Point("LM", -0.27, 0.12),
               Point("SE", 0.04, 0.00)])


def process_data(data_groups):
    for data_group in data_groups:
        name, data = data_group
        print(name + '\n-----------')
        coalitions = []  # initialize list of coalitions
        for grp in make_groups(data):
            # represent each group as a coalition (triangle)
            co = make_coalition(grp)
            # for each coalition co, compute index and append to coalition list
            coalitions.append((co.name, co.index()))
        # sort the coalitions by index
        coalitions.sort(key=lambda x: x[1])
        for name, index in coalitions:
            print(f'{name}: {index}')
        print('**')


if __name__ == "__main__":
    process_data([france1990, france2006, france2018])
