import binarytree as bt


class Tree:
    def __init__(self, *args):
        self.tree = []
        for i in args:
            self.insert(i)

    def __repr__(self):
        self.root = bt.Node(self.tree[0])
        for i in range(1,len(self.tree)):
            binary = "{0:b}".format(i+1)[1:]
            self.lefts_rights('self.root', binary, i)
        print(self.root)
        return ''

    def lefts_rights(self, path, binary, i):
        lr = ['left', 'right'][int(binary[0])]
        if len(binary) == 1:
            setattr(eval(path), lr, bt.Node(self.tree[i]))
        else:
            self.lefts_rights(path+'.'+lr, binary[1:], i)


    def parent(self, i):
        if i == 0:
            return -1
        return int(i/2)

    def children(self, i):
        if len(self.tree) < 2 * i + 2:
            return []
        elif len(self.tree) == 2 * i + 2:
            return [self.tree[2 * i + 1]]
        else:
            return [self.tree[2 * i + 1], self.tree[2 * i + 2]]

    def up_heap(self, i):
        parent_id = self.parent(i)
        if parent_id >= 0:
            if self.tree[i] > self.tree[parent_id]:
                self.tree[i], self.tree[parent_id] = self.tree[parent_id], self.tree[i]
                self.up_heap(parent_id)

    def down_heap(self, i):
        child_vals = self.children(i)
        if child_vals:
            largest_index = 2*i+1+child_vals.index(max(child_vals))
            if self.tree[i] < self.tree[largest_index]:
                self.tree[i], self.tree[largest_index] = \
                  self.tree[largest_index], self.tree[i]
                self.down_heap(largest_index)

    def insert(self, n):
        self.tree.append(n)
        self.up_heap(len(self.tree)-1)

    def extract(self):
        root = self.tree[0]
        self.tree[0] = self.tree.pop(-1)
        self.down_heap(0)
        return root

    def insert_then_extract(self,n):
        if n < self.tree[0]:
            n, self.tree[0] = self.tree[0], n
            self.down_heap(0)
        return n

    def search(self,n):
        for i in range(len(self.tree)):
            if self.tree[i] == n:
                return i
        return False
        # if n in self.tree:
        #     return self.tree.index(n)
        # return False

    def delete(self,n):
        i = self.search(n)
        print(i)
        self.tree[i] = self.tree[-1]
        del self.tree[-1]
        if i == len(self.tree):
            return self.tree
        if self.tree[i] > n:
            self.up_heap(i)
        else:
            self.down_heap(i)
        return self.tree

    def increase(self,i,n):
        self.tree[i] += n
        self.up_heap(i)

    def decrease(self,i,n):
        self.tree[i] -= n
        self.down_heap(i)



x = Tree(2,7,4,3,7,10,4,9,9)
print(x.tree, x)
x.insert(40)
print(x.tree, x)
x.insert_then_extract(5)
print(x.tree, x)
x.delete(9)
print(x.tree, x)
x.increase(2,40)
print(x.tree, x)
x.decrease(3,5)
print(x.tree, x)
