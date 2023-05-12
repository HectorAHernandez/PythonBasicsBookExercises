
families_by_city = {
    "Bonao": ["Vargas", "Burgos", "Torres"],
    "Cotui": ["Pena", "Suazo", "Metz", "Almonte"],
    "Bani": ["Baez", "Marinez", "Melo", "Encarnacion"],
    "San Pedro": ["Agelan", "Casasnova", "Zorrilla"]
    }

def families_search(cities):
    print("cities-->", cities)
    for city in cities:
        try:
            print(f"city {city} contains these families: {families_by_city[city]}")
        except KeyError:
            print(f"No families in city {city}")

def sort_families_in_city(city, order):
    try:
        families_in_city = families_by_city[city]
        if order.upper() == "A":
            families_in_city.sort(key=lambda x: x[0], reverse=False)
        else:
            families_in_city.sort(reverse=True)        
        print(f"Sorted families_in_city {city}: {families_in_city}")
    except KeyError:
        print(f"No families in city {city}")

families_search(["Bonao", "La Vega", "Bani"])

sort_families_in_city("Bonao", "D")
sort_families_in_city("Bonao", "A")
sort_families_in_city("San Pedro", "D")
sort_families_in_city("Bani", "A")

