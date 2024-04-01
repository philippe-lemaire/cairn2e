from gamelogic.roll import roll
from gamelogic.backgrounds import backgrounds, BACKGROUND_TABLES
from gamelogic.finishing_touches import (
    physique,
    skin,
    hair,
    clothing_style,
    face,
    speech,
    virtue,
    vice,
    male_names,
    female_names,
    ambiguous_names,
    last_names,
)
from gamelogic.bounds import bounds
from random import choice


class Character:
    def __init__(self, background=None):
        self.first_name = choice(choice((male_names, female_names, ambiguous_names)))
        self.last_name = choice(last_names)
        self.STR = roll("3d6")
        self.DEX = roll("3d6")
        self.WIL = roll("3d6")
        self.HP = roll("d6")
        self.background = background
        if not self.background:
            self.background = choice(backgrounds)

        (
            self.dossier_part1,
            self.dossier_part2,
            #self.dossier_part3,
            self.gear,
            self.profile,
        ) = BACKGROUND_TABLES.get(self.background)
        self.dossier_name = self.dossier_part1.get("name")
        self.dossier_option = self.dossier_part1.get("options").get(self.HP)
        self.dossier_subpart_name = self.dossier_part2.get("name")
        self.dossier_subpart_option = choice(
            list(self.dossier_part2.get("options").values())
        )


        self.common_gear = [
        ]

        self.bound = choice(bounds)

        self.finishing_touches = {
            "physique": choice(physique),
            "skin": choice(skin),
            "hair": choice(hair),
            "clothing": choice(clothing_style),
            "face": choice(face),
            "speech": choice(speech),
            "virtue": choice(virtue),
            "vice": choice(vice),
        }
