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

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.style import PlannerFontStyle as Font
from classes.style.std_styles import StdLineRowGroupStyles
from classes.style.std_styles import StdTextBoxStyles

from classes.elements.daily_schedule import DaySchedule as DaySched
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.elements.table import ColumnTable

from classes.page_layouts.half_letter_one_page import OnePageHalfLetterLayout


#_______________________________________________________________________
class DayEntry(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  DEF_DAY_LAYOUT_PATH: str =\
    'day#-layout.svg'

  DAYS: str =\
    'Mon' + 2 * Strings.SPACE +\
    'Tue' + 2 * Strings.SPACE +\
    'Wed' + 2 * Strings.SPACE +\
    'Thu' + 2 * Strings.SPACE +\
    'Fri' + 2 * Strings.SPACE +\
    'Sat' + 2 * Strings.SPACE +\
    'Sun' + 2 * Strings.SPACE + Strings.DATE_STR

  DAY_PRIMARY_EFFORTS: list =\
    ['Primary Efforts', 'Alignment']

  DAY_TODO: str =\
    'To Do'

  DAY_FOCUS: str =\
    'Today I will pay most attention to:'

  DAY_GRATITUDE: str =\
    'Gratitude'

  DAY_ACHIEVEMENT: str =\
    'A tiny triumph or epic win...'

  DAY_CHECK_IN: str =\
    'Emotional and values check-in:'

  DAY_PROMPTS: str =\
    [ 'Where can I invite more ease?'
    , 'What roadblock do I need to address?'
    , 'How can I embrace discomfort?'
    , 'What am I avoiding?'
    , 'What can I let go of?'
    , 'What am I learning about myself?'
    , 'How can I care for myself today?'
    ]

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    self.cycling_prompt_idx_: int =\
      addl_args[Key.CYCLING_PROMPT_IDX]

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
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
      , header_txt_lst=self.DAY_PRIMARY_EFFORTS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=False
      , TableType=DualLineTable
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=self.DAY_TODO
      , row_count=6
      , text_style=StdTextBoxStyles.MED_BACK_NORMAL_FONT
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=self.DAY_PROMPTS[self.cycling_prompt_idx_]
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=self.DAY_ACHIEVEMENT
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=1
      , show_outline=True
      , pri_line_style=StdLineRowGroupStyles.DOTTED
      )

    , DualLineTable
      ( total_wdth=self.main_content_wdth_
      , header_txt=self.DAY_CHECK_IN
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
      , header_txt=self.DAY_GRATITUDE
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
      (header_txt=self.DAYS, font_family=Font.FONT_FAMILY_HEADER)
