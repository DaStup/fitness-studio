from ._anvil_designer import AnmeldenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Anmelden(AnmeldenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    open_form("Kurse")
