import sqlite3

conn = sqlite3.connect("fitnessstudio.db")
cursor = conn.cursor()

# Tabellen löschen (optional für sauberen Neustart)
cursor.execute("DROP TABLE IF EXISTS Einschreiben")
cursor.execute("DROP TABLE IF EXISTS Kurs")
cursor.execute("DROP TABLE IF EXISTS Mitglied")
cursor.execute("DROP TABLE IF EXISTS Trainer")

# Trainer
cursor.execute("""
CREATE TABLE Trainer (
    TrainerID INTEGER PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    Spezialgebiet TEXT
)
""")

# Kurs (jetzt vollständig!)
cursor.execute("""
CREATE TABLE Kurs (
    KursID INTEGER PRIMARY KEY,
    Bezeichnung TEXT,
    Wochentag TEXT,
    Uhrzeit REAL,
    MaxTeilnehmer INTEGER,
    TrainerID INTEGER,
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
)
""")

# Mitglied
cursor.execute("""
CREATE TABLE Mitglied (
    MitgliedID INTEGER PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    EMail TEXT
)
""")

# Einschreiben
cursor.execute("""
CREATE TABLE Einschreiben (
    EinschreibenID INTEGER PRIMARY KEY,
    Einschreibedatum DATE,
    MitgliedID INTEGER,
    KursID INTEGER,
    FOREIGN KEY (MitgliedID) REFERENCES Mitglied(MitgliedID),
    FOREIGN KEY (KursID) REFERENCES Kurs(KursID)
)
""")

# --- Testdaten ---

# ≥ 3 Trainer
trainer = [
    (1, "Max", "Müller", "Yoga"),
    (2, "Anna", "Schmidt", "Fitness"),
    (3, "Tom", "Becker", "Cardio")
]
cursor.executemany("INSERT INTO Trainer VALUES (?, ?, ?, ?)", trainer)

# ≥ 5 Kurse (jetzt vollständig)
kurse = [
    (1, "Yoga Anfänger", "Montag", 9.0, 15, 1),
    (2, "Pilates", "Dienstag", 18.0, 12, 2),
    (3, "Zumba", "Mittwoch", 17.5, 20, 3),
    (4, "Spinning", "Donnerstag", 19.0, 10, 1),
    (5, "Crossfit", "Freitag", 16.0, 8, 2)
]
cursor.executemany("INSERT INTO Kurs VALUES (?, ?, ?, ?, ?, ?)", kurse)

# ≥ 6 Mitglieder
mitglieder = [
    (1, "Lisa", "Klein", "lisa@example.com"),
    (2, "Paul", "Meier", "paul@example.com"),
    (3, "Sophie", "Fischer", "sophie@example.com"),
    (4, "Leon", "Weber", "leon@example.com"),
    (5, "Emma", "Wagner", "emma@example.com"),
    (6, "Noah", "Schulz", "noah@example.com")
]
cursor.executemany("INSERT INTO Mitglied VALUES (?, ?, ?, ?)", mitglieder)

# ≥ 8 Einschreibungen
einschreibungen = [
    (1, "2024-01-01", 1, 1),
    (2, "2024-01-02", 2, 2),
    (3, "2024-01-03", 3, 3),
    (4, "2024-01-04", 4, 4),
    (5, "2024-01-05", 5, 5),
    (6, "2024-01-06", 6, 1),
    (7, "2024-01-07", 1, 2),
    (8, "2024-01-08", 2, 3)
]
cursor.executemany("INSERT INTO Einschreiben VALUES (?, ?, ?, ?)", einschreibungen)

conn.commit()
conn.close()

print("Datenbank korrekt erstellt und vollständig befüllt!")