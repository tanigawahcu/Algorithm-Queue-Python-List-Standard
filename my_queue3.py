# 参考URL
# - https://note.nkmk.me/python-collections-deque/
#
from collections import deque

class MyQueue:
    def __init__(self):
        self.arr  = deque()
    
    # enqueue
    def enqueue(self, val):
        self.arr.append(val)

    # dequeue
    def dequeue(self) :
        return self.arr.popleft()

    # スタックの中身を文字列に変換
    def to_string(self):
        return self.arr.__str__()

if __name__ == "__main__" :
    # 最大の大きさが6の空のキューを生成
    my_queue = MyQueue()

    # enqueue前のキューの状態を表示
    print("enqueue前のキューの状態")
    print("値: ", my_queue.to_string())
    print()

    # 要素のプッシュ
    my_queue.enqueue(6)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(7)
    my_queue.enqueue(9)

    # enqueue後のキューの状態を表示
    print("enqueue後のキューの状態")
    print("値: ", my_queue.to_string())
    print()

    # dequeue 2回
    x = my_queue.dequeue()
    print("dequeueした値：",x)
    y = my_queue.dequeue()
    print("dequeueした値：",y)
    print()

    # dequeue 後のキューの状態を表示
    print("enqueue後のキューの状態")
    print("値: ", my_queue.to_string())
    print()


