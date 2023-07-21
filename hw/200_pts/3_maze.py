# get input
x,y = input().split(" ")
x,y = (int(x), int(y))
print(x,y)
num_of_walls = int(input())
# wall的坐标
wall_locs = []
for i in range(num_of_walls):
    wall_loc = input().split(" ")
    wall_locs.append((int(wall_loc[0]), int(wall_loc[1])))
print(wall_locs)

#  form tree( simulate walking process )
tree_dict = {} 
root_list = {(0,0)}
while len(root_list):
    node = root_list.pop()
    # print("node", node)
    k = f"{node[0]},{node[1]}"
    if k in tree_dict or node in wall_locs:
        continue
    tree_dict[k] = []
    if node[0] + 1 <= x:
        right_node = (node[0] + 1, node[1])
        if right_node in wall_loc: continue
        tree_dict[k].append(right_node)
        root_list.add(right_node)
    if node[1] + 1 <= y:
        top_node = ((node[0], node[1] + 1))
        if top_node in wall_loc: continue
        tree_dict[k].append(top_node)
        root_list.add(top_node)

traps = []
# 陷阱方格
for k in tree_dict.keys():
    # print(k)
    splits = k.split(',')
    node = (int(splits[0]), int(splits[1]))
    if len(tree_dict[k]) == 0 and node != (x,y):
        traps.append(node)

unreachable_checks = []
for i in range(x+1):
    for j in range(y+1):
        if (f"{i},{j}" not in tree_dict.keys()) and ((i, j) not in wall_locs):
            unreachable_checks.append((i,j))
# print(tree_dict)
print(traps)
print(unreachable_checks)

# for i in range(x):
#     for j in range(y):
#         if k in tree_dict:
#             continue
#         tree_dict[k] = []
#         if 




    