from itertools import product

INFO_TYPES = ["Landmark", "Hidden", "Secret"]


def print_result(index, result_list):
    print_string = ", ".join(str(item) for item in result_list if item is not None)
    print(f"{index}:\t {print_string}")


if __name__ == "__main__":
    options = [[item, None] for item in INFO_TYPES]

    results = list(product(*options))

    # remove any empty lists:
    results = [r for r in results if any(r)]

    for index, result in enumerate(results):
        print_result(index, result)
