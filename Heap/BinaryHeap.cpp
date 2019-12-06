// https://www.geeksforgeeks.org/binary-heap/
#include <iostream>
#include <climits>

void swap(int&, int&);

class MinHeap {
private:
    int *harr;
    int capacity;
    int heap_size;
public:
    // constuctor
    MinHeap(int capacity);

    void MinHeapify(int);

    int parent(int i) { return (i-1) / 2; }

    int left(int i) { return 2*i+1; }

    int right(int i) { return 2*i+2; }

    int extractMin();

    void decreaseKey(int, int);

    int getMin() { return harr[0]; }

    void deleteKey(int);

    void insertKey(int);

    void print_heap();
};

MinHeap::MinHeap(int cap) {
    heap_size = 0;
    capacity = cap;
    harr = new int[cap];
}

void MinHeap::insertKey(int k) {
    if (heap_size == capacity)
        return;

    int i = heap_size;
    heap_size++;
    harr[i] = k;

    while (i != 0 && harr[parent(i)] > harr[i]) {
        swap(harr[i], harr[parent(i)]);
        i = parent(i);
    }
}

void MinHeap::decreaseKey(int i, int new_val) {
    harr[i] = new_val;
    while (i != 0 && harr[parent(i)] > harr[i]) {
        swap(harr[i], harr[parent(i)]);
        i = parent(i);
    }
}

int MinHeap::extractMin() {
    if (heap_size <= 0)
        return INT_MAX;
    if (heap_size == 1) {
        heap_size--;
        return harr[0];
    }
    int root = harr[0];
    harr[0] = harr[heap_size-1];
    heap_size--;
    MinHeapify(0);
    return root;
}

void MinHeap::deleteKey(int i) {
    decreaseKey(i, INT_MIN);
    extractMin();
}

void MinHeap::MinHeapify(int i) {
    int l = left(i);
    int r = right(i);
    int smallest = i;
    if (l < heap_size && harr[l] < harr[i])
        smallest = l;
    if (r < heap_size && harr[r] < harr[smallest])
        smallest = r;
    if (smallest != i) {
        swap(harr[i], harr[smallest]);
        MinHeapify(smallest);
    }
}

void MinHeap::print_heap() {
    std::cout << " >> ";
    for (int i = 0; i < heap_size; i++)
        std::cout << harr[i] << " ";
    std::cout << heap_size << '\n';
}

void swap(int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}

int main()
{
    MinHeap h(11);
    h.insertKey(3);
    h.insertKey(2); // 2, 3
    h.deleteKey(1);
    h.insertKey(15);
    h.insertKey(5);
    h.insertKey(4);
    h.insertKey(45);
    h.print_heap();
    std::cout << h.extractMin() << " ";
    h.print_heap();
    std::cout << h.getMin() << " ";
    h.print_heap();
    h.decreaseKey(2, 1);
    h.print_heap();
    std::cout << h.getMin();
    return 0;
}
