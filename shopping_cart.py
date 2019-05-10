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
        price_list = []
        price_list.append(i['Price'] for i in items)
        mean = sum(price_list)/len(price_list)
        return f"Mean Price: {mean}"

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass