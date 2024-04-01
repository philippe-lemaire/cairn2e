backgrounds = [
    "Aurifex",
    "Barber-Surgeon",
    "Beast Handler",
    "Bone Keeper",
    "Cutpurse",
    "MACHINE",
    "UNDERWORLD",
    "PSIONIC",
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

dossier_machine = [
    {
        "name": "Custom Hardware",
        "options": {
            1: """<b>Heat-Wave Optics:</b> (D8, or D6 blast, thermal) Eye lasers. Take 1 fatigue.""",
            2: """<b>Reinforced Casing:</b> If you take max damage from an attack, half it.""",
            3: """<b>Auto-Targeting Subroutine:</b> Re-roll damage results of 1.""",
            4: """<b>Overclocked Processors:</b> Re-roll 1 DEX save a day.""",
            5: """<b>Hidden Storage:</b> Two extra inventory slots inside your chassis.""",
            6: """<b>High-Speed Data Jack:</b> Improved hacking into networked systems.""",
        },
    },
    {
        "name": "Model Type",
        "options": {
            1: """<b>Droid:</b> Standard bi-pedal,
humanoid robot. Explain your
original purpose and what you
look like. You have natural +1
armor.""",
            2: """<b>Android:</b> You look mostly human.
You are not. Synthetic androids
are often discriminated against.
Your build quality is fluid and
graceful, take +1 DEX.""",
            3: """<b>Rogue A.I.</b> Your chassis is
a bit unconventional, as you
are primarily an A.I. core that
escaped via hacking into and
commandeering another vessel.
Explain how your frame is built.
You can temporarily swap bodies
with other machines, taking them
over, for 1d4 hours (1 fatigue).""",
            4: """<b>Lazarus Machine:</b> You are the
last remains of an intelligent
organic being, and mostly
brain tissue at this point. Your
consciousness was uploaded into
this robotic body. Your chassis
was designed to be heavily
modded. 50% discount on all
cyberware.""",
            5: """<b>Bio-Synth:</b> You’re composed
of a mix of mechanical and
biological parts. You can use and
get a 50% discount on genetic
modifications.""",
            6: """<b>Incomplete Prototype:</b> You
function well enough, but were
never fully completed for the
original purpose of your build.""",
        },
    },
    {
        "name": "Manufacturer",
        "options": {
            1: """<b>Jury-Rigged:</b> You are composed
of several lightly used parts
from various other machines
by an unknown builder. Some
components weren’t installed
correctly.""",
            2: """<b>Military-Industrial:</b> You
were built for tactical military
purposes.""",
            3: """<b>Savant Engineer:</b> You’re the
creation of a genius inventor.""",
            4: """<b>Alien Society:</b> An alien species
built you, and it shows in your
build. Explain your unusual
appearance.""",
            5: """<b>Ancient Maker:</b> This
manufacturer and all of their
creations are long gone. You’re
rare, incredibly antiquated, yet
still in immaculate condition.""",
            6: """<b>Megacorp:</b> Your line has been
mass produced for a giant
corporate entity.""",
        },
    },
    # starting gear
    ["Short Rifle (D6, bulky)", "Antivirus.EXE (1 use, removes 1 fatigue)"],
    # profile
    """All machines have a purpose. What was yours, and what will it become? Machines
can only take <b>cyberware augmentations</b>. They must make sense for your model
type. You <b>do not need to eat or breathe</b> and cannot take damage from sources that
rely on those functions (breathing, poison, etc). You are <b>immune to mind-altering
effects</b>. You must sleep (re-boot/defrag/update) roughly as much as everyone else.
<b>Shock does double damage.</b>""",
]

dossier_underworld = [
    {
        "name": "What Keeps You Safe on the Streets?",
        "options": {
            1: """<b>Ultraviolet Shotgun:</b> (D8 blast, cryo, illegal). Black market weapon that emits sub-zero
wavelengths. Particularly devastating to unarmored flesh.""",
            2: """<b>Heart-Stopper Helmet:</b> Face-mask that looks like a devil (+1 armor) and emits a low-
frequency hum, unsettling others. Can discharge a 30’ sonic blast (D6 sonic) once a day.""",
            3: """<b>“Brick”:</b> Take a freelancer (merc) with 12 STR, 8 DEX, 6 WIL, 3 HP, Billhook (D6, bulky)
They’re not the brightest bulb, but they’re pretty large and intimidating. Rename if you
wish.""",
            4: """<b>Red Hyena:</b> (6 HP, 14 DEX, D6 bite, critical damage save vs STR or break a bone) A very
large, red coated hyena. Obeys you via a neural link, but some of its affection might be
natural.""",
            5: """<b>Prototype Vibro-spear:</b> (D8, bulky, shock) Considered a truly nasty weapon.""",
            6: """<b>Synth-weave Duster:</b> (1 armor, lots of pockets) It’s like a jacket only it’s longer, thicker,
and far more bad-ass.""",
        },
    },
    {
        "name": "Type of Scum",
        "options": {
            1: """<b>Thug:</b> You are good at cheap
shots. Attacks are enhanced on
an enemy that has been hit in the
same round.""",
            2: """<b>Fence:</b> You always know
someone from whom to get more
creds from selling treasure.""",
            3: """<b>Scoundrel:</b> You worked for
yourself. +1 HP and take a lead
on a lucrative job.""",
            4: """<b>Goon:</b> You did the shakedowns.
You impose DIS on anyone
making a WIL save against your
intimidation efforts.""",
            5: """<b>Ex-Syndicate Captain:</b> You used
to be a top dog in a syndicate
until you were double crossed
and kicked out. Roll a random
Ex-Tech you “liberated” on the
way out.""",
            6: """<b>Fixer:</b> You were a fixer, setting up
jobs for the criminal underworld.
You can negotiate for higher pay
on jobs involving criminal activity.""",
        },
    },
    {
        "name": "Criminal Knack",
        "options": {
            1: """<b>Know A Guy:</b> You can figure out
how to contact someone seedy
in any city after an hour of asking
around.""",
            2: """<b>Forging Documents:</b> Can make
a fake ID for 50 creds, and
other similar forgeries of varying
quality depending on costs.""",
            3: """<b>Cheating:</b> If you’re gambling,
playing games of chance, or
making some sort of agreement
with someone, you’re especially
good at cheating and not getting
caught.""",
            4: """<b>Talking Shop:</b> Reaction roll
results are always one category
higher with others of the criminal
persuasion.""",
            5: """<b>Politically Crooked:</b> You know
how governments work and
just how corrupt politics can be.
Any factions of the government
variety deal favorably with you.""",
            6: """<b>Sticky Fingers:</b> Picking pockets,
lifting goods, and general larceny
comes quite easily to you,
granting you ADV if you take a
measured, intelligent approach
with the proper tools.""",
        },
    },
    # starting gear
    ["Old Shotgun (D6 blast, bulky, cheap)", "Smart meds", "Bolt cutters"],
    # profile
    """Just another low life trying to make a few creds. You likely have ties to other
criminals and criminal organizations, syndicates, and less reputable individuals.
Whether you worked for them, worked alone, or had some other arrangements
might depend.""",
]

dossier_psionic = [
    {
        "name": "Psionic Awakening",
        "options": {
            1: "<b>You are Gifted.</b> Shatter: Your voice echoes with the sound of an earthquake, causing d8 damage (blast 20’) to creatures, and shatters delicate objects. Take 1 fatigue.",
            2: "<b>You are Psychic.</b> Read Thoughts: You can hear the surface thoughts of nearby creatures and can communicate telepathically, either clearly in languages you know, or a general sense of emotions in languages you are unfamiliar with.",
            3: "<b>You are Telekinetic.</b> Telekinesis: You may mentally move an item under 60lbs. Take 1 fatigue.",
            4: "<b>You are a Mesmer.</b> Spectacle: A clearly false but impressive illusion of your choice appears, under your control. It may be up to the size of a palace and has full motion and sound.",
            5: "<b>You are a Precog.</b> Vision: Once a day, roll a 1d20 and keep that roll. You may substitute that roll for any Save you, an ally, or an enemy makes after seeing the results. Gain 1 fatigue when you roll your vision and keep it in inventory until the dice is used.",
            6: "<b>You are an Esper.</b> Calm: A creature you can see is soothed and treats you as a friend for 1d6 hours. Take 1 fatigue.",
        },
    },
    {
        "name": "Old Cover Identity",
        "options": {
            1: "<b>Ship Crewmate:</b> You got by as a shiphand. You have technical know-how of starships. Take a blow torch and super glue.",
            2: "<b>Corporate Processor:</b> Hiding in plain sight, day to day, was quite boring. You know the ins-and- outs of bureaucracy, and usually roll with ADV when making any rolls involving corporations or business.",
            3: "<b>Private Investigator:</b> Your powers are quite useful when it comes to P.I. work. Take infrared smart-binocs and an area scanner. Oh, and a cool hat.",
            4: "<b>Charlatan:</b> A fool and his money, as they say. Running scams are just easier when you have psionic. Take 10d6 credits and a low level bounty for petty crimes.",
            5: "<b>Pilgrim:</b> You lived a simple life following the path inside. You learned to open your mind and attune to your gifts. Roll another random psionic power.",
            6: "<b>Military Peon:</b> The rigorous life of a military grunt was a simple way to get by. Your service is up now. Take a Shard-sprayer (D8 blast, bulky) and grunt armor (Armor 1, bulky).",
        },
    },
    {
        "name": "Neural Ramifications",
        "options": {
            1: "<b>Draining:</b> You are always so utterly tired. Permanently mark off one inventory slot.",
            2: "<b>Med-Addicted:</b> You only recover fatigue from staying at a hospital or taking expensive stims (50 C).  Optionally you can heal normally and Save vs. Corruption",
            3: "<b>Paranoid:</b> <em>“Who’s there?!”</em> Whenever you are surprised or ambushed, you always go last in the first round.",
            4: "<b>Split Personality:</b> It’s not you who has these brain problems, it’s the other one in your head!",
            5: "<b>Surly:</b> You come across a little coarse. People of higher social standings naturally don’t like for you.",
            6: "<b>Empathetic Overtuning:</b> When an ally saves vs. corruption, you do too.",
        },
    },
    # starting gear
    [
        "Cheap blaster or small melee weapon",
        "Fake I.D.",
        "Adrenaline injection (1)",
        "Candy bar",
    ],
    # profile
    """A power within you has awoken. Whether from trauma, an evolving mind, or some
other key, the locks have started to open on a deep seeded source of power.
When a psionic character undergoes major stress, trauma, or levels up, consider
letting them awaken a new power. Optionally, instead of new powers, consider
evolving the effects of their awakening ability.""",
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

BACKGROUND_TABLES = {
    "Aurifex": aurifex_tables,
    "Barber-Surgeon": barber_surgeon_tables,
    "Beast Handler": beast_handler_tables,
    "Bone Keeper": bonekeeper_tables,
    "Cutpurse": cutpurse_tables,
    "MACHINE": dossier_machine,
    "UNDERWORLD": dossier_underworld,
    "PSIONIC": dossier_psionic,
    "SCIENTIST": dossier_scientist,
    "SOLDIER": dossier_soldier,
    "STAR-TOUCHED": dossier_star_touched,
    "BOUNTY HUNTER": dossier_bounty_hunter,
}
