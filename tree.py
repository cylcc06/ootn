from __future__ import unicode_literals  # at top of module
from __future__ import division, print_function, with_statement

class TreeNode(object):
    """The basic node of tree structure"""

    def __init__(self, name, parent=None):
        super(TreeNode, self).__init__()
        self.name = name
        self.parent = parent
        self.child = {}

    def __repr__(self) :
        return 'TreeNode(%s)' % self.name

    def __contains__(self, item):
        return item in self.child

    def __len__(self):
        """return number of children node"""
        return len(self.child)

    def __bool__(self, item):
        """always return True for exist node"""
        return True

    #@property
    def path(self):
        """return path string (from root to current node)"""
        if self.parent:
            return '%s %s' % (self.parent.path.strip(), self.name)
        else:
            return self.name

    def get_child(self, name, defval=None):
        """get a child node of current node"""
        return self.child.get(name, defval)

    def add_child(self, name, obj=None):
        """add a child node to current node"""
        if obj and not isinstance(obj, TreeNode):
            raise ValueError('TreeNode only add another TreeNode obj as child')
        if obj is None:
            obj = TreeNode(name)
        obj.parent = self
        self.child[name] = obj
        return obj

    def del_child(self, name):
        """remove a child node from current node"""
        if name in self.child:
            del self.child[name]

    def find_child(self, path, create=False):
        """find child node by path/name, return None if not found"""
        # convert path to a list if input is a string
        path = path if isinstance(path, list) else path.split()
        cur = self
        for sub in path:
            # search
            obj = cur.get_child(sub)
            if obj is None and create:
                # create new node if need
                obj = cur.add_child(sub)
            # check if search done
            if obj is None:
                break
            cur = obj
        return obj

    def items(self):
        return self.child.items()

    def dump(self, indent=0):
        """dump tree to string"""
        tab = '    '*(indent-1) + ' |- ' if indent > 0 else ''
        print('%s%s' % (tab, self.name))
        for name, obj in self.items():
            obj.dump(indent+1)


if __name__ == '__main__':
    # local test
    print('test add_child()')
    root = TreeNode('root') # root name is ''
    a1 = root.add_child('a1')
    a1.add_child('b1')
    a1.add_child('b2')
    a2 = root.add_child('a2')
    b3 = a2.add_child('b3')
    b3.add_child('c1')
    root.dump()
    # (root)
    #  |- a1
    #      |- b1
    #      |- b2
    #  |- a2
    #      |- b3
    #          |- c1


    print('test items()')
    for name, obj in a1.items():
        print(name, obj)
    # b1 TreeNode(b1)
    # b2 TreeNode(b2)


    print('test operator "in"')
    print("b2 is a1's child = %s" % ('b2' in a1))
    # b2 is a1's child = True


    print('test del_child()')
    a1.del_child('b2')
    root.dump()
    print("b2 is a1's child = %s" % ('b2' in a1))
    # (root)
    #  |- a1
    #      |- b1
    #  |- a2
    #      |- b3
    #          |- c1
    # b2 is a1's child = False


    print('test find_child()')
    obj = root.find_child('a2 b3 c1')
    print(obj)
    # TreeNode(c1)

    print('test find_child() with create')
    obj = root.find_child('a1 b1 c2 b1 e1 f1', create=True)
    print(obj)
    root.dump()
    # TreeNode(f1)
    # (root)
    # |- a1
    #     |- b1
    #         |- c2
    #             |- b1
    #                 |- e1
    #                     |- f1
    # |- a2
    #     |- b3
    #         |- c1

    print('test attr path')
    print(obj.path)
    # a1 b1 c2 b1 e1 f1