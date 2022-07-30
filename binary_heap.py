class MinHeap:
    def __init__(self, values: Optional[List[float]] = None):
        self._heap = values
        self._heapify()

    def __len__(self) -> int:
        return len(self._heap)

    # Push a new value onto the heap
    # O(log(n)) time and space complexity
    def push(self, value: float) -> None:
        self._heap.append(value)
        self._sift_up(len(self._heap)-1)

    # Find and extract the smallest element from the heap
    # O(log(n)) time and space complexity
    def pop(self) -> float:
        if not self._heap:
            raise IndexError('pop from an empty heap')

        # Cache the value to return
        min_value = self.peek()
        
        # Swap the heap and tail of the heap, pop the
        # smallest element, and fix the heap ordering
        self.swap(0, len(self._heap)-1)
        self._heap.pop()
        self._sift_down(0)

        return min_value

    # Find the smallest element on the heap
    # O(1) time and space complexity
    def peek(self) -> float:
        return self._heap[0]

    # Turn an unordered array into a (binary) minimum heap
    # O(n) time and O(log(n)) space complexity
    def _heapify(self) -> None:
        for i in reversed(range(len(self._heap))):
            self._sift_down(i)


    def _sift_up(self, index: int) -> None:
        while index > 0 and self._heap[(index-1)//2] > self._heap[index]:
            self.swap(index, (index-1)//2)
            index = (index-1)//2

    def _sift_down(self, index: int) -> None:
        while index < len(self._heap):
            index1 = 2*index+1
            index2 = 2*index+2

            value = self._heap[index]
            value1 = self._heap[index1] if index1 < len(self._heap) else float('inf')
            value2 = self._heap[index2] if index2 < len(self._heap) else float('inf')

            if (value <= value1) and (value <= value2):
                return
            if (value1 <= value) and (value1 <= value2):
                self.swap(index, index1)
                index = index1
            else:
                self.swap(index, index2)
                index = index2

    def swap(self, index1: int, index2: int) -> None:
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]


    
class MaxHeap:
    def __init__(self, values: Optional[List[float]] = None):
        if values is None:
            values = [] 

        # heapq uses a min-heap, so store the negative of
        # every number instead to form a max heap
        self._heap = [-x for x in values]
        heapq.heapify(self._heap)

    def push(self, value: float) -> None:
        heapq.heappush(self._heap, -value)

    def heappop(self) -> float:
        return -heapq.heappop(self._heap)

    def peek(self) -> float:
        return -self._heap[0]
