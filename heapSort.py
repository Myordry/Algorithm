def Max_Heapify(heap,HeapSize,root): #在堆中做结构调整使得父节点的值大于子节点
    left = 2*root + 1
    right = left + 1
    larger = root
    if left<HeapSize and heap[larger] < heap[left]:
        larger = left
    if right<HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root: #如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        Max_Heapify(heap,HeapSize,larger)

def Build_Max_Heap(heap): #构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap) #堆长度
    for i in range((HeapSize - 2)//2,-1,-1): #从后往前数
        Max_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_Max_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        Max_Heapify(heap,i,0)
    return heap

if __name__ == "__main__":
    a = [30,50,57,77,62,78,94,80,84]
    HeapSort(a)
    print(a)


