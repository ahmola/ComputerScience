# 연결리스트가 아닌 기본적으로 배열로 만들어놓고 인덱스를 조작하는 방식
# 부모 노드 index // 2
# 왼쪽 자식 index*2, 오른쪽 자식 index*2 + 1
class Heap:
    def __init__(self):
        self.tree = [None]
    
    def push(self, value):
        self.tree.append(value)
        index = len(self.tree)-1

        while index > 1:
            parent = index//2
            if self.tree[parent] < self.tree[index]:
                self.tree[parent], self.tree[index] = self.tree[index], self.tree[parent]
                index = parent
            else:
                break
    
    def pop(self):
        if len(self.tree) == 1:
            return 0
        elif len(self.tree) == 2:
            return self.tree.pop()
        
        value = self.tree[1]
        self.tree[1] = self.tree[len(self.tree)-1]
        self.tree.pop()
        index = 1

        while True:
            left = index*2
            right = index*2+1
            largest = index

            if left < len(self.tree) and self.tree[left] > self.tree[largest]:
                largest = left
            if right < len(self.tree) and self.tree[right] > self.tree[largest]:
                largest = right
            if largest == index:
                break

            self.tree[largest], self.tree[index] = self.tree[index], self.tree[largest]
            index = largest
        
        return value

n = int(input())
heap = Heap()
operation = [int(input()) for _ in range(n)]

for o in operation:
    if o == 0:
        print(heap.pop())
    else:
        heap.push(o)