import sys
queue=[]
data = input()
equation=[]
for i in data:
    equation.append(i)

ans=[]
for i in equation:
    if i == "(":
        queue.append(i)
    elif i == "+" or i == "-":
        while (queue and (queue[-1] != "(")):
            print(queue.pop(), end="")
        queue.append(i)
    elif i == "*" or i=="/":
        while (queue) and(queue[-1] != "(") and ((queue[-1]=="*") or (queue[-1]=="/")):
            print(queue.pop(),end="")
        queue.append(i)
    
    elif i ==")":
        while (queue and queue[-1] != "("):
            print(queue.pop(),end="")
        queue.pop()

    else:
        print(i,end="")
    
if queue:
    for i in range(len(queue)):
        print(queue.pop(),end="")

