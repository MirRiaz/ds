def create_stack():
    Stack = []
    return Stack


def is_empty(Stack):
    if Stack == 0:
        print('Stack Is empty', Stack)


def push(Stack, item):
    Stack.append(item)
    print('Pushed item' + item)


def pop(Stack):
    if (is_empty(Stack)):
        return 'Stack Is empty'

    return Stack.pop()


def size():
    return len()


stack = create_stack()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))

print(len(stack))

