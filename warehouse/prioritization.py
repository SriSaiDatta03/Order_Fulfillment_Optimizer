import heapq

class OrderQueue:
    def __init__(self):
        self.queue=[]

    def add_order(self,priority,order_details):
        heapq.heappush(self.queue,(priority,order_details))

    def process_order(self):
        return heapq.heappop(self.queue) if self.queue else None
    