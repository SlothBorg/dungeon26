from random import choice, randint

SIGNIFICANT_TERRAIN = [
    {
        "name": "Ancient farmland",
        "description": "A huge stretch of land was re-engineered for optimal farming.",
    },
    {
        "name": "Arratu wasteland",
        "description": "An area here was once xenoformed by the Outsiders into an environment hostile to humanity or one inhabited by dangerous alien lifeforms.",
    },
    {
        "name": "Blasted lands",
        "description": "Radioactive or scorched over by ancient war. Many ruins are likely.",
    },
    {
        "name": "Canyons",
        "description": "A region with extensive canyons cut by rivers present or long-vanished. Make sure the rivers don't climb after leaving them.",
    },
    {
        "name": "Dense forest",
        "description": "Trackless, dark, and an effective natural barrier.",
    },
    {
        "name": "Grasslands",
        "description": "A broad sweep of savanna or grassy plains is a coherent whole here.",
    },
    {
        "name": "Islands",
        "description": "There's a single significant island off the coast or an archipelago of some note.",
    },
    {
        "name": "Jagged mountains",
        "description": "A new or re-sharpened mountain range forms a barrier in the region. The mountains are young, tall, and likely cast a substantial rain shadow.",
    },
    {
        "name": "Jungle",
        "description": "A classic adventure-worthy jungle of wild, semi-alien flora and fauna.",
    },
    {
        "name": "Light forest",
        "description": "Interspersed with other terrain.",
    },
    {
        "name": "Megaplex",
        "description": "The ruins of a single huge ancient structure stretch for endless miles.",
    },
    {
        "name": "Pit",
        "description": "A Deep or some other underground megastructure collapsed and left a hole with a diameter measured in tens of miles.",
    },
    {
        "name": "Rain forest",
        "description": "Vast, damp, and green.",
    },
    {
        "name": "Rocky hills",
        "description": "Rough and stony, with little arable land. Herding and raiding are the most profitable employments here.",
    },
    {
        "name": "Rolling hills",
        "description": "A stretch of gently rolling hills makes for good agricultural land.",
    },
    {
        "name": "Sand desert",
        "description": "This desert is a waste of sand and dunes. It may be from a rain shadow, or it might be a legacy of ancient war.",
    },
    {
        "name": "Scrub desert",
        "description": "These often appear on the leeward side of mountain ranges. Borders will often be grasslands or savanna.",
    },
    {
        "name": "Swamp",
        "description": "A sinking river, lake margin, or wet coastal delta forms a vast bog in this flat land.",
    },
    {
        "name": "Volcano",
        "description": "One or more mountains in a nearby range are volcanically active. This may be natural or it may be a consequence of Legacy flux or ancient manipulation.",
    },
    {
        "name": "Weathered mountains",
        "description": "A significant skirt of hills is common. The rain shadow is likely limited due to the rounded, low mountains.",
    },
]
DANGER = [
    {
        "name": "Safer than usual",
        "description": "Safer than usual for someplace like it",
    },
    {
        "name": "One notable danger",
        "description": "There's one notable kind of danger there",
    },
    {
        "name": "Site-specific perils",
        "description": "It's got some site-specific flavors of peril",
    },
    {
        "name": "Unusually dangerous",
        "description": "It's unusually dangerous in several ways",
    },
    {
        "name": "Deadly to unprepared",
        "description": "It will quickly kill the unprepared or unwary",
    },
    {
        "name": "Death zone",
        "description": "It's a death zone for all but the strongest",
    },
]
USE = [
    {
        "name": "Rare resource",
        "description": "A rare and precious resource is found there",
    },
    {
        "name": "Ancient sites",
        "description": "Ancient sites and relics are common there",
    },
    {
        "name": "Sacred land",
        "description": "It's sacred land to a group or religion",
    },
    {
        "name": "Military significance",
        "description": "Controlling it has military significance",
    },
    {
        "name": "Productive infrastructure",
        "description": "It has substantial productive infrastructure",
    },
    {
        "name": "Major trade route",
        "description": "A major trade route goes through it",
    },
    {
        "name": "Nest of raiders",
        "description": "Uncontrolled, it's a nest of raiders and worse",
    },
    {
        "name": "Functioning Working",
        "description": "A mighty Working is still functioning there",
    },
]
EVENT = [
    {
        "name": "Significant battle",
        "description": "A significant battle was fought there",
    },
    {
        "name": "Mad prophet",
        "description": "A mad prophet tried to start a faith there",
    },
    {
        "name": "Usurper fled",
        "description": "A usurper and supporters fled into it",
    },
    {
        "name": "Resource strike",
        "description": "A resource strike drew numerous people",
    },
    {
        "name": "Bandit nest formed",
        "description": "A major nest of bandits or raiders formed",
    },
    {
        "name": "Ruin discovered",
        "description": "A rich ancient ruin was discovered there",
    },
    {
        "name": "Uncanny plague",
        "description": "An uncanny plague erupted in the area",
    },
    {
        "name": "Terrible awakening",
        "description": "Some grim and terrible thing was awoken",
    },
    {
        "name": "Outcast community",
        "description": "A community of outcasts or marginals formed",
    },
    {
        "name": "Disaster struck",
        "description": "A natural or uncanny disaster struck there",
    },
]
POPULATION = [
    {
        "name": "Almost unpopulated",
        "description": "Almost unpopulated for something like it",
    },
    {
        "name": "Very few settlers",
        "description": "Very few settlers or workers there",
    },
    {
        "name": "Average density",
        "description": "Average or more population density",
    },
    {
        "name": "Population rush",
        "description": "A rush of people have gone there",
    },
]
FOE = [
    {
        "name": "Violent secessionist rebels",
        "description": "Violent secessionist rebels",
    },
    {
        "name": "Angry cultists",
        "description": "Angry cultists of a local faith",
    },
    {
        "name": "Resentful locals",
        "description": "Locals who resent interloping outsiders",
    },
    {
        "name": "Cunning beasts",
        "description": "A type of cunning, dangerous beast",
    },
    {
        "name": "Relic-creatures",
        "description": "Relic-creatures of ancient settlements",
    },
    {
        "name": "Elemental emanations",
        "description": "Elemental emanations of the disordered land",
    },
    {
        "name": "Hostile monsters",
        "description": "A hostile sentient monster civilization",
    },
    {
        "name": "Brutal government envoys",
        "description": "Brutal envoys of the central government",
    },
    {
        "name": "Raiders and bandits",
        "description": "Raiders and bandits driven into the area",
    },
    {
        "name": "Rapacious lords",
        "description": "Rapacious local lords and gang bosses",
    },
    {
        "name": "Furious natives",
        "description": "Remnants of a furious native population",
    },
    {
        "name": "Outsider remnants",
        "description": "Outsider remnants with a bitter grudge",
    },
]
QUIRCKS = [
    {
        "name": "Magical structures",
        "description": "It has significant magical structures in it",
    },
    {
        "name": "Origin legend",
        "description": "It has a place in the national origin legend",
    },
    {
        "name": "Man-made by ancients",
        "description": "It is entirely man-made by ancient arts",
    },
    {
        "name": "Time and space slip",
        "description": "Time and space sometimes slip there",
    },
    {
        "name": "Attracts wizards",
        "description": "The magical power there attracts wizards",
    },
    {
        "name": "Changes inhabitants",
        "description": "It subtly changes those who live there",
    },
    {
        "name": "Holy land",
        "description": "It's holy land to a particular faith",
    },
    {
        "name": "Different terrain formerly",
        "description": "It was formerly a different kind of terrain",
    },
    {
        "name": "Human-worked beauty",
        "description": "It has human-worked vistas of beauty",
    },
    {
        "name": "Outsider stronghold",
        "description": "It was formerly an Outsider stronghold",
    },
    {
        "name": "Subterranean",
        "description": "A significant part of it is subterranean",
    },
    {
        "name": "Warded expansion",
        "description": "It'd expand were it not for ancient wards",
    },
    {
        "name": "Nature preserve",
        "description": "It was a nature preserve of a megastructure",
    },
    {
        "name": "Artificial mind",
        "description": "It's maintained by an ancient artificial mind",
    },
    {
        "name": "Warped magic",
        "description": "Magic is somehow warped in its area",
    },
    {
        "name": "Off flora and fauna",
        "description": "The flora and fauna are queasily 'off'",
    },
    {
        "name": "Former heavy population",
        "description": "The locals once populated it more heavily",
    },
    {
        "name": "Disputed rulership",
        "description": "Rulership of the feature is widely disputed",
    },
    {
        "name": "Caves and delvings",
        "description": "It's riddled with caves and delvings",
    },
    {
        "name": "Unique sentients",
        "description": "A unique type of sentient lives there",
    },
]


terrain = choice(SIGNIFICANT_TERRAIN)
print(f"{terrain['name']}")
print(f"\t{terrain['description']}")

for item in [DANGER, USE, EVENT, POPULATION, FOE]:
    item_selection = choice(item)
    print(f"\t{item_selection['name']}")
    print(f"\t\t{item_selection['description']}")

if randint(0, 1) > 0:
    print(f"{choice(QUIRCKS)}")
