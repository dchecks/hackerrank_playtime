class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.l_node = None
        self.r_node = None
        self.value = value

class BST:
    def __init__(self):
        self.head = None
        self.nums = []

    def rec_insert(self, parent, num):
        if parent.value > num:
            if parent.l_node is None:
                parent.l_node = Node(parent, num)
                self.nums.append(num)
            else:
                self.rec_insert(parent.l_node, num)
        elif parent.value < num:
            if parent.r_node is None:
                parent.r_node = Node(parent, num)
                self.nums.append(num)
            else:
                self.rec_insert(parent.r_node, num)
        else:
            raise RuntimeError("Duplicate value exception")

    def insert(self, num):
        if self.head is None:
            self.head = Node(None, num)
            self.nums.append(num)
        else:
            self.rec_insert(self.head, num)

    def locate(self, num, collect):
        parent = collect[-1]
        if num == parent.value:
            # Will already have collected the current value
            return collect
        elif num < parent.value:
            collect.append(parent.l_node)
            return self.locate(num, collect)
        elif num > parent.value:
            collect.append(parent.r_node)
            return self.locate(num, collect)

    def sum_distances(self):
        if len(self.nums) == 2:
            return 1
        pairs = [(x,y) for x in sorted(self.nums)
                 for y in sorted(self.nums)]
        #print(self.nums)
        #print(pairs)
        pair_sub = [p for p in pairs if p[0] < p[1]] # TODO Condense
        #print(pair_sub)
        sum = 0

        for x, y in pair_sub:
            collect_x = self.locate(x, [self.head])
            collect_y = self.locate(y, [self.head])
            #print("Collects:\n%s\n%s" % ([x.value for x in collect_x], [y.value for y in collect_y]))

            cs = 0
            cs_range = min(len(collect_x), len(collect_y))
            #print(cs_range)
            for i in range(cs_range):
                if collect_x[i] == collect_y[i]:
                    cs = i
                else:
                    break
            #print(cs)
            #print("Collect subtree:\nx: %s\ny: %s" % ([x.value for x in collect_x[cs:]], [y.value for y in collect_y[cs:]]))
            len_x = len(collect_x[cs:]) - 1
            len_y = len(collect_y[cs:]) - 1

            totez = len_x + len_y
            #print("Totez: %s" % totez)
            sum += totez

        return sum


def solve(arr):
    totals = []
    if not len(arr):
        return []
    if len(arr) == 1:
        return [0]
    bst = BST()

    for num in arr:
        bst.insert(num)
        d_sum = bst.sum_distances()
        totals.append(d_sum)

    return totals


if __name__ == '__main__':
    arr = [4, 7, 3, 1, 8, 2, 6, 5]
    result = solve(arr)
    expected = [0, 1, 4, 10, 20, 35, 52, 76]
    #print("Expected: %s" % expected)
    #print("Result: %s" % result)

