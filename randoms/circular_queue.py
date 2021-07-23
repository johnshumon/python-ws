"""Circular Queue Module"""

# Algorithm for Circular Queue
# > Initialize the queue, with size of the queue
#   defined (max_size), and head and tail pointers.
#
# > enqueue: Check if the number of elements is equal to maxSize - 1:
#   - If Yes, then return Queue is full
#   - If No, then add the new data element to the location of tail
#     pointer and increment the tail pointer.
#
# > dequeue: Check if the number of elements in the queue is zero:
#   - If Yes, then return Queue is empty
#   - If No, then increment the head pointer.
#
# > size:
#   - If tail >= head --> size = tail - head
#   - If head > tail --> size = max_size - (head - tail)

from typing import Any


class CircularQueue:
    """Circular queue class"""

    # class constructor
    # user defines max size, default 10
    def __init__(self, max_size: int = 10):

        self.queue = list()
        self.max_size = max_size

        self.head = 0
        self.tail = 0

    def size(self):
        """Return the size of the queue"""
        return (
            self.tail - self.head
            if self.tail >= self.head
            else self.max_size - (self.tail - self.head)
        )

    def enqueue(self, data) -> Any:
        """adds data to the queue if its not full"""

        if self.size() == self.max_size - 1:
            return "Queue is full"

        self.queue.append(data)
        self.tail = (self.tail + 1) % self.max_size
        return "{} inserted in the queue".format(data)

    def dequeue(self) -> Any:
        """removes data from the queue if its not empty"""

        if self.size() == 0:
            return "Empty queue!"

        data = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size

        return data


def main():
    # user input for queue size
    queue_size = input("Enter the queue size: ")
    c_queue = CircularQueue(int(queue_size))

    # change the enqueue and dequeue statements as you want
    print(c_queue.enqueue(1))
    print(c_queue.enqueue(2))
    print(c_queue.enqueue(3))
    print(c_queue.enqueue(4))
    print(c_queue.enqueue(5))
    print(c_queue.enqueue("Studytonight"))
    print(c_queue.enqueue(7))
    print(c_queue.enqueue(8))
    print(c_queue.enqueue(9))
    print(c_queue.enqueue(10))
    print(c_queue.enqueue(11))
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())
    print(c_queue.dequeue())


if __name__ == "__main__":
    main()
