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
#   Layout for daily entry.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.style import PlannerFontStyle as Font
from classes.style.std_styles import StdLineRowGroupStyles
from classes.style.std_styles import StdTextBoxStyles

from classes.elements.daily_schedule import DaySchedule as DaySched
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.elements.table import ColumnTable

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class DayEntry(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  , cycling_prompt_idx: int = 6
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    self.cycling_prompt_idx_: int = cycling_prompt_idx

    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , padding=padding
      )

    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    Add content to layout.

    Parameters:
      None

    Returns:
      None
    """
    super().add_content()

    #___________________________________________________________________
    sched_insert_x: int = self.content_insert_pt_x_\
      + self.content_wdth_\
      - self.schedule_wdth_\
      + Dims.BRD_MARGIN_PX * self.sched_.pad_lft_

    sched_insert_y: int = self.content_insert_pt_y_

    self.sched_['transform'] =\
      f'translate({sched_insert_x},{sched_insert_y})'

    self.add(self.sched_)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.30
    self.main_content_wdth_: int =\
      self.content_wdth_ - self.schedule_wdth_ - Dims.BRD_MARGIN_PX

    self.sched_: DaySched =\
      DaySched\
      ( wdth=self.schedule_wdth_
      , hght=self.content_hght_
      , time_inc_min=30
      , use_24=True
      )

    self.entries_: list =\
    [ DualLineTable\
      ( total_wdth=self.main_content_wdth_
      , header_txt='Values'
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=3
      , show_outline=False
      , inner_pad_lft=True
      , inner_pad_rgt=True
      )

    , ColumnTable
      ( total_wdth=self.main_content_wdth_
      , header_txt_lst=Strings.DAY_PRIMARY_EFFORTS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=False
      , TableType=DualLineTable
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_TODO
      , row_count=6
      , text_style=StdTextBoxStyles.MED_BACK_NORMAL_FONT
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PROMPTS[self.cycling_prompt_idx_]
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_ACHIEVEMENT
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=Strings.DAY_PROMPT_LAST_24
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=True
      )
    ]

    fill_hght: int = self.calc_remaining_hght_per_element(1)

    self.entries_.insert(3,
      SingleLineTable\
      ( total_wdth=self.main_content_wdth_
      , total_hght=fill_hght
      , header_txt=Strings.DAY_GRATITUDE
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_W_OUTLNE
      , show_outline=True
      )
    )

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """

    return super().create_page_header\
      (header_txt=Strings.DAYS, font_family=Font.FONT_FAMILY_HEADER)
