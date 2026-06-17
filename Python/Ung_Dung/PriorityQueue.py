from queue import PriorityQueue

pq = PriorityQueue()

pq.put(("thấp", "task C"))
pq.put(("cao", "task A"))
pq.put(("trung bình", "task B"))

while not pq.empty():
    priority, task = pq.get()
    print(priority, task)
