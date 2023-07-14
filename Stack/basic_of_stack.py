from sys import maxsize


def create_stack():
    return []


def is_empty(stack):
    return len(stack) == 0


def push(my_stack, item):
    my_stack.append(item)


def pop(stack):
    if is_empty(stack):
        return str(-maxsize - 1)  # returning minus infinite

    return stack.pop()


def peek(stack):
    if is_empty(stack):
        return str(-maxsize - 1)  # return minus infinite
    return stack[len(stack) - 1]
