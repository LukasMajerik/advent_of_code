# https://adventofcode.com/2023/day/10

import os


FILENAME = "data.txt"
# FILENAME = "data_test.txt"

DIRECTIONS = ["l", "u", "r", "d"]

DIRECTIONS_OPPOSITE = {}
DIRECTIONS_OPPOSITE["u"] = "d"
DIRECTIONS_OPPOSITE["d"] = "u"
DIRECTIONS_OPPOSITE["l"] = "r"
DIRECTIONS_OPPOSITE["r"] = "l"

# parameters typing
type Directions = DIRECTIONS

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")


class PointTypes:
    def __init__(self):
        self.types = {}

        dict_ = {}
        dict_.setdefault("u", "N")
        dict_.setdefault("d", "S")
        self.types.setdefault("|", dict_)

        dict_ = {}
        dict_.setdefault("l", "W")
        dict_.setdefault("r", "E")
        self.types.setdefault("-", dict_)

        dict_ = {}
        dict_.setdefault("u", "N")
        dict_.setdefault("r", "E")
        self.types.setdefault("L", dict_)

        dict_ = {}
        dict_.setdefault("u", "N")
        dict_.setdefault("l", "W")
        self.types.setdefault("J", dict_)

        dict_ = {}
        dict_.setdefault("d", "S")
        dict_.setdefault("l", "W")
        self.types.setdefault("7", dict_)

        dict_ = {}
        dict_.setdefault("d", "S")
        dict_.setdefault("r", "E")
        self.types.setdefault("F", dict_)

        dict_ = {}
        dict_.setdefault("u", "N")
        dict_.setdefault("d", "S")
        dict_.setdefault("l", "W")
        dict_.setdefault("r", "E")
        self.types.setdefault("S", dict_)

        dict_ = {}
        self.types.setdefault(".", dict_)

    def _get_type(self, type):
        return self.types.get(type, None)

    def get_type_direc(self, type, direction):
        return self._get_type(type).get(direction, None)


class Point:
    TRAVELABLE = ["|", "-", "L", "J", "7", "F", "S"]
    NON_TRAVELABLE = ["."]
    START = "S"
    ALL = TRAVELABLE + NON_TRAVELABLE

    def __init__(self, value):
        self.visited = "N"
        self.dist_from_start = 0
        self.value = value

    def _get_curr_loc_surr():
        pass

    def __repr__(self):
        return str(self.value)


class PointTypesConnectible:
    def __init__(self):
        self.relat_position_of_pt_to_pt_centre = None
        self.pt_centre = None
        self.pt = None
        self.point_types = PointTypes()

        self.directions_connectible = {}
        self.directions_connectible[("u", "d")] = ("N", "S")
        self.directions_connectible[("d", "u")] = ("S", "N")
        self.directions_connectible[("l", "r")] = ("W", "E")
        self.directions_connectible[("r", "l")] = ("E", "W")

    def is_there_connection(
        self,
        relat_position_of_pt_to_pt_center: DIRECTIONS,
        pt_center: type[Point],
        pt: type[Point],
    ) -> bool:
        direct_from_center, direct_to_center = (
            relat_position_of_pt_to_pt_center,
            DIRECTIONS_OPPOSITE.get(relat_position_of_pt_to_pt_center),
        )
        # print(
        #     "center value:",
        #     pt_center.value,
        #     "to center value:",
        #     pt.value,
        #     "direct_from_center:",
        #     direct_from_center,
        #     "direct_to_center:",
        #     direct_to_center,
        # )

        # print(
        #     "self.point_types.get_type_direc(pt_center.value, direct_from_center):",
        #     self.point_types.get_type_direc(pt_center.value, direct_from_center),
        # )
        # print(
        #     "self.point_types.get_type_direc(pt.value, direct_to_center):",
        #     self.point_types.get_type_direc(pt.value, direct_to_center),
        # )
        # print(
        #     "self.directions_connectible.get(direct_from_center, direct_to_center):",
        #     self.directions_connectible.get((direct_from_center, direct_to_center)),
        # )

        if (
            self.point_types.get_type_direc(pt_center.value, direct_from_center),
            self.point_types.get_type_direc(pt.value, direct_to_center),
        ) == self.directions_connectible.get((direct_from_center, direct_to_center)):
            return True
        return False


class PointMatrix:
    def __init__(self, field_map):
        self.matrix = []
        self.start_pos = None
        self.cur_pos = None
        self.pt = PointTypes()
        self.ptc = PointTypesConnectible()

        for row in field_map:
            row_points = []
            for e in row:
                p = Point(e)
                row_points.append(p)
            self.matrix.append(row_points)

        self.length = len(self.matrix)
        self.width = len(self.matrix[0])

        self.directions_list = ["l", "u", "r", "d"]
        self.directions_diff = {}
        self.directions_diff["u"] = (-1, 0)
        self.directions_diff["d"] = (1, 0)
        self.directions_diff["l"] = (0, -1)
        self.directions_diff["r"] = (0, 1)

    def print_me(self, value=False, dist_from_start=False, visited=False):
        print(
            f"PointMatrix.print_me(value={value}, dist_from_start={dist_from_start}, visited={visited})"
        )

        def get_property(p: Point):
            if value is True:
                return p.value
            elif dist_from_start is True:
                return p.dist_from_start
            elif visited is True:
                return p.visited
            else:
                return p.value

        for row in self.matrix:
            for point in row:
                if dist_from_start:
                    print(f" {int(point.dist_from_start):003d} ", end="")
                else:
                    print(get_property(point), end="")
            print()

    def find_start_pos_and_init(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                # print(self.matrix[i][j])
                point = self.matrix[i][j]
                if point.value == Point.START:
                    self.start_pos = [i, j]
                    point.visited = "Y"
                    point.dist_from_start = 0
                    self.cur_pos = self.start_pos
                    break

    def look_around_and_move(self, pos=None):
        print("look_around_and_move()", 55 * "=")
        if pos:
            self.cur_pos = pos

        moved = False

        cur_pos_i, cur_pos_j = self.cur_pos
        print(
            "central value:",
            self.matrix[cur_pos_i][cur_pos_j],
            "self.cur_pos:",
            self.cur_pos,
        )

        # check left -> up -> right -> down
        for direct in self.directions_list:
            i, j = self.directions_diff.get(direct)
            look_pos = [
                min(self.width - 1, max(0, cur_pos_i + i)),
                min(self.length - 1, max(0, cur_pos_j + j)),
            ]
            look_pos_i, look_pos_j = look_pos
            print(
                "curr_pos_around:",
                look_pos_i,
                look_pos_j,
                self.matrix[look_pos_i][look_pos_j].value,
            )

            if self._is_new_pos_non_vis_and_new_and_connectible(
                direct, [look_pos_i, look_pos_j]
            ):
                self._move(look_pos_i, look_pos_j)
                moved = True
                return moved
        return moved

    def _is_new_pos_non_vis_and_new_and_connectible(self, direct, look_pos):
        # print(f"_is_new_pos_non_vis_and_new_and_connectible({look_pos})")
        cur_pos_i, cur_pos_j = self.cur_pos
        look_pos_i, look_pos_j = look_pos

        if (
            self.cur_pos != look_pos
            and self.matrix[look_pos_i][look_pos_j].visited != "Y"
        ):
            print(
                "checking if there is a way",
                "direct:",
                direct,
                cur_pos_i,
                cur_pos_j,
                self.matrix[cur_pos_i][cur_pos_j],
                look_pos_i,
                look_pos_j,
                self.matrix[look_pos_i][look_pos_j],
            )

            if self.ptc.is_there_connection(
                direct,
                self.matrix[cur_pos_i][cur_pos_j],
                self.matrix[look_pos_i][look_pos_j],
            ):
                print("its connectible")
                return True
        return False

    def _move(self, next_pos_i, next_pos_j):
        cur_pos_i, cur_pos_j = self.cur_pos
        p_c = self.matrix[cur_pos_i][cur_pos_j]
        p_n = self.matrix[next_pos_i][next_pos_j]
        p_n.visited = "Y"
        p_n.dist_from_start = p_c.dist_from_start + 1
        self.cur_pos = [next_pos_i, next_pos_j]

    def traverse_matrix(self):
        cur_pos_i, cur_pos_j = self.cur_pos
        dist_from_start = self.matrix[cur_pos_i][cur_pos_j].dist_from_start

        moved = False

        # do first step in order to avoid condition where start_pos == cur_pos
        if dist_from_start == 0:
            moved = self.look_around_and_move()
        while moved:
            moved = self.look_around_and_move()

    def get_max_dist_from_start(self):
        max = 0
        for row in self.matrix:
            for point in row:
                if point.dist_from_start > max:
                    max = point.dist_from_start
        return max


# pt = PointTypes()
# print(pt._get_type("|"))
# for e in Point.ALL:
#     print(5 * "*", e, pt._get_type(e))
#     for i in DIRECTIONS:
# print(e, pt.get_type_direc(e, i))


# for row in data:
#     print("row in data:", row)

pm = PointMatrix(data)
pm.print_me(visited=True)
pm.find_start_pos_and_init()
print("start is on:", pm.start_pos)
# pm.look_around_and_move()


pm.traverse_matrix()
# pm.cur_pos = [1, 1]
# pm.look_around_and_move([1, 1])

# pm.cur_pos = [1, 1]

# for dir in pm.directions_list:
#     pm.is_there_way(dir)

ptc = PointTypesConnectible()
print(
    "is there conneciton :",
    ptc.is_there_connection("u", pm.matrix[3][1], pm.matrix[2][2]),
)

pm.print_me(value=True)
pm.print_me(visited=True)
# pm.print_me(dist_from_start=True)
# print((pm.get_max_dist_from_start / 2) - 1)
print(((pm.get_max_dist_from_start() - 1) / 2) + 1)
