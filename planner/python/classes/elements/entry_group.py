import svgwrite.container

from classes.elements.entry_table import EntryTable

class EntryRow(svgwrite.container.Group):
  """
  Horizonal group of Entry Tables.
  """

  #_____________________________________________________________________
  def __init__(self):
    super().__init__()

    # List representing row of entry tables
    self.entries_: list = []
    self.total_hght_: int = 0
    self.insert_x_: int = 0

    return

  #_____________________________________________________________________
  def add_entry(self, entry: EntryTable):

    self.entries_ = self.entries_ + [entry]
    self.update_hght()

    # Keep track of last item added to group to update placement
    entry['transform'] = f'translate({self.insert_x_}, {0})'
    self.insert_x_ = self.insert_x_ + entry.total_wdth_

    self.add(entry)

    return

  #_____________________________________________________________________
  def update_hght(self) -> int:
    """
    Calculates max height of entries.

    Side Effects:
      Updates total_hght_.

    Parameters:
      None

    Returns:
      None
    """

    self.total_hght_: int = 0

    for entry in self.entries_:

      if (entry.total_hght_ > self.total_hght_):
        self.total_hght_ = entry.total_hght_

    return
