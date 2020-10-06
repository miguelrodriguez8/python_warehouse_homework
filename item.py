
class Item:
    id = 0
    title = ''
    category = ''
    stock = 0
    price = 0.0

    def __init__(self, id, title, cat, stock, price):
        self.id = id
        self.title = title
        self.category = cat
        self.stock = stock
        self.price = price



