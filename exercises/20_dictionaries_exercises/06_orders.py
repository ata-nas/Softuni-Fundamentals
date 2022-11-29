class Product:
    all_dict = {}

    def __init__(self, name, price, quantiy) -> None:
        self.name = name
        self.price = price
        self.quantity = quantiy

    def add_product(self):
        if self.name not in Product.all_dict.keys():
            Product.all_dict[self.name] = [
                float(self.price), int(self.quantity)]
        else:
            if float(self.price) != Product.all_dict[self.name][0]:
                Product.all_dict[self.name][0] = float(self.price)
                Product.all_dict[self.name][1] += self.quantity
            else:
                Product.all_dict[self.name][1] += self.quantity

    @classmethod
    def print_items(cls):
        for key, value in cls.all_dict.items():
            print(f'{key} -> {(value[0] * value[1]):.2f}')


def main():
    products = []
    while True:
        user_input = input()

        if user_input == "buy":
            break

        user_input = user_input.split(sep=" ")

        prod_name = user_input[0]
        prod_price = float(user_input[1])
        prod_quant = int(user_input[2])

        curr_product = Product(prod_name, prod_price, prod_quant)
        curr_product.add_product()

    Product.print_items()


if __name__ == '__main__':
    main()
