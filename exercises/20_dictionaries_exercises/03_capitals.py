def main():
    countries = [country for country in input().split(sep=", ")]
    capitals = [capital for capital in input().split(sep=", ")]

    result_dict = {country: city for country, city in zip(countries, capitals)}

    [print(f'{country} -> {city}') for country, city in result_dict.items()]


if __name__ == '__main__':
    main()
