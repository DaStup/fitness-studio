from ._anvil_designer import KurseTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Kurse(KurseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    kurs_ids = anvil.server.call('query_kurs_ids', 0)

    max_besucher = []
    for id in kurs_ids:
      max_besucher.append(f"{anvil.server.call('query_kurs_besucher', 0, id[0])}/{anvil.server.call('query_kurs_besucher_max', 0, id[0])}")
 

    kurs_data = anvil.server.call('query_kurs_data', 0)

    self.repeating_panel_kurse.items = kurs_data

    
    
