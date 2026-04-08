import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

database_file = "fitnessstudio.db"

@anvil.server.callable
def query_kurs_data(self):
  query = "SELECT Bezeichnung, Wochentag, Uhrzeit, Trainer.Nachname || ' ' || Trainer.Vorname Trainer FROM Kurs INNER JOIN Trainer ON Trainer.TrainerID = Kurs.TrainerID;"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_kurs_besucher(self, kurs_id):
  query = f"SELECT COUNT(Einschreiben.MitgliedID) FROM Einschreiben INNER JOIN Mitglied ON Mitglied.MitgliedID = Einschreiben.MitgliedID INNER JOIN Kurs ON Kurs.KursID = Einschreiben.KursID WHERE Einschreiben.KursID = {kurs_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def query_kurs_besucher_max(self, kurs_id):
  query = f"SELECT MaxTeilnehmer FROM Kurs WHERE KursID={kurs_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result
  
@anvil.server.callable
def query_kurs_ids(self):
  query = "SELECT KursID FROM Kurs;"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result