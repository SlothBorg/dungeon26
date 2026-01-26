from datetime import date
from itertools import product
from random import randint

INFO_TYPES = ["Landmark", "Hidden", "Secret"]
LOCATIONS = [
    "Entrance Foyer",
    "Catalogue of Contents",
    "Help Desk",
    "Reading Lounge",
    "Chained Lectern",
    "Display Case",
    "Ink Vats",
    "Map Gallery",
    "Boiler-room",
    "Auditorium",
    "Skeleton Collection",
    "Chapel",
    "Tea-room",
    "Statuary",
    "Stuffed Animals",
    "Mausoleum",
    "Storage Vault",
    "Planetarium",
    "Calculation Engine",
    "Phantom Databanks",
    "Spider Trapdoor",
    "Printing Machine",
    "Ossuary",
    "Syphon of Phantoms",
    "Steam vents",
    "Paper Beehive",
    "Furnace",
    "Holding Pen",
    "Phantom Pumps",
    "Infernal Gateway",
    "Jarred Brains",
    "Dissection Theatre",
    "Mummy Vault",
    "Sheol Computer",
]
DETAILS = [
    "Empty",
    "Treasure-pile",
    "Notes",
    "Oriental Rug",
    "Candles",
    "Webs",
    "Fireplace",
    "Lamp-Post",
    "Gas Lamps",
    "Glass Tubes",
    "Staircase",
    "Candle-sticks",
    "Portcullis",
    "Scrolls",
    "Funeral Urns",
    "Turning Gears",
    "Vault",
    "Chained Books",
    "Too Small",
    "Phosphorescent Lamps",
    "Stacked Papers",
    "Negligible Gravity",
    "Silent",
    "Letters",
    "Spirit Illumination",
    "Too Large",
    "Haunted",
    "Smoking",
    "Spirit Tubes",
    "Watchful",
    "Morbid",
    "Time-locked",
    "Semi-corporeal",
    "Doorway Out",
]


def get_info_type():
    options = [[item, None] for item in INFO_TYPES]

    results = list(product(*options))

    offset = randint(0, (len(results) - 1))

    return results[offset]


def get_random_item(item_list):
    base = randint(1, 20)
    bias = date.today().day

    offset = base + bias

    if offset >= len(item_list):
        offset = int(offset / 2)

    return item_list[offset]


def get_location():
    return get_random_item(LOCATIONS)


def get_detail():
    return get_random_item(DETAILS)


def print_result(result_list):
    print_string = ", ".join(str(item) for item in result_list if item is not None)
    print(f"{print_string}")


if __name__ == "__main__":
    print(f"{get_location()}\t{get_detail()}")
    print_result(get_info_type())
