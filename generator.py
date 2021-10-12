from random import randint, uniform, shuffle

from pymongo import MongoClient

try:
    conn = MongoClient(
        "mongodb+srv://Ines-Diaz:CF2QDipwxkQNxwQr@edaid-soil.hflhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

"""
Conexión con base y colección
"""

codes_list = ["G0" + str(i) for i in range(201, 501)]
asd_list = ["0100" + str(i) for i in range(301, 601)]
shuffle(asd_list)

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
        "CÓDIGO": code,
        "FOTOGRAFÍAS": "See JPG: " + code + "-SSC y " + code + "-U",
        "DESCRIPCIÓN": "Anuales + RF 20-70 part emb???",
        "COORDENADAS X": randint(310000, 340000),
        "COORDENADAS Y": randint(4050000, 4080000),
        "ALTITUD": randint(300, 1000),
        "PENDIENTE": randint(0, 60),
        "GRAVAS": randint(0, 300),
        "ARENAS MUY GRUESAS": a1,
        "ARENAS GRUESAS": a2,
        "ARENAS MEDIAS": a3,
        "ARENAS FINAS": a4,
        "ARENAS MUY FINAS": a5,
        "ARENAS TOTALES": a1 + a2 + a3 + a4 + a5,
        "LIMOS GRUESOS": l1,
        "LIMOS FINOS": l2,
        "LIMOS TOTALES": l1 + l2,
        "ARCILLAS": randint(0, 10),
        "FACTOR K": round(uniform(0.0, 1.0), 2),
        "DENSIDAD APARENTE": round(uniform(0.0, 2.0), 2),
        "ESTABILIDAD DE AGREGADOS": randint(30, 60),
        "PERMEABILIDAD": randint(0, 150),
        "CAPACIDAD DE CAMPO": randint(10, 60),
        "PUNTO DE MARCHITEZ PERMANENTE": randint(0, 20),
        "HIDROFOBICIDAD": randint(0, 1),
        "CARBONO ORGÁNICO": str(round(uniform(0.0, 10.0), 2)),
        "FACTOR C": round(uniform(0.0, 1.0), 2),
        "CONDUCTIVIDAD ELÉCTRICA": str(round(uniform(0.0, 0.5), 2)),
        "RESPUESTA ESPECTRAL": "Ver documento: " + asd + ".asd",
    }

    conn.SoilDB.Data.insert_one(item)
    print(f"Inserting item {i}/{ITEMS_COUNT}", end="\r")

    """
    item = {
        "CODE": code,
        "PHOTOGRAPHS": "See JPG: " + code + "-SSC y " + code + "-U",
        "DESCRIPTION": "Anuales + RF 20-70 part emb???",
        "COORDINATES X": randint(310000, 340000),
        "COORDINATES Y": randint(4050000, 4080000),
        "ALTITUDE": randint(300, 1000),
        "SLOPE": randint(0, 60),
        "GRAVES": randint(0, 300),
        "VERY THICK SANDS": a1,
        "THICK SANDS": a2,
        "MEDIUM SANDS": a3,
        "FINE SANDS": a4,
        "VERY FINE SANDS": a5,
        "TOTAL SANDS": a1 + a2 + a3 + a4 + a5,
        "THICK LIMES": l1,
        "FINE LIMES": l2,
        "TOTAL LIMES": l1 + l2,
        "CLAYS": randint(0, 10),
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
        "SPECTRAL RESPONSE ":" See document: " + asd + ".asd"
    }

    collection.insert_one(item)
    """
