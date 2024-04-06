backgrounds = [
    "Aurifex",
    "Barber-Surgeon",
    "Beast Handler",
    "Bone Keeper",
    "Cutpurse",
    "Field Warden",
    "Fletchwind",
    "Foundling",
    "SCIENTIST",
    "SOLDIER",
    "STAR-TOUCHED",
    "BOUNTY HUNTER",
]

aurifex_tables = [
    {
        "name": "What experiment went horribly wrong?",
        "options": {
            1: "There was an explosion, and you lost your sense of smell. Well, almost: you can sniff out gold as a pig does truffles. Take a <b>Tin of Snuff</b> (6 uses) to dampen the impact. Use it every day or become deprived.",
            2: "You dematerialized a beloved pet. Now it follows you around, invisible but always present. Although it cannot interact with the physical realm, you are able to share its senses (add a Fatigue each time). It follows basic commands.",
            3: "You were exposed to a long-acting truth serum whose effects have yet to wear off. The disorder has its advantages: you cannot repeat lies you’ve heard, either.",
            4: "You were adept at creating fake gold, which is almost as good. Eventually, your ruse was discovered and you had to make a hasty retreat. Take a heavy Metal Ingot and Gold Powder (3 uses).",
            5: "Your recipe worked, but a rival stole the blueprint before your claims could be proven. Take a prototype Blunderbuss (d12, blast, bulky) and a taste for revenge.",
            6: "Ridiculed for discovering how to turn gold into lead, you were a laughing stock. Take a bottle of Universal Solvent (2 uses) that dissolves anything it touches into its constituent parts.",
        },
    },
    {
        "name": "What alchemical marvel is the product of your latest ingenuity?",
        "options": {
            1: "<b>Pyrophoric Gel:</b> A sticky green fluid that catches fire when exposed to air, then burns for 8 hours. Cannot be extinguished (1 use).",
            2: "<b>Blast Sphere</b>: A head-sized iron ball filled with explosive powder that explodes on impact (d12, blast, bulky, 1 use).",
            3: "<b>Aqua Vita</b>: Purifies any liquid, converting it to pure water. Drinking it cures 1d6 STR (1 use).",
            4: "<b>Mimic Stone</b>: Records a short phrase that can later be played back.",
            5: "<b>Spark Dust</b>: Ignites easily and quickly. Useful for starting a fire or as an incendiary device (3 uses).",
            6: "<b>Homunculus</b>: A miniature clay replica of yourself that follows your every command to the letter. It hates being enthralled to you and complains bitterly whenever possible. Any damage done to the homunculus is also done to you.",
        },
    },
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Lantern",
        "Oil Can (6 uses)",
        "Needle-Knife (d6)",
        "Protective Gloves (petty)",
    ],
    # profile
    """You are an artisan of the arcane, a smith of subtle forces. In the crucible of your
workshop, the laws that govern this world are warped to suit your needs.""",
    # names
    [
        "Hestia",
        "Basil",
        "Rune",
        "Prism",
        "Ember",
        "Quintess",
        "Aludel",
        "Mordant",
        "Salaman",
        "Jazia",
    ],
]

barber_surgeon_tables = [
    {
        "name": "How have you “improved” yourself?",
        "options": {
            1: """You have a replacement eye that can magnify objects, acts as a telescope,
and provides minimal night vision. You cannot wear anything metal on
your head, and strong magnets make you deprived.""",
            2: """One foot is mostly metal (kick, d6), and you treat some Tough Terrain
as Easy. Carry an Oil Can (6 uses). Without a daily application you are
deprived and noisy.""",
            3: """One of your fingers has been swapped, the bone replaced by gold and
iron. Take a Hook and a Screwdriver that can attach to the fingertip.""",
            4: """Both ears have been surgically enhanced, tripling your hearing. You can
focus on a specific sound at a great distance, such as a conversation. You
wear an ear flap to protect against sudden loud noises (WIL save to avoid
temporary paralysis).""",
            5: """Your chest is lined with alchemical sigils, toughening the skin (1 Armor).
Wearing other metallic armor nullifies the effect.""",
            6: """One arm is fully metal, and comes off at the shoulder. It can be used as a
weapon (d8, bulky when not attached) and can move independently if you
are within sight of it.""",
        },
    },
    {
        "name": "What rare tool is essential to your work?",
        "options": {
            1: """Regrowth
SalveRegrows a body part over the course of a day (1 use).""",
            2: """GraftgrubA small worm that can fuse inanimate objects with parts
of the body (1 use).""",
            3: """WoundwaxHeals wounds from fire or chemicals (restoring full STR),
but nothing else (2 uses).""",
            4: """QuicksilverA stimulant. Go first in combat, and automatically pass any
WIL saves for one hour. Addictive: Save STR or become
deprived after 24 hours without it (4 uses).""",
            5: """Pneuma
PumpPortable iron lungs (bulky). Enables life-saving surgery, or
underwater breathing.""",
            6: """LodestoneDraws out dangerous elements from the body, and acts as
a powerful magnetic force.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Amputation Knife (d6)",
        "Bandages (3 uses)",
        "Leech (restores 1 STR, 3 uses)",
        "Stained Medical Finery (petty)",
    ],
    # profile
    """You walk the line between healer and harrower, knowing the frailty of the flesh
but also the secrets that lay within. With the right tools, life and death are merely
words.""",
    # names
    [
        "Wilmot",
        "Patch",
        "Lancet",
        "Sawbones",
        "Theo",
        "Cutwell",
        "Humor",
        "Landsford",
        "Goodeye",
        "Johanna",
    ],
]


beast_handler_tables = [
    {
        "name": "What creature is your specialty?",
        "options": {
            1: "Arachnids</b>: Take a Quick-Flame Rod and an Oil Can (6 uses). It can destroy a large spider nest in seconds.",
            2: "<b>Felines</b>: Take a sack of Whiskerwort. Its odor can calm and control even the largest of cats.",
            3: "<b>Canines</b>: Take a wreath of Wolfsbane and a Large Net. Also effective against werewolves!",
            4: "<b>Birds</b>: Take a Warble-Whistle (3 charges). It can imitate any bird call, and can even be used to send simple messages.  Recharge: Feed a baby bird as its mother would, then blow.",
            5: "<b>Rodents</b>: Take a Windpipe that emits a high-pitched sound that only rodents can hear. So long as you play, they will follow. Even to their deaths.",
            6: "<b>Serpents</b>: Take a Warming Stone that generates an irresistible heat, and a vial of Antitoxin (2 uses).",
        },
    },
    {
        "name": "What do creatures of the wild understand that your kind do not?",
        "options": {
            1: """There is far more to the world than meets the eye. With quiet
concentration, you can borrow the senses of a nearby creature of your
specialty.""",
            2: """The behavior of beasts is a language in itself. When observing beasts of
your specialty, you gain insight into weather patterns and impending
disasters.""",
            3: """The pulse of the hunt is a powerful impulse. You have a sense for when
predators, even those not of your specialty, are near.""",
            4: """You know some lands intimately. Your chance of becoming lost in a
terrain dominated by the beasts of your specialty is reduced by one step
(e.g. 4-in-6 becomes 3-in-6).""",
            5: """Nature’s symphony can be heard if you attune to its rhythm. When
surrounded by creatures of your specialty they can alert you to
approaching danger before it arrives.""",
            6: """Survival is about adaptability. Once per day, you may take on a simple
feature from a creature of your speciality (webbed fingers, night vision,
etc.). Add a Fatigue each time.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Leather Whip (d6)",
        "Soporific Darts (STR save or fall asleep, 6 uses)",
        "Lure",
        "Rope (25ft)",
    ],
    # profile
    """You alone can walk among the creatures of the wild, fearless and in control. You
share a connection with animals that others can only dream of...so long as you
don’t become their snack.""",
    # names
    [
        "Amara",
        "Wulf",
        "Mireille",
        "Soren",
        "Freki",
        "Aster",
        "Gerrik",
        "Boreas",
        "Delphine",
        "Matheus",
    ],
]

bonekeeper_tables = [
    {
        "name": "What did you take from the dead?",
        "options": {
            1: """<b>Paired Sudo-Collars:</b> Highly unethical metal collars with a subject-object relationship. If
you can get another living being to wear one, they pretty much do what you want. Make a
opposed WIL save every day to maintain control.""",
            2: """<b>Hummingbird Knife:</b> (D6, Vorpal) Vibrates at subsonic frequencies. Illegal.""",
            3: """<b>Loyal Sidekick: Create a freelancer. You’ve been through thick and thin together. Think
about how you met.""",
            4: """<b>Hacking Sleeve:</b> Mechanized gauntlet with tools to hack, slice, and infiltrate just about
any system or mechanical device. 1 fatigue when successfully used.""",
            5: """<b>Custom Cape:</b> (Reaction rolls are always one category higher) Flamboyant design of your
choice. Looking good is part of the job.""",
            6: """<b>Moon Gum:</b> Tastes great. Causes intense hallucinations for 1d6 hours and is effectively
immobilizing. Pretty colors… (6 sticks left)""",
        },
    },
    {
        "name": "What tool was invaluable in your work?",
        "options": {
            1: """<b>A Crow-Shaped Amulet</b>. You can ask a question of the dead, but must add a <b>Fatigue</b> each time.""",
            2: """A <b>mortal wound</b> from a freed revenant. You were healed, but the
disfigurement has made you a pariah. You require neither air nor
sustenance, but are still subject to pain and death. Trapped between, the
dead see you as one of their own.""",
            3: """A <b>Blood Pail</b> <em>(bulky)</em> from a local death-cult. Empty its contents to
summon a creature built from items buried below (bones, rocks, pottery,
etc). It obeys your command, but if destroyed you permanently lose 1d4
STR. It has 6 HP, 1 Armor, 13 STR, 11 DEX, 4 WIL, shard fists (d8). <b>Recharge</b>:
Fill the bucket with the blood of a dying warrior.""",
            4: """A <b>Burial Wagon</b> (+6 slots) from your last job. It came with a stubborn old <b>Donkey</b> (+4 slots, +2 slots if pulling wagon, <em>slow</em>).""",
            5: """
The Detect Magic <b>Spellbook</b>, stolen from an ancient library. Your family
worked in service to an obscure underworld deity, but you lost your faith.
Though exiled, you continue to serve, even as an apostate.
<em><b>Detect Magic</b></em>: You can see or hear nearby magical auras.""",
            6: """
A <b>Plague Doctor’s Mask</b>, after its owner succumbed to the disease that
wiped out everyone you once knew. They should have kept it on.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Lantern",
        "Oil Can (6 uses)",
        "Stake (d6)",
        "Chains (10ft)",
    ],
    # Profile
    """You are a shepherd to the departed. You listen to the final whispers of the dead as
they descend into the cold, unyielding earth. You know that to fully celebrate the
gift of life, we must honor its finale as well.""",
    # names
    [
        "Rook",
        "Ebon",
        "Moro",
        "Yew",
        "Pall",
        "Leth",
        "Nix",
        "Barnaby",
        "Vesper",
        "Leder",
    ],
]

cutpurse_tables = [
    {
        "name": "What was your last big job?",
        "options": {
            1: """A noble’s summer home. The place was full of fancy wine (+20gp) but not much else. Take <b>Fence Cutters</b>.""",
            2: """A bank (you were caught). You bear a brand only visible by firelight, and
anyone that sees the mark can ask you for a beer. Take <b>Retractable Wires</b>.""",
            3: """A guild warehouse. Take a <b>Ladder</b> (<em>bulky</em>, 10ft) and <b>Blinding Powder</b> (1 use).""",
            4: """
Moneylender. Someone beat you to the job, but left behind a <b>Scroll</b> of
<em>Arcane Eye</em> (petty).
<em><b>Arcane Eye</b></em>: You can see through a magical floating eyeball that flies around at your command.""",
            5: """Constable’s quarters. You escaped, but left some friends behind. Take
<b>Strong Silk Rope</b> and a queasy feeling.""",
            6: """A university. You were seen, but not pursued. You still don’t know why.
Take <b>Smoke Pellets</b> (3 uses).""",
        },
    },
    {
        "name": "What helps you steal?",
        "options": {
            1: """<b>Catring</b> 2 charges. Climb up walls and fall safely. Recharge: Place the ring on a stray cat’s tail.""",
            2: """<b>Gildfinger</b> 1 charge. A finger glove that mimics any mundane key.
Recharge: Bundle it with at least 100gp for a night.""",
            3: """<b>Glimpse
Glass</b> 3 charges. A monocle that lets you see through walls or
other obstructions. It shatters after the last use.""",
            4: """<b>Sweetwhistle1 charge</b>. Listeners hear a soft, familiar voice in the
distance that they cannot resist following. Recharge: Lose
a dear memory (describe it).""",
            5: """<b>Vagrant’s
Veil</b> 1 charge. Wear it to blend seamlessly into crowds,
appearing as a simple pauper. Recharge: Donate all the
day’s winnings to the poor (Petty).""",
            6: """<b>Smokestack
Marble</b> 3 uses. Crush to release a dense cloud of smoke that
follows you (Petty).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Twin Daggers (d6+d6, bulky)",
        "Padded Leather (1 Armor)",
        "Lockpicks",
        "Black Outfit (petty)",
    ],
    # profile
    """You live in the grey space between those who have power and
those who don’t. You find opportunity where others see
only chaos. With nimble fingers, you unburden both the
richest merchant and the lowliest guard.""",
    # names
    [
        "Sable",
        "Lyra",
        "Eamon",
        "Salina",
        "Elara",
        "Freya",
        "Isolde",
        "Sparrow",
        "Ivy",
        "Silas",
    ],
]

field_warden_tables = [
    {
        "name": "What got the better of you?",
        "options": {
            1: """A voracious swarm of pests that swallowed crops and animals alike. With
nothing to defend, you left. Take <b>Gale Seed Extract</b> (3 uses). Ingesting one
lets you sprint with a speed four times your regular rate. Afterward you
add two <b>Fatigue</b>.""",
            2: """A crop spirit, angered by a poor tithing. The fires consumed nearly
everything, and afterwards you were able to gather a pouch of <b>Fireseeds</b>
(d8, <em>blast</em>, 4 uses).""",
            3: """An antlered, toothy demon that nearly ended you. Take a <b>blood-stained
bone knife</b> (d6). On critical damage, its next attack becomes <em>enhanced</em>
from contact with blood.""",
            4: """<em>The Withering</em>, a type of stem rot from <b>The Roots</b>. Take a <b>Diseased Crop</b>
(6 uses) that decays any plant it touches.""",
            5: """Wolves, or so you thought. You are now a <b>Werewolf</b> [8 HP, 15 STR, 14 DEX,
claws (d6+d6) or bite (d8)]. Your WIL remains the same. You can turn at
will (once per day) but must make a WIL save to revert. Anyone left alive
from your attacks must make a WIL save to avoid infection.""",
            6: """Crop thieves. Not all of them survived, but you were outnumbered. Take a
+d4 HP and a <b>Hilted Broadsword</b> (d8, <em>bulky</em>).""",
        },
    },
    {
        "name": "What tool saved your life?",
        "options": {
            1: """<b>Bloodvine Whip</b> d8 damage. On Critical Damage it drains the target’s
blood, granting the weapon’s next attack the blast quality.""",
            2: """<b>Clatter Keeper</b> A hand-cranked device that emits a loud noise, frightening
away most creatures.""",
            3: """<b>Sun Stick</b> Provides ample warmth and light for up to one hour (1
use). <b>Recharge:</b> Leave in heavy sunlight for a full day.""",
            4: """<b>Root Tether</b> When thrown, binds up to a wolf-sized creature to the soil
for a short time.""",
            5: """<b>Greenwhistle</b> A small flute that calms plants, making passage through
areas heavy with plant life a bit easier.""",
            6: """<b>Everbloom Band</b> A circlet adorned with flowers that never wilt. On taking
<b>Critical Damage</b> the flowers dissolve into dust, but you
act as if your save succeeded (STR loss still occurs).""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Brigandine (1 Armor, <em>bulky</em>)",
        "Sling (d6)",
        "Hand Axe (d6)",
        "Repellent (state the creature, 3 uses)",
    ],
    # profile
    """Protectors of the harvest, defense against pests, thieves, and beasts. A position of
great honor, while it lasts: many guardians do not live out their natural lives.
Roll a second time on the <b>Bonds</b> table.""",
    # names
    [
        "Seed",
        "Thresh",
        "Dibber",
        "Sow",
        "Stalk",
        "Harrow",
        "Cobb",
        "Flax",
        "Briar",
        "Rye",
    ],
]

fletchwind_tables = [
    {
        "name": "How did you earn your bow?",
        "options": {
            1: """<b>War</b>. If you are first to attack, your bow gains the blast property for the
first round.""",
            2: """<b>Falconry</b>. You keep a falcon [3 hp, 5 STR, 16 DEX, 4 WIL, claws (d6+d6),
bite (d6)]. It only eats live game.""",
            3: """<b>Hunting.</b> When taking the Supply (pg. 80) action your ability to secure
Rations increases by one step (e.g. 1d4 becomes 1d6).""",
            4: """<b>Tournaments.</b> Attacks with your bow are enhanced if the target is
immobile.""",
            5: """<b>Training.</b> If you are the first to attack, melee attacks against you are
impaired until you take STR damage.""",
            6: """<b>Scouting.</b> When taking the Travel (pg. 80) action, your presence decreases
the chance of getting lost by one step (e.g. 4-in-6 becomes 3-in-6).""",
        },
    },
    {
        "name": "What kind of wood is your bow made from?",
        "options": {
            1: """<b>Western Yew</b> (d6, <em>bulky</em>). Can be wielded as a blunt weapon (d6). Noisy.""",
            2: """<b>Sessile Oak</b> (d8, <em>bulky</em>). Slams into targets. On critical damage, something is torn off.""",
            3: """<b>Stone Pine</b> (d6, <em>bulky</em>). Produces one use of Sticky Sap per day. It is highly explosive.""",
            4: """<b>White Ash</b> (d6, <em>bulky</em>). Can be used in place of a shield in melee combat (+1 Armor).""",
            5: """<b>Striped Bamboo</b> (d6). Collapsible, it only requires one slot (but still requires both hands).""",
            6: """<b>Wych Elm</b> (d6, <em>bulky</em>). Protects the bearer from poisons and toxins, so long as they are holding it.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Bow (see table)",
        "Serrated Knife (d6)",
        "Boiled Leather (1 Armor)",
        "Heartroot Salve (restores 1d4 STR, 1 use)",
    ],
    # profile
    """You strike from afar, but that does not make you a coward. You are a musician,
the song of your bowstring nought but a warning, singing the silent promise of a
quick death.""",
    # names
    [
        "Flint",
        "Feather",
        "Crier",
        "Thunder",
        "Falcon",
        "Pluck",
        "Needle",
        "Warsong",
        "Hawk",
        "Cai",
    ],
]

foundling_tables = [
    {
        "name": "Who took you in?",
        "options": {
            1: """An old hunter. You were both quite happy, until it all ended. Take a
<b>Weathered Longbow</b> (d8, <em>bulky</em>) and a <b>Leather Jerkin</b> (1 Armor).""",
            2: """A wizened apothecary, who taught you the healing arts but maintained a
clinical detachment. Take a <b>Healing Ungent</b> (restores d4 STR).""",
            3: """A druid, who taught you the language of trees. When it came time to leave
you took with you only a <b>Gnarled Staff</b> (d8) and the promise that one day
you would return.""",
            4: """A gruff blacksmith from a sleepy river town. You were always kept at arm’s
length. Now the forge is cold, and you’ve moved on. Take a <b>Smith’s Apron</b>
(petty) and a set of oft-mended <b>Chain Mail</b> (2 Armor, <em>bulky</em>).""",
            5: """A troupe of traveling entertainers. For a time, they were like family to you.
One day you woke up and they were gone with no explanation. Take a
<b>Storybook</b>, a <b>Dagger</b> (d6), and some burning questions.""",
            6: """
The monks of a secluded forest monastery. When their rules became too
strict, you snuck away. Take a <b>Monk’s Habit</b> (warm, petty) and a <b>Spellbook</b>
of <em>Control Plants</em>.<br>
<em><b>Control Plants:</b> Nearby plants and trees obey you and gain the ability to
move at a slow pace.</em>""",
        },
    },
    {
        "name": "What keeps away bad tidings?",
        "options": {
            1: """<b>Pipeweed</b> Your good luck charm. Conversations tend to flow more easily after a smoke (6 uses).""",
            2: """<b>Stink Jar</b> Shattering this jar releases an odor so foul all nearby must
make a STR save or immediately vomit (1 use).""",
            3: """<b>Ivy Worm</b> A green worm often mistaken for a weed. Swallowed
whole, it absorbs any toxins or rot in the body before
exiting through the usual way.""",
            4: """<b>Dream Stone</b> A smooth blue stone that helps recall dreams more clearly.
Overuse can cause dream-addiction.""",
            5: """<b>Drowning Rod</b> A finger-sized wooden stick that doubles in size each time
it is fully submerged in water. It doesn’t shrink back down.""",
            6: """<b>Rabbit’s Foot</b> You were wearing it when they found you. They say it is
the foot of she who left you, and that it protects you from
witch magic.""",
        },
    },
    # starting gear
    [
        "3d6 Gold Pieces",
        "Rations (3 uses)",
        "Torch (3 uses)",
        "Salt Pouch",
        "Heirloom Amulet (<em>petty</em>, glows in the presence of magic)",
        "Sling (d6)",
        "Dagger (d6)",
    ],
    # profile
    """An odd birthmark, a strange smell: somehow, the touch of elsewhere still lingers.
You’ll never fit in, at least not where you’re at. Roll on the Omens table, but keep
the results private for now.""",
    # names
    [
        "Faunus",
        "Snowdrop",
        "Wisp",
        "Silverdew",
        "Brim",
        "Solstice",
        "Steeleye",
        "Sileas",
        "Gossamer",
        "Hazel",
    ],
]

dossier_scientist = [
    {
        "name": "Prized Lifetime Research",
        "options": {
            1: "<b>Skeletal Resonator:</b> Attract or repel a single target that has a skeleton, unless they pass a STR save. No effect on cartilage.",
            2: "<b>Portal Generator:</b> Create a portal between two flat sources that you can see. The gate closes if you pass through or break line of sight. Causes 1 fatigue.",
            3: "<b>Temporal Bomb:</b> Time slows down 60 times in a 20 foot sphere (blast). Lasts for 1 minute outside the sphere, or one second inside. One use.",
            4: "<b>Corpse Reviver #42:</b> Brings back the dead if used within 1 minute of death. One use.",
            5: "<b>Particle-Mirror Array:</b> (+1 Armor) A molecular shield generator. Once a day, make a DEX save to reflect energy weapon shots back at their source.",
            6: "<b>Creature in a Jar:</b> A baby sludge creature with one eye. Upon release, it will eat a corpse’s brain consuming its memories, effectively allowing the user to ask a corpse one question. The fresher the corpse, the better the memory. Needs a day to rest before it will come back out.",
        },
    },
    {
        "name": "Field of Expertise",
        "options": {
            1: "<b>Medical Doctor:</b> Take medical supplies that can restore 1d4 STR a day.",
            2: "<b>Molecular Chemist:</b> Take a vial of universal solvent, which dissolves anything it touches.  Enough for a brick-sized portion.  One use.",
            3: "<b>Experimental Physicist:</b> Take a can of de-friction spray. 3 charges.",
            4: "<b>Xeno Biology:</b> Take a strange alien Gecko-Fox as a pet. (3hp, 14 DEX, d6 bite, can climb sheer surfaces, must be fed something living once a week)",
            5: "<b>Toxicology:</b> Years of experimentation, immunity- building & study have provided you an immunity to all known poisons, and reduced effect on failed saves against unknown or alien toxins and poisons.",
            6: "<b>Higher Dimensions:</b> Prying open the secrets of the universe have exposed you to things you can’t explain. Roll for a random Astromancy.",
        },
    },
    {
        "name": "Why You Left Science",
        "options": {
            1: "<b>Uncouth Research:</b> You dabbled in things that are frowned upon and were run out of academia.  Start with 3 corruption.",
            2: "<b>Malaise:</b> You wanted new challenges and life in the lab just wasn’t cutting it anymore. Roll a random talent.",
            3: "<b>Blackmail:</b> A rival researcher, competitor, or criminal organization implied that if you didn’t stop your current research, they’d stop it for you.",
            4: "<b>Lab Accident:</b> There’s a corporate-sponsored bounty on your head for damage to company property.",
            5: "<b>Research De-funded:</b> Due to budgetary issues, your research has been placed on permanent hold. Sorry.",
            6: "<b>Field-Research:</b> You wanted more hands-on experience in your field.",
        },
    },
    # starting gear
    [
        "Lab coat",
        "Test tubes (6) & assorted medical tools",
        "Plasma-Knife (D6 thermal, concealable)",
    ],
    # profile
    """You’ve spent most of your life dedicated to the advancement of science. Due to new
circumstances, you’ve decided to make the change from lab work to field work.""",
]

dossier_soldier = [
    {
        "name": "Special-Issue Equipment",
        "options": {
            1: "<b>Gate Cloak:</b> Hooded cloak inscribed with nano-particle algebraic equations that allows the user to phase-shift 10’ in any direction instead of taking damage. One use a day.",
            2: "<b>Mark IV Executioner:</b> (D8 blast, silencer) A combat shotgun created by a legendary weapons manufacturer - limited run. Replaces starting weapon.",
            3: "<b>Kinetic Katana:</b> (D8, bulky, thermal) An alien weapon you recovered. Slender black blade sheathed in a metal casing. Vibrates at subsonic levels producing an intense heat and orange glow. On a roll of maximum damage, the target must make a STR save or be fatally severed in half.",
            4: "<b>RNA-Attuned Shield Generator:</b> (+1 Armor, immune to bio damage) Gene-synthesized custom shield generator. Prevents illness. Take a few cigars too.",
            5: "<b>Dual-Oculus Hooded Mask:</b> A hooded faceplate mask with two circular smart-display goggles. Allows for perfect vision in darkness and other debris via A.I. aided image sequencing.",
            6: "<b>Cockatrice Claymores:</b> 3 remote-operated explosives that explode with a gray bio- synthetic dust. (blast 40’) Make a STR save or instantly be turned to stone.",
        },
    },
    {
        "name": "Spec-Ops Team",
        "options": {
            1: "<b>Infiltration:</b> Stealth unit. Once a day you automatically succeed when prompted to make a Save to move quietly, in shadows, balancing on precarious surfaces, or similar risky actions.",
            2: "<b>Heavy Marine:</b> Heavy unit, breach specialists. Increase STR to 13 if not currently at 13.",
            3: "<b>Flash Commando:</b> Light unit, worked in small teams. Re-roll damage rolls of 1.",
            4: "<b>Shock Trooper:</b> Special weapons drop troopers. Add shock damage to your starting weapon.",
            5: "<b>Counter-Insurgency:</b> If fighting in small, confined urban spaces, your first attack roll in combat is enhanced if your weapon is suited for close-range (melee, shotgun)",
            6: "<b>Top Secret Project:</b> You were part of an experimental top- secret project. Start with a bio- aug. Roll augment and re-flavor.",
        },
    },
    {
        "name": "Squad Job",
        "options": {
            1: "<b>Cook:</b> Once a day you can stretch out a single ration to feed the whole party if you spend 10-minutes preparing it with cooking tools.",
            2: "<b>Negotiator:</b> You can attempt to negotiate mid-combat. Make a WIL save, on a success enemy reaction is improved and the fighting temporarily halts.",
            3: "<b>Quartermaster:</b> Two extra inventory slots in your backpack.",
            4: "<b>Scout:</b> You and your group can never be ambushed if you are at full HP.",
            5: "<b>Demolitions:</b> Take 2 thermal detonators. If you set up an ambush with explosives the damage is enhanced.",
            6: "<b>Point Man:</b> You have an additional 2 HP when you’re at the front of the marching order.",
        },
    },
    # starting gear
    ["Tactical fatigues", "Shotgun or Rifle", "Dog tags"],
    # profile
    """You’re ex-special ops. Having completed or parting with your duties, new
opportunities are calling your name.""",
]


dossier_star_touched = [
    {
        "name": "What Gift Did the Stars Bring?",
        "options": {
            1: "<b>The Deplorable Word:</b> Anyone you speak the word to must make a WIL save or take 1d12 WIL damage. Use once a day. WIL save vs corruption.",
            2: "<b>Carried By the Wind:</b> Fly: Can fly once a day for 2d6 seconds at your normal movement.",
            3: "<b>Puzzle Tongue:</b> Comprehend Languages: Can speak to, understand, and be understood by all spoken languages of approximately human-level intelligence.",
            4: "<b>Warding Scriptures:</b> Your body is covered in a glowing script. Once a day when an attack is made against you for maximum damage, the damage is reverted back to the attacker.  Save vs corruption as the scriptures crawl further into you.",
            5: "<b>Sunder:</b> You can attack with your mind and two free hands for D6 damage from up to 60 ft. Does not cause fatigue.",
            6: "<b>Glittering Gate:</b> Spend 10 minutes performing a ritual in a 10’ circular area. Star-blessed spaces exist as a dyad, and only two can exist at once. Stepping into one space transfers those who enter to the other space. When a new space is created, the creator mentally chooses one of the existing two locations to dissipate. All who pass through this void space must save vs corruption.",
        },
    },
    {
        "name": "Your Vision",
        "options": {
            1: "<b>A Thousand Burning Suns:</b> Your eyes smolder. Fire does not harm you.",
            2: "<b>The Forever Deep:</b> You can breathe underwater and are never cold.",
            3: "<b>Abhorrent Geometry:</b> You are immune to mind-altering effects.",
            4: "<b>Belly of a Black Hole:</b> Your eyes are pitch black. You can see in the dark.",
            5: "<b>The Secret Truth:</b> You cannot understand or speak it. You can sense any untruth you hear.",
            6: "<b>Perfect Symmetry:</b> It was almost too beautiful to behold.  Social encounters are much easier for you. Reaction rolls in social situations are always one category higher than your result.",
        },
    },
    {
        "name": "What Was Taken?",
        "options": {
            1: "<b>Your Voice:</b> You can speak, but at a slow, strained crackle that sets others on edge.",
            2: "<b>Your Memories:</b> The past before you touched the infinite is insignificant, burned away to ash. You remember nothing from before.",
            3: "<b>Your Mind:</b> Whenever you gain fatigue, roll a d6. On a 1, you spend the next round clutching your head and babbling.  Addiction-inducing stims will calm you.",
            4: "<b>Your Superego:</b> Societal morality must be relearned, or perhaps simply left behind entirely.",
            5: "<b>Your Future:</b> Once a week you must make a save vs. corruption.  Slowly your future is rotting away.",
            6: "<b>Your Humanity:</b> Roll on the mutations table (pg. 89)",
        },
    },
    # starting gear
    ["Nothing can be truly possessed. You start with nothing but your clothing."],
    # profile
    """The living void and its myriad aspects reach out to you. You now belong to some
    greater purpose, or vaster intelligence, and have been gifted with a sliver of that
    power to wield as the envoy of forces you could no possibly comprehend.""",
]


dossier_bounty_hunter = [
    {
        "name": "Specialty Tool",
        "options": {
            1: "<b>Visage of Dread:</b> (+1 Armor, immune to mind-altering effects): Skull helmet (or something intimidating). At the start of combat, enemies save vs WIL or cower in fear for 1 round.",
            2: "<b>Heat-Seeking Sniper Rifle:</b> (D10) One mile range. 9-10 damage on the first shot of combat or from a hidden position is an instant kill.",
            3: "<b>Grave-Foam Gauntlet:</b> Sprays a liquid cloud of gray dust, forming a 12 inch thick casing around the target for 1d12 hours. Nothing inside can break out. The casing keeps its contents alive in a safe stasis until released. 1 cartridge of fuel (3 uses). Buy more fuel from Bounty Hunters’ Union.",
            4: "<b>Shock Dart:</b> (D6, spec ammo) Wrist mounted rocket dart. DEX save vs paralysis for 1d6 minutes.",
            5: "<b>Wire Shot:</b> (grappling) Wrist-mounted. Shoots a magnetic smart-wire that wraps around and ensnares targets. Dex save or completely grappled. No save if surprised.",
            6: "<b>Trick-Axe:</b> (D8, bulky, sweep): Can retract down to 3 feet in length for (D6).",
        },
    },
    {
        "name": "How Did You Hunt?",
        "options": {
            1: "<b>Like a True Hunter:</b> You hunted for trophies and glory, and by any means necessary. Take a notorious reputation and a war dog companion (d6 bite, 2 HP, 12 STR, 60’ speed)",
            2: "<b>From the Shadows:</b> If you get the jump on someone from hiding, your attacks are enhanced.",
            3: "<b>With a Personal Code:</b> Other hunters and those in the community respect you. You can request an audience with typically inaccessible underworld leaders.",
            4: "<b>Loaded With Tech:</b> Take 1d4 smart grenades (d6 blast, thermal, grappling) an auto-saw, and binocs.",
            5: "<b>By Any Means Necessary:</b> It was sometimes dirty, or unfair, but you got the job done. Any damage from traps, snares, or other preparations you make are enhanced.",
            6: "<b>Just for the Money:</b> It’s only a job, after all. Negotiate for double payouts on any bounty job. The NPC offering the job must pass a WIL save to resist, otherwise they’re persuaded to pay extra.",
        },
    },
    {
        "name": "A Past Complication",
        "options": {
            1: "<b>Revenge:</b> An old target escaped from prison and is after you. The hunter becomes the hunted…",
            2: "<b>Wanted:</b> You crossed the wrong syndicate. You’re now a wanted (alive) individual in 16 systems.",
            3: "<b>Radio Silence:</b> Your old primary fixer and contact went silent. You worry they may be compromised, or worse.",
            4: "<b>Old Dog:</b> Injuries, a hard life, and general wear and tear has taken its toll, and you’re not as spry as you once were. Sometimes that comes back to bite you.",
            5: "<b>Imposter:</b> After you left the scene, someone else recently appeared claiming to be you, and they’re ruining your hard-earned rep. Undealt with, it could have some unpleasant consequences.",
            6: "<b>One Last Job</b> An old client really needs your help on one last job.  Word is the pay is high...high enough for a lot of other hunters to also be on the hunt.",
        },
    },
    # starting gear
    [
        "Rifle or two blasters.",
        "Old Armor (Armor 1, Bulky)",
        "Manacles",
        "Bounty Hunting License & Union Membership.",
    ],
    # profile
    """It’s a slimy, treacherous world out there, and you had to be just as nasty to keep the
wolves from the door. You made your living as a licensed bounty hunter.""",
]


template_tables = [
    {
        "name": "What Keeps You Safe on the Streets?",
        "options": {},
    },
    {
        "name": "Type of Scum",
        "options": {},
    },
    # starting gear
    [],
    # profile
    """""",
    # names
    [],
]
BACKGROUND_TABLES = {
    "Aurifex": aurifex_tables,
    "Barber-Surgeon": barber_surgeon_tables,
    "Beast Handler": beast_handler_tables,
    "Bone Keeper": bonekeeper_tables,
    "Cutpurse": cutpurse_tables,
    "Field Warden": field_warden_tables,
    "Fletchwind": fletchwind_tables,
    "Foundling": foundling_tables,
    "SCIENTIST": dossier_scientist,
    "SOLDIER": dossier_soldier,
    "STAR-TOUCHED": dossier_star_touched,
    "BOUNTY HUNTER": dossier_bounty_hunter,
}
