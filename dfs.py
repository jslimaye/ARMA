#taking input from user
global n
n = int(input("No. of squares: "))
global conf
conf = input("Configuration of the squaes: ").split(" ")

print("Length of Path : ",n)
print(conf)

#no. of nodes
global count
count = 0

#declaring tree data structure
class Tree:
    def __init__(self):
        self.pos = None
        self.left = None
        self.right = None
        self.parent = None
    

#making the statespace tree
def make_tree(node):
    position = node.pos
    if position >= n:
        return
    
    elif conf[position-1] == "W" or conf[position-1] == "w":
        new_position = position + 1
        new_node = Tree()
        new_node.parent = node
        node.left = new_node
        new_node.pos = new_position
        
        global count
        count += 1
        make_tree(new_node)
        
        new_position = position + 2
        new_node = Tree()
        new_node.parent = node
        node.right = new_node
        new_node.pos = new_position
        
        count += 1
        make_tree(new_node)
        
        
    elif conf[position-1] == "B" or conf[position-1] == "b":
        new_position = position + 1
        new_node = Tree()
        new_node.parent = node
        node.left = new_node
        new_node.pos = new_position
        
        count += 1
        make_tree(new_node)
        
        new_position = position + 4
        new_node = Tree()
        new_node.parent = node
        node.right = new_node  
        new_node.pos = new_position
        
        count += 1
        make_tree(new_node)

        
#identify the hits
global hits
hits = list()

#depth-first search
def dfs(node):
    if node.pos == n:
        hits.append(node)
        #print("HIT!!!")
    if node.left != None:
        dfs(node.left)
    else:
        return
    if node.right != None:
        dfs(node.right)
    else:
        return      

#root of the tree
root = Tree()
root.pos = 1
root.parent = None

count += 1
make_tree(root)

print("No. of nodes = ",count)

#search for solutions
dfs(root)
print("No. of solutions found = ", len(hits))

#searching for best solution
fastest_soln = root

min_height = count

for node in hits:
    height = 0
    temp = node
    while temp.parent != None:
        height += 1
        temp = temp.parent
    #print(height)
    if height < min_height:
        min_height = height
        print("Quickest solution in ", min_height, " steps. Processing...") 
        fastest_soln = node
    else:
        continue
        
print("Fastest solution is in ", min_height ," steps")
node = fastest_soln
while node.parent != None:
    print("Position : ",node.pos, "\tColour of Square : ", conf[node.pos - 1])
    print("\t\t|")
    node = node.parent
print("Position : ",root.pos,"\tColour of Square : ",conf[0])