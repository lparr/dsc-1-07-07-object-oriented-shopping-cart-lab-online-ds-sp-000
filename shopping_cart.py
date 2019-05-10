class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, emp_discount=None, items = []):
        self.total = sum([i['Price']*i['Quantity'] for i in items])
        self.emp_discount = emp_discount
        self.items = items

    def add_item(self, name, price, quantity=1):
        self.items.append({'Item Name': name, 'Price': price, 'Quantity': quantity})
        self.total += price * quantity
        return self.total
      
    def mean_item_price(self):
        num_items = sum(i['Quantity'] for i in self.items)
        total = self.total
        return total/num_items

    def median_item_price(self):
        length = sum(i['Quantity'] for i in self.items)
        prices = sorted([i['Price'] for i in self.items])
          if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass