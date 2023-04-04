from enum import Enum
from pathlib import Path

class StoryType(Enum):
    Character = 1
    CharacterHScene = 2
    Main = 3
    Event = 4

class EventType(Enum):
    Tutorial = 0
    Raid = 1
    Treasure = 2
    Other = 3

class Rarity(Enum):
    A = 2
    S = 3
    SS = 4

class Character(Enum):
    Paddington = 0
    Awilda = 1
    Tayshet = 2
    Kuala_Lum = 3
    Jeran = 4
    Volklingen = 5
    Ohana = 6
    Futamata = 7
    Penang_Hill = 8
    Finchley = 9
    Queensway = 10
    Notting_Hill = 11
    Ooenomiya = 12
    Putra = 13
    Karakawa = 14
    Alexandra = 15
    Phnom_Penh = 16
    Fussen = 17
    Novella = 18
    Karlsruhe = 19
    Yakutsk = 20
    Shimoamazu = 21
    Amanohashidate = 22
    Orleans = 23
    Yoshino = 24
    Volgo = 25
    Leipzig = 26
    Fayette = 27
    Murmansk = 28
    Amiens = 29
    Anzio = 30
    Dover = 31
    Bourse = 32
    Rouen = 33
    Lancaster = 34
    Vivienne = 35
    Salem = 36
    Roswell = 37
    Acapulco = 38
    Las_Vegas = 39
    Abashiri = 40
    Passy = 41
    Tianjin = 42
    Detroit = 43
    Chitose = 44
    Pancras = 45
    Naypyidaw = 46
    Puerto_Rico = 47
    Shibuya = 48
    Beijing = 49
    Pennsylvania = 50
    Termini = 51
    Victoria = 52
    Tombstone = 53
    Nara = 54
    Rennes = 55
    Kuang = 56
    Blanche = 57
    Oculus = 58
    Freiburg = 59
    Kings_Cross = 60
    Batu = 61
    Carthage = 62
    Tokachi = 63
    Verona = 64
    Part_Dieu = 65
    Honolulu = 66
    Columbia = 67
    Shanghai = 68
    Frankfurt = 69
    Messina = 70
    Brittany = 71
    Udon_Thani = 72
    Tendou = 73
    Stia = 74
    Izumo_no_Hakuto = 75
    Khabarovsk = 76
    Zouerat = 77
    Pleven = 78
    Waterloo = 79
    Blackfriars = 80
    Akihabara = 81
    Munich = 82
    Ayala = 83
    Port_Royal = 84
    Austerlitz = 85
    Costa_Rica = 86
    Kinugawa = 87
    Nikkou = 88
    Khajuraho = 89
    Petropav = 90
    Grenoble = 91
    Wernigerode = 92
    Fontaine = 93
    Bestyakh = 94
    Karamachi = 95
    Shiyan = 96
    Woking = 97
    Sentosa = 98
    San_Diego = 99
    Monte_Carlo = 100
    Susukino = 101
    Naples = 102
    Yokosuka = 103
    Euston = 104
    Urga = 105
    Asahikawa = 106
    Pittsburgh = 107
    Annecy = 108
    Menlo_Park = 109
    Versailles = 110
    Miyako = 111
    Adelaide = 112
    Goslar = 113
    Margit_Ebenbach = 114
    Momoyo_Kawakami = 115
    Tsubame_Matsunaga = 116
    Benkei_Musashibou = 117
    Aki_Mogami = 118
    Yukie_Mayuzumi = 119
    Unknown120 = 120
    Unknown121 = 121
    Unknown122 = 122
    Unknown123 = 123
    Unknown124 = 124
    Yukikaze_Mizuki = 125
    Rinko_Akiyama = 126
    Felicia = 127
    Kirara_Onisaki = 128
    Hebiko_Aishu = 129
    Asagi_Igawa = 130
    Khao_Yai = 131
    Unknown132 = 132
    Addis_Ababa = 133
    Tsurugaoka = 134
    Baraboo = 135
    Oaxaca = 136
    Etretat = 137
    Berrigan = 138
    Kumamoto = 139
    Catania = 140
    Isobe = 141
    Mary = 142
    Yuuzen = 143
    Dr_Gloria = 144
    Palermo = 145
    Quedlinburg = 146
    Oshiage = 147
    Hachiroku = 148
    Olivi = 149
    Reina = 150
    Niiroku = 151
    Hiyoko = 152
    Celia = 153
    Mio_Kisaki = 154
    Akane_Ryuuzouji = 155
    Risona_Okura = 156
    Luna_Sakurakouji = 157
    Minato_Yanagase = 158
    Maki = 159
    Vincennes = 160


class CharacterStory:
    def __init__(self, filename:str=""):
        self.story_type = StoryType(int(filename[0:1]))
        assert self.story_type == StoryType.Character or self.story_type == StoryType.CharacterHScene
        self.character_id = Character(int(filename[1:-5]))
        self.rarity = Rarity(int(filename[-5:-4]))
        self.rarity_id = filename[-4:-2]
        self.scenario_id = filename[-2:]

    def __str__(self) -> str:
        return f"{self.story_type.value}{self.character_id.value}{self.rarity.value}{self.rarity_id}{self.scenario_id}"

    def csv_filename(self) -> Path:
        return Path(f"Character").joinpath(f"{self.character_id.value:>04}.csv")

    def translated_filename(self) -> Path:
        return Path("Character").joinpath(f"{self}.json")

class MainStory:
    def __init__(self, filename:str=""):
        self.story_type = StoryType(int(filename[0:1]))
        assert self.story_type == StoryType.Main
        self.chapter_id = filename[1:4]
        self.subchapter_id = filename[4:]

    def __str__(self) -> str:
        return f"{self.story_type.value}{self.chapter_id}{self.subchapter_id}"

    def csv_filename(self) -> Path:
        return Path(f"Main").joinpath(f"{self.chapter_id}.csv")
    
    def translated_filename(self) -> Path:
        return Path("Main").joinpath(f"{self}.json")

class EventStory:
    def __init__(self, filename:str=""):
        self.story_type = StoryType(int(filename[0:1]))
        assert self.story_type == StoryType.Event
        self.event_type1 = EventType(int(filename[1:2]))
        self.event_id = filename[2:-3]
        self.event_type2 = EventType(int(filename[-3:-2]))
        self.subchapter_id = filename[-2:]

    def __str__(self) -> str:
        return f"{self.story_type.value}{self.event_type1.value}{self.event_id}{self.event_type2.value}{self.subchapter_id}"

    def csv_filename(self) -> Path:
        return Path("Event").joinpath(f"{self.event_type2.name}_{self.event_id}.csv")

    def translated_filename(self) -> Path:
        return Path("Event").joinpath(f"{self}.json")