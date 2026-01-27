from itertools import chain, combinations

INFO_TYPES = ["City", "Wilds", "Wastes", "Below"]


def get_info_type():
    return [
        list(combo)
        for combo in chain.from_iterable(
            combinations(INFO_TYPES, r) for r in range(1, len(INFO_TYPES) + 1)
        )
    ]


if __name__ == "__main__":
    for index, result in enumerate(get_info_type()):
        print(f"{index + 1}:\t {result}")
