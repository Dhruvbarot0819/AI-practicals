class node:
    def __init__(self, node_name, child_node, parent_node):
        self.node_name = node_name
        self.child_node = child_node
        self.parent_node = parent_node

class tree:
    def __init__(self, root):
        self.root = root

    def insert_node(self, name, parent_node):
        child_node = node(name, [], parent_node)
        parent_node.child_node.append(child_node)
        return child_node

def bfs_search(tree, search_string):
    queue = []
    queue.append(tree.root)

    while len(queue) != 0:
        pop_node = queue.pop(0)
        if pop_node.node_name == search_string:
            return pop_node
        else:
            for child in pop_node.child_node:
                queue.append(child)
    return None

def print_path(pop_node):
    path_list = []
    node = pop_node
    while node != None:
        path_list.append(node.node_name)
        node = node.parent_node

    totallen = len(path_list)
    r_list = path_list[::-1]
    print("path is as below:")

    for i in range(0, totallen-1):
        print(r_list[i], end=" -> ")
    print(r_list[totallen-1])
    print(f"path cost: {totallen}")

root = tree(node("amit", [], None))
amit = root.root

rahul = root.insert_node('rahul', amit)
priya = root.insert_node('priya', amit)

sanjay = root.insert_node('sanjay', rahul)
ravi = root.insert_node('ravi', rahul)

nisha = root.insert_node('nisha', priya)
claire = root.insert_node('claire', priya)

deepak = root.insert_node('deepak', sanjay)
raj = root.insert_node('raj', sanjay)
suresh = root.insert_node('suresh', sanjay)

lisa = root.insert_node('lisa', nisha)
eric = root.insert_node('eric', nisha)

vinay = root.insert_node('vinay', deepak)
akash = root.insert_node('akash', deepak)

gaurav = root.insert_node('gaurav', raj)

meena = root.insert_node('meena', suresh)

sam = root.insert_node('sam', lisa)
john = root.insert_node('john', lisa)

ankit = root.insert_node('ankit', vinay)
harsh = root.insert_node('harsh', vinay)

aditya = root.insert_node('aditya', gaurav)
sneha = root.insert_node('senha', gaurav)
alice = root.insert_node('alice', gaurav)

reena = root.insert_node('reena', meena)

abhishek = root.insert_node('abhishek', ankit)

puneet = root.insert_node('puneet', harsh)
vikas = root.insert_node('vikas', harsh)
varun = root.insert_node('varun', harsh)

anjali = root.insert_node('anjali', sneha)
arjun = root.insert_node('arjun', sneha)

caral = root.insert_node('caral', alice)
dave = root.insert_node('dave', alice)

rohan = root.insert_node('rohan', abhishek)
ajay = root.insert_node('ajay', abhishek)

nidhi = root.insert_node('nidhi', anjali)

sachin = root.insert_node('sahin', arjun)
sumit = root.insert_node('simit', arjun)

aruna = root.insert_node('aruna', rohan)
ramji = root.insert_node('ramji', rohan)

virat = root.insert_node('virat', ajay)
isha = root.insert_node('isha', ajay)

pream = root.insert_node('pream', nidhi)
lina = root.insert_node('lina', nidhi)

print('22012012001')

username = input('Enter name to search:')
ans = bfs_search(root, username)

if ans != None:
    print("--------------------------------")
    print(f"search_node: {ans.node_name}")
    print_path(ans)
    print("--------------------------------")
else:
    print("searched node not exit")
