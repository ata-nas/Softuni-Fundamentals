class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return list(filter(lambda x: x.startswith(first_letter), self.products))

    def __repr__(self):
        prod = list(sorted(self.products))
        print_prod = "\n".join(prod)
        return f"Items in the {self.name} catalogue:\n{print_prod}"
