# print(1)
# print("1") กลุ่มตัวหนังสือ string
# print('r') ตัวหนังสืออย่างเดียว
# ปัจจุบันใช้ได้เหมือนกัน
# txt = "rai"
# print(txt)

# # fruit = "apple"
# fruits = ["apple", "banana"]
# fruits.append("orange")
# fruits.remove("apple")
# fruits.insert(0, "melon")
# for fruit in fruits:
#     print(f"This is a {fruit}.")

# i = 0
# while i < 3:
#     print(i)
#     i = i + 1
# print("done")

############# Dictionary in Mobile Robot ###############
#           A
#          / \
#         B   C
#        / \   \
#       D  E    F

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
}
start = 'A'
goal = 'E'
frontier = [start]
explored = set() # Use a set for unique (ignore duplicate append)

print(frontier, explored)

while len(frontier) > 0: #len = เช็คจำนวน
    current = frontier.pop() #remove and put into varaible
    print(current)

    if current == goal:
        print("Goal reach")
        break
    
    for neighber in graph[current]:
        frontier.append(neighber)