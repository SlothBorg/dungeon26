from random import choice, randint

THEME = [
    {
        "name": "Barbarism",
        "description": "with brutal savagery",
    },
    {
        "name": "Decadence",
        "description": "of sins and fashion",
    },
    {
        "name": "Despair",
        "description": "with good things unlooked-for",
    },
    {
        "name": "Exhaustion",
        "description": "with strength spent and lost",
    },
    {
        "name": "Ignorance",
        "description": "of terrors and the unknown",
    },
    {
        "name": "Oppression",
        "description": "with rule a crushing weight",
    },
    {
        "name": "Poverty",
        "description": "where even the rich are poor",
    },
    {
        "name": "Precarity",
        "description": "with all goods made fleeting",
    },
    {
        "name": "Stratification",
        "description": "where classes do not touch",
    },
    {
        "name": "Violence",
        "description": "where life is something cheap",
    },
    {
        "name": "Enlightenment",
        "description": "where knowledge is loved",
    },
    {
        "name": "Expanse",
        "description": "where there's room for more",
    },
    {
        "name": "Hope",
        "description": "that the future should be better",
    },
    {
        "name": "Justice",
        "description": "where a reckoning is had",
    },
    {
        "name": "Legitimacy",
        "description": "where power is backed by right",
    },
    {
        "name": "Pageantry",
        "description": "of splendor and magnificence",
    },
    {
        "name": "Prosperity",
        "description": "with wealth easily had",
    },
    {
        "name": "Renewal",
        "description": "with things growing brighter",
    },
    {
        "name": "Triumph",
        "description": "with victory over a backing threat",
    },
    {
        "name": "Unity",
        "description": "where purposes are shared",
    },
]
RELATIONS = [
    {
        "name": "Taking refuge",
        "description": "Raiders are taking refuge in their lands",
    },
    {
        "name": "Ownership dispute",
        "description": "Ownership of a resource site is disputed",
    },
    {
        "name": "Sheltering criminals",
        "description": "A usurper or criminal is being sheltered there",
    },
    {
        "name": "Troublemaking religion",
        "description": "A troublemaking religion is based there",
    },
    {
        "name": "Political claim",
        "description": "Their rulers have a political claim on the throne",
    },
    {
        "name": "Diplomatic marriage",
        "description": "A diplomatic marriage is going sour",
    },
    {
        "name": "War savagery",
        "description": "A past war's savagery has left deep scars",
    },
    {
        "name": "Supplanting beliefs",
        "description": "Their culture is supplanting local beliefs",
    },
    {
        "name": "Gaining influence",
        "description": "Their immigrants are gaining great influence",
    },
    {
        "name": "Broke alliance",
        "description": "They broke off an alliance or important pact",
    },
    {
        "name": "Lured away academy",
        "description": "They lured away an academy or great temple",
    },
    {
        "name": "Blocking trade",
        "description": "Border tariffs and taxes are blocking trade",
    },
    {
        "name": "Drove terrible beast",
        "description": "They drove a terrible beast into this land",
    },
    {
        "name": "Working caused problems",
        "description": "A Working of theirs caused problems here",
    },
    {
        "name": "Great hero",
        "description": "They view us as a great peril from the past",
    },
    {
        "name": "Cooperating with enemy",
        "description": "They're cooperating with an enemy group",
    },
    {
        "name": "Backing assassinations",
        "description": "They're suspected of backing assassinations",
    },
    {
        "name": "Spy ring",
        "description": "A spy ring is suspected or has been found",
    },
    {
        "name": "Refused agreement",
        "description": "They refused to give aid for some current need",
    },
    {
        "name": "Hostile to ally",
        "description": "They've been hostile to an allied group",
    },
]
TIES = [
    {
        "name": "Related ruling classes",
        "description": "The ruling classes are related in some way",
    },
    {
        "name": "Importers of faith",
        "description": "An important faith originated there",
    },
    {
        "name": "Fought together",
        "description": "They fought by our side sometime in the past",
    },
    {
        "name": "Admired culture",
        "description": "Their culture is widely admired here",
    },
    {
        "name": "Helped overcome peril",
        "description": "They helped to overcome an eldritch peril",
    },
    {
        "name": "Took back enemy",
        "description": "They held back an enemy from our border",
    },
    {
        "name": "Co-ethnics",
        "description": "They are co-ethnics of the same origins",
    },
    {
        "name": "Critical trade",
        "description": "They provide critical trade relations",
    },
    {
        "name": "Sages and scholars",
        "description": "Sages and scholars came from there",
    },
    {
        "name": "Critical aid",
        "description": "They gave critical aid during a disaster",
    },
    {
        "name": "Hero from there",
        "description": "A hero of this land came originally from there",
    },
    {
        "name": "Ruled both",
        "description": "A past hero-king once ruled both lands",
    },
    {
        "name": "Produce commodity",
        "description": "They produce some vital commodity",
    },
    {
        "name": "Shared enemy",
        "description": "They have a shared enemy",
    },
    {
        "name": "Working here too",
        "description": "A Working they have is helpful here, too",
    },
    {
        "name": "Alliance or pact",
        "description": "A long-standing alliance or trade pact exists",
    },
    {
        "name": "Conceded land",
        "description": "They recently conceded some disputed land",
    },
    {
        "name": "Admire culture",
        "description": "They greatly admire elements of this culture",
    },
    {
        "name": "Considered attractive",
        "description": "They're considered unusually attractive here",
    },
    {
        "name": "Took in refugees",
        "description": "They took in refugees from here at one point",
    },
]
PROBLEMS = [
    {
        "name": "Farmland depleted",
        "description": "Farmland is becoming worn-out and depleted",
    },
    {
        "name": "Verminous monsters",
        "description": "Verminous monsters are swarming",
    },
    {
        "name": "Rebel front",
        "description": "A rebel front is stirring up trouble",
    },
    {
        "name": "Renegade powers",
        "description": "A renegade powers backing internal strife",
    },
    {
        "name": "Inept leadership",
        "description": "The leadership is inept and distracted",
    },
    {
        "name": "Religious reformer",
        "description": "A religious reformer is breaking old compacts",
    },
    {
        "name": "Provincial raiding",
        "description": "An outlying province is raiding",
    },
    {
        "name": "Dark cults",
        "description": "Dark cults are attracting the ambitious",
    },
    {
        "name": "Blighted horde",
        "description": "A blighted horde is threatening the borders",
    },
    {
        "name": "Ancient evil",
        "description": "An ancient evil is once more a peril",
    },
    {
        "name": "Patent artifact",
        "description": "Malcontents have obtained a potent artifact",
    },
    {
        "name": "Nation's coffers bare",
        "description": "Luxuriance has left the nation's coffers bare",
    },
    {
        "name": "Collapse of independence",
        "description": "Local potentates are collapsing independence",
    },
    {
        "name": "Important mine harmed",
        "description": "An important mine has run out or been harmed",
    },
    {
        "name": "Sinister favorite",
        "description": "A sinister favorite has infatuated the leader",
    },
    {
        "name": "Plundering monster",
        "description": "A rampaging giant beast is causing hunger",
    },
    {
        "name": "Fearsome preachers",
        "description": "Fearsome preachers are migrating into the land",
    },
    {
        "name": "Rival preparing",
        "description": "A rival is preparing for war or raiding",
    },
    {
        "name": "Grand national plan",
        "description": "A grand national plan is exhausting the people",
    },
    {
        "name": "Savage grudge",
        "description": "A savage grudge has erupted between lords",
    },
]
BOONS = [
    {
        "name": "Splendid mine found",
        "description": "A splendid mine or resource has been found",
    },
    {
        "name": "Pious saint",
        "description": "A pious saint is strengthening a major faith",
    },
    {
        "name": "Noble heir",
        "description": "A noble heir shows signs of heroic greatness",
    },
    {
        "name": "Major rival defeated",
        "description": "A major rival was recently defeated or calamity",
    },
    {
        "name": "New farmland",
        "description": "New farmland has been opened up recently",
    },
    {
        "name": "New trade route",
        "description": "A new trade route has been forged",
    },
    {
        "name": "Horrible disaster",
        "description": "A horrible monster was slain or driven off",
    },
    {
        "name": "Good harvests",
        "description": "Good harvests have enriched the people",
    },
    {
        "name": "Wicked minister deposed",
        "description": "A wicked minister has been deposed",
    },
    {
        "name": "New authority",
        "description": "A new academy has gained new fame",
    },
    {
        "name": "Bandit uprising crushed",
        "description": "A bandit or rebel uprising has been crushed",
    },
    {
        "name": "Rival lords peace",
        "description": "Two rival lords have started to make peace",
    },
    {
        "name": "Old enemy peace",
        "description": "An old enemy has agreed to a peace pact",
    },
    {
        "name": "Military victory",
        "description": "The military won a recent smashing victory",
    },
    {
        "name": "Working activated",
        "description": "A helpful Working has been activated",
    },
    {
        "name": "Powerful artifact",
        "description": "A powerful artifact is helping the ruler",
    },
    {
        "name": "Old unrest calmed",
        "description": "An old source of unrest has been calmed",
    },
    {
        "name": "Dark cult purged",
        "description": "A dark cult has been revealed and purged",
    },
    {
        "name": "New diplomatic ties",
        "description": "New diplomatic ties have been made",
    },
    {
        "name": "New lord",
        "description": "A new lord has been loved by his people",
    },
]

for item in [THEME, RELATIONS, TIES, PROBLEMS, BOONS]:
    item_selection = choice(item)
    print(f"\t{item_selection['name']}")
    print(f"\t\t{item_selection['description']}")
