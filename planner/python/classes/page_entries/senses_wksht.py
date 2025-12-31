#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2024, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   Worksheet for Five Senses grounding exercise.
#_______________________________________________________________________


from classes.elements.table import DualLineTable
from classes.style.std_styles import StdTextBoxStyles
from classes.page_layouts.half_page_layout import HalfPageLayout


#_______________________________________________________________________
class SensesWksht(HalfPageLayout):
  """
  Layout for ACE exercise
  """

  PAGE_HEADER_TXT: str = 'Five Senses Grounding Exercise'

  SEE   : str = 'See:   Name 5 things you see.'
  TOUCH : str = 'Touch: Name 4 things you can physically feel.'
  HEAR  : str = 'Hear:  Name 3 things you hear.'
  SMELL : str = 'Smell: Name 2 things you smell.'
  TASTE : str = 'Taste: Name 1 thing you can taste.'

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Parameters
      None

    Side Effects
      Populates self.entries_ class variable.

    Returns
      None
    """
    super().create_content()

    header_style = StdTextBoxStyles.LTE_BACK_HEADER_FONT

    self.entries_: list =\
    [ DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=10
      , total_hght=220
      , header_txt=self.SEE
      , text_style=header_style
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=8
      , total_hght=180
      , header_txt=self.TOUCH
      , text_style=header_style
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=6
      , total_hght=140
      , header_txt=self.HEAR
      , text_style=header_style
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=2
      , total_hght=60
      , header_txt=self.SMELL
      , text_style=header_style
      , show_outline=True
      )
    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , row_count=1
      , total_hght=40
      , header_txt=self.TASTE
      , text_style=header_style
      , show_outline=True
      )
    ]

    return
