from random import choice, randint

TAG = [
    {
        "name": "Antimagical",
        "description": "The faction is dwarven or of some other breed of skilled counter-sorcerers. Assets that require Medium or higher Magic to purchase roll all attribute checks twice against this faction during an Attack and take the worst roll.",
    },
    {
        "name": "Concealed",
        "description": "All Assets the faction purchases enter play with the Stealth quality.",
    },
    {
        "name": "Imperialist",
        "description": "TThe faction quickly expands its Bases of Influence. Once per turn, it can use the Expand Influence action as a special ability instead of it taking a full action.",
    },
    {
        "name": "Innovative",
        "description": "The faction can purchase Assets as if their attribute ratings were two points higher than they are. Only two such over-complex Assets may be owned at any one time.",
    },
    {
        "name": "Machiavellian",
        "description": "The faction is diabolically cunning. It rolls an extra die for all Cunning attribute checks. Its Cunning must always be its highest attribute.",
    },
    {
        "name": "Martial",
        "description": "The faction is profoundly devoted to war. It rolls an extra die for all Force attribute checks. Force must always be its highest attribute.",
    },
    {
        "name": "Massive",
        "description": "The faction is an empire, major kingdom, or other huge organizational edifice. It automatically wins attribute checks if its attribute is more than twice as big as the opposing side’s attribute, unless the other side is also Massive.",
    },
    {
        "name": "Mobile",
        "description": "The faction is exceptionally fast or mobile. Its faction turn movement range is twice what another faction would have in the same situation.",
    },
    {
        "name": "Populist",
        "description": "TThe faction has widespread popular support. Assets that cost 5 Treasure or less to buy cost one point less, to a minimum of 1.",
    },
    {
        "name": "Rich",
        "description": "The faction is rich or possessed of mercantile skill. It rolls an extra die for all Wealth attribute checks. Wealth must always be its highest attribute.",
    },
    {
        "name": "Rooted",
        "description": "The faction has very deep roots in its area of influence. They roll an extra die for attribute checks intheir headquarters location, and all rivals roll theirown checks there twice, taking the worst die.",
    },
    {
        "name": "Scavenger",
        "description": "As looters and raiders, when they destroyan enemy Asset they gain a quarter of its purchasevalue in Treasure, rounded up.",
    },
    {
        "name": "Supported",
        "description": "The faction has excellent logistical support.All damaged Assets except Bases of Influence regainone lost hit point per faction turn automatically.",
    },
    {
        "name": "Tenacious",
        "description": "The faction is hard to dislodge. When one of its Bases of Influence is reduced to zero hit points, it instead survives with 1 hit point. This trait can’t be used again on that base until it’s fully fixed.",
    },
    {
        "name": "Zealot",
        "description": "Once per turn, when an Asset fails an Attack action check, it can reroll the attribute check. It automatically takes counterattack damage from its target, however, or 1d6 if the target has less or none.",
    },
]
EXAMPLE_GOAL = [
    "Blood the Enemy",
    "Destroy the Foe",
    "Eliminate Target",
    "Expand Influence",
    "Inside Enemy Territory",
    "Invincible Valor",
    "Peaceable Kingdom",
    "Root Out the Enemy",
    "Sphere Dominance",
    "Wealth of Kingdoms",
]
CUNNING_ASSET = [
    {
        "name": "Bewitching Charmer",
        "description": "When the Bewitching Charmer succeeds in an Attack, the targeted Asset is unable to leave the same location as the Bewitching Charmer until the latter Asset moves or is destroyed. Bewitching Charmers are immune to Counterattack.",
    },
    {
        "name": "Blackmail",
        "description": "When a Blackmail asset is in a location, hostile factions can't roll more than one die during Attacks made by or against them there, even if they have tags or Assets that usually grant bonus dice.",
    },
    {
        "name": "Court Patronage",
        "description": "Powerful nobles or officials are appointing their agents to useful posts of profit. A Court Patronage Asset automatically grants 1 Treasure to its owning faction each turn.",
    },
    {
        "name": "Covert Transport",
        "description": "As a free action once per turn, the faction can pay 1 Treasure and move any Cunning or Wealth Asset at the same location as the Covert Transport. The transported Asset gains the Stealth quality until it performs some action or is otherwise utilized by the faction.",
    },
    {
        "name": "Cryptomancers",
        "description": "In place of an Attack action, they can make a Cunning vs. Cunning attack on a specific hostile Asset within one move. On a success, the targeted Asset is unable to do anything or be used for anything on its owner's next faction turn. On a failure, no Counterattack damage is taken.",
    },
    {
        "name": "Dancing Girls",
        "description": "Dancing Girls or other charming distractions are immune to Attack or Counterattack damage from Force Assets, but they cannot be used to defend against Attacks from Force Assets.",
    },
    {
        "name": "Expert Treachery",
        "description": "On a successful Attack by Expert Treachery, this Asset is lost, 5 Treasure is gained by its owning faction, and the Asset that Expert Treachery targeted switches sides. This conversion happens even if their new owners lack the attributes usually necessary to maintain their new Asset.",
    },
    {
        "name": "Hired Friends",
        "description": "As a free action, once per turn, the faction may spend 1 Treasure and grant a Wealth Asset within one turn's movement range the Subtle quality. This quality will remain, regardless of the Wealth Asset's movement, until the Hired Friends are destroyed or they use this ability again.",
    },
    {
        "name": "Idealistic Thugs",
        "description": "Easily-manipulated hotheads are enlisted under whatever ideological or religious principle best enthuses them for violence.",
    },
    {
        "name": "Informers",
        "description": "As a free action, once per turn, the faction can spend 1 Treasure and have the Informers look for Stealthed Assets. To do so, the Informers pick a faction and make a Cunning vs. Cunning Attack on them. No counterattack damage is taken if they fail, but if they succeed, all Stealthed Assets of that faction within one move of the Informers are revealed.",
    },
    {
        "name": "Interrupted Logistics",
        "description": "Non-Stealthed hostile units cannot enter the same location as the Interrupted Logistics Asset without paying 1d4 Treasure and waiting one turn to arrive there.",
    },
    {
        "name": "Just As Planned",
        "description": "Some sublimely cunning mastermind ensures that the schemes of this faction are unimaginably subtle and far-seeing. Whenever the faction's Assets make a roll involving Cunning, they may reroll a failed check at the cost of inflicting 1d6 damage on Just As Planned. This may be done repeatedly, though it may destroy the Asset. There is no range limit on this benefit.",
    },
    {
        "name": "Mindbenders",
        "description": "Once per turn as a free action, the Mindbenders can force a rival faction to reroll a check, Attack, or other die roll they just made and take whichever result the Mindbenders prefer. A faction can only be affected this way once until the start of the Mindbender's faction's next turn.",
    },
    {
        "name": "Occult Infiltrators",
        "description": "Magically-gifted spies and assassins are enlisted to serve the faction. Occult Infiltrator Assets always begin play with the Stealth quality.",
    },
    {
        "name": "Omniscient Seers",
        "description": "At the start of their turn, each hostile Stealthed asset within one turn's movement of the Omniscient Seers must succeed in a Cunning vs. Cunning check against the owning faction or lose their Stealth. In addition, all Cunning rolls made by the faction for units or events within one turn's movement of the seers gain an extra die.",
    },
    {
        "name": "Organization Moles",
        "description": "Sleeper agents and deep-cover spies burrow into hostile organizations, waiting to disrupt them from within when ordered to do so.",
    },
    {
        "name": "Petty Seers",
        "description": "A cadre of skilled fortune-tellers and minor oracles have been enlisted by the faction to foresee perils and allow swift counterattacks.",
    },
    {
        "name": "Popular Movement",
        "description": "Any friendly Asset is allowed movement into the same location as the Popular Movement, even if it would normally be forbidden by its owners and lacks the Subtle quality. If the Popular Movement later moves or is destroyed, such Assets must also leave or suffer the usual consequences of a non-Subtle Asset in a hostile area.",
    },
    {
        "name": "Prophet",
        "description": "Whether a religious prophet, charismatic philosopher, rebel leader, or other figure of popular appeal, the Asset is firmly under the faction's control.",
    },
    {
        "name": "Saboteurs",
        "description": "An Asset that is Attacked by the Saboteurs can't use any free action abilities it may have during the next turn, whether or not the Attack was successful.",
    },
    {
        "name": "Seditionists",
        "description": "In place of an Attack action, the Seditionists' owners may spend 1d4 Treasure and attach the Asset to a hostile Asset in the same location. Until the Seditionists are destroyed, infest another Asset, or leave the same location, the rebelling Asset cannot be used for anything and grants no benefits.",
    },
    {
        "name": "Shapeshifters",
        "description": "As a free action once per turn, the faction can spend 1 Treasure and grant the Shapeshifters the Stealth quality.",
    },
    {
        "name": "Smugglers",
        "description": "As a free action, once per faction turn, the Smugglers can move any allied Wealth or Cunning Asset in their same location to a destination within movement range, even if the destination wouldn't normally allow an un-Subtle Asset to locate there.",
    },
    {
        "name": "Spymaster",
        "description": "A veteran operative runs a counterintelligence bureau in the area and formulates offensive schemes for the faction.",
    },
    {
        "name": "Underground Roads",
        "description": "A well-established network of secret transit extends far around this Asset. As a free action, the faction may pay 1 Treasure and move any friendly Asset from a location within one round's move of the Underground Roads to a destination also within one round's move of the Roads.",
    },
    {
        "name": "Useful Idiots",
        "description": "Hirelings, catspaws, foolish idealists, and other disposable minions are gathered together in this Asset. If another Asset within one turn's move of the Useful Idiots is struck by an Attack, the faction can instead sacrifice the Useful Idiots to negate the attack. Only one band of Useful Idiots can be sacrificed on any one turn.",
    },
    {
        "name": "Vigilant Agents",
        "description": "A constant flow of observations runs back to the faction from these watchful counterintelligence agents. Whenever another faction moves a Stealthed asset into a location within one move's distance from the Vigilant Agents, they may make a Cunning vs. Cunning attack against the owning faction. On a success, the intruding Asset loses its Stealth after it completes the move.",
    },
]
FORCE_ASSET = [
    {
        "name": "Apocalypse Engine",
        "description": "One of a number of hideously powerful ancient super-weapons unearthed from some lost armory, an Apocalypse Engine rains some eldritch horror down on a targeted enemy Asset.",
    },
    {
        "name": "Brilliant General",
        "description": "A leader for the ages is in service with the faction. Whenever the Brilliant General or any allied Force Asset in the same location Attacks or is made to defend, it can roll an extra die to do so.",
    },
    {
        "name": "Cavalry",
        "description": "Mounted troops, chariots, or other mobile soldiers are in service to the faction. While weak on defense, they can harry logistics and mount powerful charges.",
    },
    {
        "name": "Demonic Slayer",
        "description": "Powerful sorcerers have summoned or constructed an inhuman assassin-beast to hunt down and slaughter the faction's enemies. A Demonic Slayer enters play Stealthed.",
    },
    {
        "name": "Enchanted Elites",
        "description": "A carefully-selected group of skilled warriors are given magical armaments and arcane blessings to boost their effectiveness.",
    },
    {
        "name": "Fearful Intimidation",
        "description": "Judicious exercises of force have intimidated the locals, making them reluctant to cooperate with any group that stands opposed to the faction.",
    },
    {
        "name": "Fortification Program",
        "description": "A program of organized fortification and supply caching has been undertaken around the Asset's location, hardening allied communities and friendly Assets. Once per turn, when an enemy makes an Attack that targets the faction's Force rating, the faction can use the Fortification Program to defend if the Asset is within a turn's move from the attack.",
    },
    {
        "name": "Guerrilla Populace",
        "description": "The locals have the assistance of trained guerrilla warfare leaders who can aid them in sabotaging and attacking unwary hostiles.",
    },
    {
        "name": "Infantry",
        "description": "Common foot soldiers have been organized and armed by the faction. While rarely particularly heroic in their capabilities, they have the advantage of numbers.",
    },
    {
        "name": "Invincible Legion",
        "description": "The faction has developed a truly irresistible military organization that can smash its way through opposition without the aid of any support units. During a Relocate Asset action, the Invincible Legion can relocate to locations that would otherwise not permit a formal military force to relocate there, as if it had the Subtle quality. It is not, however, in any way subtle.",
    },
    {
        "name": "Knights",
        "description": "Elite warriors of considerable personal prowess have been trained or enlisted by the faction, either from noble sympathizers, veteran members, or amenable mercenaries.",
    },
    {
        "name": "Local Guard",
        "description": "Ordinary citizens are enlisted into night watch patrols and local guard units. They're most effective when defending from behind a fortified position, but they have some idea of how to use their weapons.",
    },
    {
        "name": "Magical Logistics",
        "description": "An advanced web of magical Workings, skilled sorcerers, and trained logistical experts are enlisted to streamline the faction's maintenance and sustain damaged units. Once per faction turn, as a free action, the Asset can repair 2 hit points of damage to an allied Force Asset.",
    },
    {
        "name": "Military Roads",
        "description": "The faction has established a network of roads with a logistical stockpile at this Asset's location. As a consequence, once per faction turn, the faction can move any one Asset from any location within its reach to any other location within its reach at a cost of 1 Treasure.",
    },
    {
        "name": "Military Transport",
        "description": "A branch of skilled teamsters, transport ships, road-building crews, or other logistical facilitators is in service to the faction. As a free action once per faction turn, it can bring an allied Asset to its location, provided they're within one turn's movement range, or move an allied Asset from its own location to a target also within a turn's move. Multiple Military Transport assets can chain this movement over long distances.",
    },
    {
        "name": "Purity Rites",
        "description": "A rigorous program of regular mental inspection and counterintelligence measures has been undertaken by the faction. This Asset can only defend against attacks that target the faction's Cunning, but it allows the faction to roll an extra die to defend.",
    },
    {
        "name": "Reserve Corps",
        "description": "Retired military personnel and rear-line troops are spread through the area as workers or colonists, available to resist hostilities as needed.",
    },
    {
        "name": "Scouts",
        "description": "Long-range scouts and reconnaissance experts work for the faction, able to venture deep into hostile territory.",
    },
    {
        "name": "Siege Experts",
        "description": "These soldiers are trained in trenching, sapping, and razing targeted structures. When they successfully Attack an enemy Asset, the owner loses 1d4 points of Treasure from their reserves and this faction gains it.",
    },
    {
        "name": "Summoned Hunter",
        "description": "A skilled sorcerer has summoned a magical beast or mentally bound a usefully disposable assassin into the faction's service.",
    },
    {
        "name": "Temple Fanatics",
        "description": "Fanatical servants of a cult, ideology, or larger religion, these enthusiasts wreak havoc on enemies without a thought for their own lives. After every time the Temple Fanatics defend or successfully attack, they take 1d4 damage.",
    },
    {
        "name": "Thugs",
        "description": "These gutter ruffians and common kneebreakers have been organized in service to the faction's causes.",
    },
    {
        "name": "Vanguard Unit",
        "description": "This unit is specially trained to build bridges, reduce fortifications, and facilitate a lightning strike into enemy territory. When its faction takes a Relocate Asset turn, it can move the Vanguard Unit and any allied units at the same location to any other location within range, even if the unit type would normally be prohibitive from moving there. Thus, a Force asset could be moved into a foreign nation's territory even against their wishes. The unit may remain at that location afterwards even if the Vanguard Unit leaves.",
    },
    {
        "name": "War Fleet",
        "description": "While a war fleet can only Attack assets and locations within reach of the waterways, once per turn it can freely relocate itself to any coastal area within movement range. The Asset itself must be based out of some landward location to provide for supply and refitting.",
    },
    {
        "name": "War Machines",
        "description": "Mobile war machines driven by trained beasts or magical motive power are under the faction's control.",
    },
    {
        "name": "Warshaped",
        "description": "The faction has the use of magical creatures designed specifically for warfare, or ordinary humans that have been greatly altered to serve the faction's needs. Such forces are few and elusive enough to evade easy detection.",
    },
    {
        "name": "Witch Hunters",
        "description": "Certain personnel are trained in sniffing out traitors and spies in the organization, along with the presence of hostile magic or hidden spellcraft.",
    },
]
WEALTH_ASSET = [
    {
        "name": "Ancient Mechanisms",
        "description": "Some useful magical mechanism from ages past has been refitted to be useful in local industry. Whenever an Asset in the same location must roll to make a profit, such as Farmers or Manufactory, the faction may roll the die twice and take the better result.",
    },
    {
        "name": "Ancient Workshop",
        "description": "A workshop has been refitted with ancient magical tools, allowing prodigies of production, albeit not always safely. As a free action, once per turn, the Ancient Workshop takes 1d6 damage and the owning faction gains 1d6 Treasure.",
    },
    {
        "name": "Arcane Laboratory",
        "description": "The faction's overall Magic is counted as one step higher for the purposes of creating Assets in the same location as the laboratory. Multiple Arcane Laboratories in the same location can increase the Magic boost by multiple steps.",
    },
    {
        "name": "Armed Guards",
        "description": "Hired caravan guards, bodyguards, or other armed minions serve the faction.",
    },
    {
        "name": "Caravan",
        "description": "As a free action, once per turn, the Caravan can spend 1 Treasure and move itself and one other Asset in the same place to a new location within one move.",
    },
    {
        "name": "Cooperative Businesses",
        "description": "If any other faction attempts to create an Asset in the same location as a Cooperative Business, the cost of doing so increases by 1 Treasure. This penalty stacks.",
    },
    {
        "name": "Dragomans",
        "description": "Interpreters, cultural specialists, and go-betweens simplify the expansion of a faction's influence in an area. A faction that takes an Expand Influence action in the same location as this Asset can roll an extra die on all checks there that turn. As a free action once per turn, this Asset can move.",
    },
    {
        "name": "Economic Disruption",
        "description": "As a free action once per turn, this Asset can move itself without cost.",
    },
    {
        "name": "Farmers",
        "description": "Farmers, hunters, and simple rural artisans are in service to the faction here. Once per turn, as a free action, the Asset's owner can roll 1d6; on a 5+, they gain 1 Treasure from the Farmers.",
    },
    {
        "name": "Free Company",
        "description": "Hired mercenaries and professional soldiers, this Asset can, as a free action once per turn, move itself. At the start of each of its owner's turn, it takes 1 Treasure in upkeep costs; if this is not paid, roll 1d6. On a 1-3 the Asset is lost, on a 4-6 it goes rogue and will move to Attack the most profitable-looking target. This roll is repeated each turn until back pay is paid or the Asset is lost.",
    },
    {
        "name": "Front Merchant",
        "description": "Whenever the Front Merchant successfully Attacks an enemy Asset, the target faction loses 1 Treasure, if they have any, and the Front Merchant's owner gains it. Such a loss can occur only once per turn.",
    },
    {
        "name": "Golden Prosperity",
        "description": "Each turn, as a free action, the faction gains 1d6 Treasure that can be used to fix damaged Assets as if by the Repair Assets action. Any of this Treasure not spent on such purposes is lost.",
    },
    {
        "name": "Healers",
        "description": "Whenever an Asset within one move of the Healers is destroyed by an Attack that used Force against the target, the owner of the Healers may pay half its purchase price in Treasure, rounded up, to instantly restore it with 1 hit point. This cannot be used to repair Bases of Influence.",
    },
    {
        "name": "Hired Legion",
        "description": "As a free action once per turn, the Hired Legion can move. This faction must be paid 2 Treasure at the start of each turn as upkeep, or else they go rogue as the Free Company Asset does. This Asset cannot be voluntarily sold or disbanded.",
    },
    {
        "name": "Lead or Silver",
        "description": "If Lead or Silver's Attack reduces an enemy Asset to zero hit points, this Asset's owner may immediately pay half the target's purchase cost to claim it as their own, reviving it with 1 hit point.",
    },
    {
        "name": "Mad Genius",
        "description": "As a free action, once per turn, the Mad Genius may move. As a free action, once per turn, the Mad Genius may be sacrificed to treat the Magic rating in their location as High for the purpose of buying Assets that require such resources. This boost lasts only until the next Asset is purchased in that location.",
    },
    {
        "name": "Manufactory",
        "description": "Once per turn, as a free action, the Asset's owner may roll 1d6; on a 1, one point of Treasure is lost, on a 2-5, one point is gained, and on a 6, two points are gained. If Treasure is lost and none is available to pay it by the end of the turn, this Asset is lost.",
    },
    {
        "name": "Merchant Prince",
        "description": "A canny master of trade, the Merchant Prince may be triggered as a free action once per turn before buying a new Asset in the same location; the Merchant Prince takes 1d4 damage and the purchased Asset costs 1d8 Treasure less, down to a minimum of half its normal price.",
    },
    {
        "name": "Monopoly",
        "description": "Once per turn, as a free action, the Monopoly Asset can target an Asset in the same location; that Asset's owning faction must either pay the Monopoly's owner 1 Treasure or lose the targeted Asset.",
    },
    {
        "name": "Occult Countermeasures",
        "description": "This asset can only Attack or inflict Counterattack damage on Assets that require at least a Low Magic rating to purchase.",
    },
    {
        "name": "Pleaders",
        "description": "Whether lawyers, skalds, lawspeakers, sage elders, or other legal specialists, Pleaders can turn the local society's laws against the enemies of the faction. However, Pleaders can neither Attack nor inflict Counterattack damage on Force Assets.",
    },
    {
        "name": "Smuggling Fleet",
        "description": "Once per turn, as a free action, they may move themselves and any one Asset at their current location to any other water-accessible location within one move. Any Asset they move with them gains the Subtle quality until they take some action at the destination.",
    },
    {
        "name": "Supply Interruption",
        "description": "As a free action, once per turn, the Asset can make a Cunning vs. Wealth check against an Asset in the same location. On a success, the owning faction must sacrifice Treasure equal to half the target Asset's purchase cost, or else it is disabled and useless until this price is paid.",
    },
    {
        "name": "Trade Company",
        "description": "Bold traders undertake potentially lucrative- or catastrophic- new business opportunities. As a free action, once per turn, the owner of the Asset may roll accept 1d4 damage done to the Asset in exchange for earning 1d6-1 Treasure points.",
    },
    {
        "name": "Transport Network",
        "description": "A vast array of carters, ships, smugglers, and official caravans are under the faction's control. As a free action the Transport Network can spend 1 Treasure to move any friendly Asset within two moves to any location within one move of either the target or the Transport Network.",
    },
    {
        "name": "Usurers",
        "description": "Moneylenders and other proto-bankers ply their trade for the faction. For each unit of Usurers owned by a faction, the Treasure cost of buying Assets may be decreased by 2 Treasure, to a minimum of half its cost. Each time the Usurers are used for this benefit, they suffer 1d4 damage from popular displeasure.",
    },
    {
        "name": "Worker Mob",
        "description": "The roughest, most brutal laborers in service with the faction have been quietly organized to sternly discipline the enemies of the group.",
    },
]

tag = choice(TAG)
print(f"Tag:\t{tag['name']}")
print(f"Goal:\t{choice(EXAMPLE_GOAL)}")

if randint(0, 1) > 0:
    cunning = choice(CUNNING_ASSET)
    print(f"Cunning Asset:\t{cunning['name']}")

if randint(0, 1) > 0:
    force = choice(FORCE_ASSET)
    print(f"Force Asset:\t{force['name']}")

if randint(0, 1) > 0:
    wealth = choice(WEALTH_ASSET)
    print(f"Wealth Asset:\t{wealth['name']}")
