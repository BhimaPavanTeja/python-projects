stack = []
def push(val):
    if len(stack) == 5:
        print("Stack Overflow!")
        return
    stack.append(val)
def pop():
    if stack:
        print(stack.pop())
        return
    print("Stack Underflow")
def top():
    if stack:
        print(stack[-1])
        return
    print("empty!")

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)  # This should trigger "Stack Overflow!"

print(stack)

top()  # This should print 5

pop()   # This should print 5
top()  # This should print 4

pop()   # This should print 4
pop()   # This should print 3
pop()   # This should print 2
pop()   # This should print 1
pop()   # This should trigger "Stack Underflow"
