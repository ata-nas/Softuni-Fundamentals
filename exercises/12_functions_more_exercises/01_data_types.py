def data_types(input_data_type: str, input_data):
    if input_data_type == "int":
        return int(input_data) * 2
    elif input_data_type == "real":
        return f"{(float(input_data) * 1.5):.2f}"
    elif input_data_type == "string":
        return f"${input_data}$"


data_type = input()
data = input()

print(data_types(data_type, data))
