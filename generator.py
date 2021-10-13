from random import randint, uniform, shuffle, choice

from pymongo import MongoClient

try:
    conn = MongoClient(
        "mongodb+srv://Ines-Diaz:CF2QDipwxkQNxwQr@edaid-soil.hflhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")


codes_list = ["G0" + str(i) for i in range(201, 501)]
asd_list = ["0100" + str(i) for i in range(301, 601)]
shuffle(asd_list)

descriptions = [
    "Sandy soil",
    "Limestone soil",
    "Silty soil",
    "Black earth soil",
    "Argillaceous soil",
    "Stony soil",
    "Peat soil",
    "Saline soil",
]

ITEMS_COUNT = 300

for i in range(ITEMS_COUNT):
    code = codes_list[i]
    a1 = randint(0, 10)
    a2 = randint(0, 10)
    a3 = randint(0, 30)
    a4 = randint(0, 50)
    a5 = randint(0, 50)
    l1 = randint(10, 40)
    l2 = randint(10, 40)
    asd = asd_list[i]

    item = {
        "CODE": code,
        "PHOTOGRAPHS": "See JPG: " + code + "-SSC y " + code + "-U",
        "DESCRIPTION": choice(descriptions),
        "COORDINATES X": randint(310000, 340000),
        "COORDINATES Y": randint(4050000, 4080000),
        "ALTITUDE": randint(300, 1000),
        "INCLINE": randint(0, 60),
        "GRAVES": randint(0, 300),
        "VERY THICK SAND": a1,
        "THICK SAND": a2,
        "MEDIUM SAND": a3,
        "FINE SAND": a4,
        "VERY FINE SAND": a5,
        "TOTAL SAND": a1 + a2 + a3 + a4 + a5,
        "THICK LIMES": l1,
        "FINE LIMES": l2,
        "TOTAL LIMES": l1 + l2,
        "CLAY": randint(0, 10),
        "K FACTOR": round(uniform(0.0, 1.0), 2),
        "APPARENT DENSITY": round(uniform(0.0, 2.0), 2),
        "AGGREGATE STABILITY": randint(30, 60),
        "PERMEABILITY": randint(0, 150),
        "FIELD CAPACITY": randint(10, 60),
        "PERMANENT WILTING POINT": randint(0, 20),
        "HYDROPHOBICITY": randint(0, 1),
        "ORGANIC CARBON": str(round(uniform(0.0, 10.0), 2)),
        "C FACTOR": round(uniform(0.0, 1.0), 2),
        "ELECTRIC CONDUCTIVITY": str(round(uniform(0.0, 0.5), 2)),
        "SPECTRAL RESPONSE ": " See document: " + asd + ".asd",
    }

    conn.SoilDB.Data.insert_one(item)
    print(f"Inserting item {i}/{ITEMS_COUNT}", end="\r")
