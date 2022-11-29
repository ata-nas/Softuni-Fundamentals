COMMAND_END = 'End'


class Registry:
    registry = {}

    curr_company = None
    curr_id = None

    @classmethod
    def _save(cls):
        if cls.curr_company not in cls.registry.keys():
            cls.registry[cls.curr_company] = [cls.curr_id]
        elif cls.curr_id not in cls.registry[cls.curr_company]:
            cls.registry[cls.curr_company].append(cls.curr_id)

    @classmethod
    def tree_registry(cls):
        for key, values in cls.registry.items():
            print(key)
            for value in values:
                print(f'-- {value}')

    @classmethod
    def fill_registry(cls, emp_tuple):
        for item in emp_tuple:
            company = item[0]
            emp_id = item[1]

            curr_employee = Employee(company, emp_id)

            cls.curr_company = curr_employee.company
            cls.curr_id = curr_employee.id

            cls._save()


class Company:
    def __init__(self, company_name) -> None:
        self.company_name = company_name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(\'{self.company_name}\')'

    # def __str__(self) -> str:
    #     return f'Company name: {self.company_name}'


class EmployeeID:
    def __init__(self, id) -> None:
        self.id = id

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.id})'

    # def __str__(self) -> str:
    #     return f'Employee ID: {self.id}'


class Employee:
    def __init__(self, company_name, id) -> None:
        self.__comp_name = Company(company_name=company_name)
        self.__emp_id = EmployeeID(id=id)

    @property
    def company(self):
        return self.__comp_name.company_name

    @property
    def id(self):
        return self.__emp_id.id

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__comp_name.company_name}, {self.__emp_id.id})'


def generate_employee_tuple():
    result = []

    while True:
        user_input = input()

        if user_input == COMMAND_END:
            break

        company, emp_id = user_input.split(sep=' -> ')

        result.append((company, emp_id))

    return tuple(result)


def main():
    emp_tup = generate_employee_tuple()

    Registry.fill_registry(emp_tup)

    Registry.tree_registry()


if __name__ == '__main__':
    main()
