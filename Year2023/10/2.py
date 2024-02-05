# https://adventofcode.com/2023/day/10

import os


FILENAME = "data.txt"
# FILENAME = "data_test.txt"

DIRECTIONS = ["l", "u", "r", "d"]
POINT_DISTANCE_NONE = "xxx"

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
        self.dist_from_start = POINT_DISTANCE_NONE
        self.value = value
        self.within_loop = None

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
        self.max_ = None
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

    def print_me(
        self, value=False, dist_from_start=False, visited=False, within_loop=False
    ):
        print(
            f"PointMatrix.print_me(value={value}, dist_from_start={dist_from_start}, visited={visited}, within_loop={within_loop})"
        )

        def get_property(p: Point):
            if value is True:
                return p.value
            elif dist_from_start is True:
                return p.dist_from_start
            elif visited is True:
                return p.visited
            elif within_loop:
                return p.within_loop
            else:
                return p.value

        for row in self.matrix:
            for point in row:
                if dist_from_start:
                    dfs = point.dist_from_start
                    if dfs == POINT_DISTANCE_NONE:
                        print(f" {dfs} ", end="")
                    else:
                        print(f" {dfs:003d} ", end="")
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
        # print("look_around_and_move()", 55 * "=")
        if pos:
            self.cur_pos = pos

        moved = False

        cur_pos_i, cur_pos_j = self.cur_pos
        # print(
        #     "central value:",
        #     self.matrix[cur_pos_i][cur_pos_j],
        #     "self.cur_pos:",
        #     self.cur_pos,
        # )

        # check left -> up -> right -> down
        for direct in self.directions_list:
            i, j = self.directions_diff.get(direct)
            look_pos = [
                min(self.length - 1, max(0, cur_pos_i + i)),
                min(self.width - 1, max(0, cur_pos_j + j)),
            ]
            look_pos_i, look_pos_j = look_pos
            # print(
            #     "direction:",
            #     direct,
            #     "curr_pos_around:",
            #     look_pos_i,
            #     look_pos_j,
            #     self.matrix[look_pos_i][look_pos_j].value,
            # )

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
            # print(
            #     "  checking if there is a way",
            #     "direct:",
            #     direct,
            #     cur_pos_i,
            #     cur_pos_j,
            #     self.matrix[cur_pos_i][cur_pos_j],
            #     look_pos_i,
            #     look_pos_j,
            #     self.matrix[look_pos_i][look_pos_j],
            # )

            if self.ptc.is_there_connection(
                direct,
                self.matrix[cur_pos_i][cur_pos_j],
                self.matrix[look_pos_i][look_pos_j],
            ):
                # print("its connectible")
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
        if self.max_:
            return self.max_
        max_ = 0
        for row in self.matrix:
            for point in row:
                if (
                    isinstance(point.dist_from_start, int)
                    and point.dist_from_start > max_
                ):
                    max_ = point.dist_from_start

        self.max_ = max_
        return self.max_

    def are_points_chain(self, pos1, pos2):
        p1 = self.matrix[pos1[0]][pos1[1]]
        p2 = self.matrix[pos2[0]][pos2[1]]

        # print(
        #     "are_points_chain()",
        #     "pos1:",
        #     pos1,
        #     "pos1 dist_from_start:",
        #     p1.dist_from_start,
        #     "pos2:",
        #     pos2,
        #     "pos2 dist_from_start:",
        #     p2.dist_from_start,
        # )

        if isinstance(p1.dist_from_start, str) or isinstance(p2.dist_from_start, str):
            return False

        if (
            abs(p1.dist_from_start - p2.dist_from_start)
            == self.get_max_dist_from_start()
        ):
            return True

        if abs(p1.dist_from_start - p2.dist_from_start) == 1:
            return True

        return False


class Node:
    def __init__(self, y, x):
        self.done = False
        self.road = None
        y1, y2 = y
        x1, x2 = x
        self.position = ((y1, y2), (x1, x2))

    def look_around(self):
        # print("Look around")
        i, j = self.position
        i1, j1 = i
        i2, j2 = j

        edges = []

        look_left = ((i1, i2), (j1, i2))
        look_up = ((i1, i2), (i1, j2))
        look_right = ((i1, j2), (j1, j2))
        look_down = ((j1, i2), (j1, j2))

        look_directions = [look_left, look_up, look_right, look_down]
        look_directions_names = ["l", "u", "r", "d"]

        for m in range(len(look_directions)):
            k, l = look_directions[m]

            edge = k, l
            # print(
            #     "position:",
            #     self.position,
            #     "direction:",
            #     look_directions_names[m],
            #     "resulting edge:",
            #     edge,
            # )
            edges.append(edge)
        return edges

    def __repr__(self):
        return f"Node(self.done={self.done}, self.road={self.road}, self.position={self.position})"


class Nodes:
    def __init__(self, field_map):
        self.length = len(field_map) - 1
        self.width = len(field_map[0]) - 1
        self.nodes = []

        for j in range(self.length):
            row = []
            for i in range(self.width):
                row.append(Node((j, j + 1), (i, i + 1)))
            self.nodes.append(row)

    def __repr__(self):
        return f"Node(self.nodes={self.nodes})"

    def print_me(self, done=False, road=False):
        if done:
            print("Nodes.print_me(done=True)")
        elif road:
            print("Nodes.print_me(road=True)")
        else:
            print("Nodes.print_me()")

        for row in self.nodes:
            for n in row:
                if done:
                    print_val = n.done
                elif road:
                    print_val = n.road
                else:
                    print_val = n.position
                print(f"{str(print_val):<5}   ", end="")
            print()

    def is_it_outside_edge(self, edge):
        p1, p2 = edge
        i1, j1 = p1
        i2, j2 = p2
        coordinates_i = [i1, i2]
        coordinates_j = [j1, j2]
        # print(
        #     "Node.is_it_outside_edge()",
        #     "edge:",
        #     edge,
        #     "length:",
        #     self.length,
        #     "width:",
        #     self.width,
        #     "coor_i:",
        #     coordinates_i,
        #     "coor_j:",
        #     coordinates_j,
        # )

        if i1 == i2 and (i1 in [0, self.length]):
            return True

        if j1 == j2 and (j1 in [0, self.width]):
            return True

        return False

    def look_around_node_pos(self, node_pos):
        cur_pos_i, cur_pos_j = node_pos
        look_positions = []

        directions_list = ["l", "u", "r", "d"]
        directions_diff = {}
        directions_diff["u"] = (-1, 0)
        directions_diff["d"] = (1, 0)
        directions_diff["l"] = (0, -1)
        directions_diff["r"] = (0, 1)

        print(self.length - 1, self.width - 1)

        for direct in directions_list:
            i, j = directions_diff.get(direct)
            look_pos = [
                min(self.length - 1, max(0, cur_pos_i + i)),
                min(self.width - 1, max(0, cur_pos_j + j)),
            ]
            look_positions.append(look_pos)

        return look_positions


class Solution:
    def __init__(self, field_map):
        self.ns = Nodes(field_map)
        self.ns.print_me()
        self.pm = PointMatrix(field_map)

        self.pm.find_start_pos_and_init()
        self.pm.traverse_matrix()
        self.pm.print_me(value=True)
        self.pm.print_me(visited=True)
        self.pm.print_me(dist_from_start=True)

    def _find_undone_node_on_road(self):
        for i, node_row in enumerate(self.ns.nodes):
            for j, node in enumerate(node_row):
                if node.done is False and node.road is True:
                    return i, j

    def grow_road_around_node(self, node_pos):
        print(f"Solution.grow_road_around_node(node_pos={node_pos})")
        i, j = node_pos

        for node_arround_pos in self.ns.look_around_node_pos(node_pos):
            m, n = node_arround_pos
            point_positions = self.get_point_pos_between_nodes(
                self.ns.nodes[m][n], self.ns.nodes[i][j]
            )
            if not self.pm.are_points_chain(point_positions[0], point_positions[1]):
                print(f"self.ns.nodes[{m}][{n}].road = True")
                self.ns.nodes[m][n].road = True
        print(f"self.ns.nodes[{i}][{j}].done = True")
        self.ns.nodes[i][j].done = True

    def grow_roads(self):
        while node_pos := self._find_undone_node_on_road():
            self.grow_road_around_node(node_pos)

    def find_points_within_loop(self):
        print("Solution.find_points_within_loop()")
        anchor = 0, 0
        anchor_r = 0, 1
        anchor_d = 1, 0
        anchor_diagonal = 1, 1

        square = [anchor, anchor_r, anchor_d, anchor_diagonal]

        are_they_roads = []

        for i in range(self.ns.length - 1):
            for j in range(self.ns.width - 1):
                print(i, j, self.ns.nodes[i][j].position)
                are_they_roads = []
                for m, n in square:
                    are_they_roads.append(self.ns.nodes[i + m][j + n].road)
                print(
                    "are_they_roads:",
                    are_they_roads,
                    "not any(are_they_roads)",
                    not any(are_they_roads),
                )
                if not any(are_they_roads):
                    x, y = self.ns.nodes[i][j].position
                    self.pm.matrix[x[1]][y[1]].within_loop = True

    def sum_points_within_loop(self):
        sum = 0
        for row in self.pm.matrix:
            for point in row:
                if point.within_loop:
                    sum += 1

        return sum

    def _init_outside_edge_nodes(self):
        def _init_outside_edge_nodes_inter(self, edge, node):
            # print(
            #     f"self.ns.is_it_outside_edge({edge}):",
            #     self.ns.is_it_outside_edge(edge),
            #     f"self.pm.are_points_chain({edge[0]}, {edge[1]})",
            #     self.pm.are_points_chain(edge[0], edge[1]),
            # )
            if self.ns.is_it_outside_edge(edge) and not (
                self.pm.are_points_chain(edge[0], edge[1])
            ):
                # print("_init_outside_edge_nodes()", "road=True")
                node.road = True

        print("init top row", 88 * "=")
        for node in self.ns.nodes[0]:
            for edge in node.look_around():
                _init_outside_edge_nodes_inter(self, edge, node)

        print("init last row", 88 * "=")
        for node in self.ns.nodes[-1]:
            for edge in node.look_around():
                _init_outside_edge_nodes_inter(self, edge, node)

        print("init left column", 88 * "=")
        for row in self.ns.nodes:
            for edge in row[0].look_around():
                _init_outside_edge_nodes_inter(self, edge, row[0])

        print("init last column", 88 * "=")
        for row in self.ns.nodes:
            for edge in row[-1].look_around():
                _init_outside_edge_nodes_inter(self, edge, row[-1])

    def get_point_pos_between_nodes(self, node1, node2):
        y1, x1 = node1.position
        y2, x2 = node2.position

        y11, y12 = y1
        y21, y22 = y2
        y_all = y11, y12, y21, y22
        y_inbetween = int(sum(y_all) / len(y_all))

        x11, x12 = x1
        x21, x22 = x2
        x_all = [x11, x12, x21, x22]
        x_inbetween = int(sum(x_all) / len(x_all))

        if y1 != y2:
            point1_pos = y_inbetween, x11
            point2_pos = y_inbetween, x12
        else:
            point1_pos = y11, x_inbetween
            point2_pos = y12, x_inbetween

        return point1_pos, point2_pos


# for row in data:
#     print("row in data:", row)


s = Solution(data)
# print("are they chain:", s.pm.are_points_chain((1, 1), (0, 1)))
# print(((s.pm.get_max_dist_from_start() - 1) / 2) + 1)

s._init_outside_edge_nodes()
s.grow_roads()
# s.ns.print_me()
s.ns.print_me(road=True)
s.ns.print_me(done=True)
s.find_points_within_loop()
s.pm.print_me(within_loop=True)
print("sum:", s.sum_points_within_loop())
