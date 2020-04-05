import sqlite3

connection = sqlite3.connect("genes.db")

connection.execute('''CREATE TABLE IF NOT EXISTS metadata (
                                                        animal_id INTEGER PRIMARY KEY,
                                                        dna_chip_id TEXT UNIQUE,
                                                        breed TEXT,
                                                        sex TEXT
                                                        )''')

connection.execute("""CREATE TABLE IF NOT EXISTS genstudio (psnp_id INTEGER PRIMARY KEY, 
                                            SNP_Name TEXT,
                                            SNP_Index INTEGER,
                                            SNP_Aux INTEGER,
                                            dna_chip_id TEXT,
                                            SNP TEXT,
                                            Allele1_Top TEXT,
                                            Allele2_Top TEXT,
                                            Allele1_Forward TEXT,
                                            Allele2_Forward TEXT,
                                            Allele1_AB TEXT,
                                            Allele2_AB TEXT,
                                            Chr TEXT,
                                            Position INTEGER,
                                            GC_Score REAL,
                                            GT_Score REAL,
                                            Theta REAL,
                                            R REAL,
                                            B_Allele_Freq REAL,
                                            Log_R_Rationame REAL
                                            REFERENCES
                                            metadata (dna_chip_id)
                                            ON DELETE CASCADE
                                            ON UPDATE CASCADE)""")




query = """INSERT INTO genstudio (psnp_id, SNP_Name, SNP_Index, SNP_Aux, dna_chip_id, SNP, Allele1_Top, Allele2_Top, 
        Allele1_Forward, Allele2_Forward, Allele1_AB, Allele2_AB, Chr, Position, GC_Score, GT_Score, Theta, R, B_Allele_Freq, 
        Log_R_Rationame) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

with open("genstudio.csv", 'r') as genstudio:
    genstudio.readline()
    for i in genstudio.readlines():
        line = i.split(",")
        print(line)
        connection.execute(query, line)

query = "INSERT INTO metadata (animal_id, dna_chip_id, breed, sex) VALUES (?, ?, ?, ?) "

with open("metadata.csv", 'r') as metadata:
    metadata.readline()
    for i in metadata.readlines():
        line = i.split(",")
        connection.execute(query, line)


connection.execute('''DELETE FROM metadata WHERE metadata.animal_id = 6''')


connection.commit()

