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
        

#root of the tree
root = Tree()
root.pos = 1
root.parent = None

count += 1
make_tree(root)

print("No. of nodes = ",count)

#finding solution
node = root
while True:
    if node.pos == n:
        hit = 1
        soln = node
        break
    if node.pos > n:
        hit = 0
        soln = node
        print("Oops!..    Hit Deadend...")
    #computing heuristics
    if node.left != None and node.right != None:
        #heuristic values
        h_left = n - node.left.pos 
        h_right = n - node.right.pos
        
        #deciding next move
        if h_left < h_right:
            node = node.left
        else:
            node = node.right
    else:
        print("Oops!..    Hit Deadend...")
        break

if hit == 0:
    print("Could not find solution! ")
    print("Local Maxima supercedes the Global maximum.")
    print("Steps followed : ")
    node = soln.parent
else:
    temp = soln
    height = 0
    while temp.parent != None:
        height += 1
        temp = temp.parent

    print("Fastest solution is in ", height ," steps")
    node = soln

while node.parent != None:
    print("Position : ",node.pos, "\tColour of Square : ", conf[node.pos - 1])
    print("\t\t|")
    node = node.parent
print("Position : ",root.pos,"\tColour of Square : ",conf[0])

