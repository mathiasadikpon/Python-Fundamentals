class Queue:
    def __init__(self):
        self.items = []
    

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    
    def take_order(self,customer:str, flavor:str, scoops:int):
        if flavor not in self.flavors:
            print(f"Sorry {customer}, we don't have {flavor} flavor.")
            
        if scoops < 1 or scoops > 3:
            print("Choose between 1-3 sccops.")
        else:
            print("Order created!")
            order = {"customer":customer, "flavor":flavor, "scoops":scoops}
            self.orders.enqueue(order)
    

    def show_all_orders(self):
        """print all orders in the queue"""
        print("\nAll Pending Ice Cream Orders:")
        if self.orders.size() == 0:
            print("No pending orders.")
            return
        for order in self.orders.items:
            print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")
    

    def next_order(self):
        '''dequeue the head order in the queue and show it'''
        print("\nNext Order Up!")
        if self.orders.size() == 0:
            print("No pending orders.")
            return
        order = self.orders.dequeue()
        print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")

