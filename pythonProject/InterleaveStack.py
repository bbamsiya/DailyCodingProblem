from queue import Queue


def interleave_stack(stack):
    N = len(stack)
    if N <= 1:
        return

    # Create a queue
    queue = Queue()

    half_size = N // 2

    # Step 1: Push the first half of the stack into the queue
    for _ in range(half_size):
        queue.put(stack.pop())

    # Step 2: Move elements back to the stack to reverse the second half
    while not queue.empty():
        stack.append(queue.get())

    # Step 3: Move the reversed second half to the queue
    for _ in range(half_size):
        queue.put(stack.pop())

    # Step 4: Interleave the elements from the queue and stack
    for _ in range(half_size):
        stack.append(queue.get())
        stack.append(stack.pop())

    # If N is odd, handle the middle element
    if N % 2 != 0:
        stack.append(queue.get())


def main():
    stack = [1, 2, 3, 4, 5, 6]
    print("Original stack:", stack)
    interleave_stack(stack)
    print("Interleaved stack:", stack)


if __name__ == "__main__":
    main()


