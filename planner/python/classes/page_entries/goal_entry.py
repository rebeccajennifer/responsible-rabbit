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
#   Entry for goal. Fills content for one half sheet.
#_______________________________________________________________________

from copy import deepcopy
import svgwrite.container

from classes.constants.strings import PlannerStrings as Strings

from classes.elements.table import ColumnTable
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable

from classes.page_layouts.half_page_layout import HalfPageLayout

from classes.style.style import PlannerFontStyle as Font
from classes.style.std_styles import StdTextBoxStyles

class GoalStrings:
  #_____________________________________________________________________
  # Goal layout strings
  #_____________________________________________________________________

  CHECKLIST: str =\
     '[] Specific'    + Strings.SPACE\
   + '[] Measureable' + Strings.SPACE\
   + '[] Achievable'  + Strings.SPACE\
   + '[] Relevant'    + Strings.SPACE\
   + '[] Challenging'

  ACTIONS: str =\
    'Critical Steps'

  MILESTONES: list =\
  [ 'Advancement'
  , 'Date'
  ]

  MEASUREMENT: str =\
    'Tangible Results'

  OBSTACLES: str =\
    'Obstacles'

  LIFE_IMPROVEMENT: str =\
    'Impacts of Success'

  PLAN: str =\
    'Commitment Cadence'

  REWARD: str =\
    'Celebration Plan'

  MONTHS: list =\
  [ 'Month 1:'
  , 'Month 2:'
  , 'Month 3:'
  ]

  VALUES: str =\
    'How does this goal support your values?'


#_______________________________________________________________________
class GoalEntry(HalfPageLayout):
  """
  Daily entry layout.
  """
  PAGE_HEADER_TXT: str = 'Goal #'

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , addl_args=addl_args
      )

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Side Effects:
      Populates self.entries_ class variable.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    self.entries_: list =\
    [ DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=GoalStrings.VALUES
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=False
      )
    , ColumnTable\
      ( total_wdth=self.content_wdth_
      , header_txt_lst=GoalStrings.MILESTONES
      , text_style=StdTextBoxStyles.WHT_BACK_HEADER_FONT_NO_OUTLNE
      , row_count=7
      , col_wdths=[275, -1]
      , TableType=DualLineTable
      , show_outline=True
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=GoalStrings.MEASUREMENT
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=1
      , show_outline=False
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=GoalStrings.OBSTACLES
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=True
      )

    , DualLineTable\
      ( total_wdth=self.content_wdth_
      , header_txt=GoalStrings.LIFE_IMPROVEMENT
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=2
      , show_outline=False
      )
   ]

    # Calculate remaining height to evenly distribute spanning tables
    fill_hght: int =\
      self.calc_remaining_hght_per_element(2)

    self.entries_ = self.entries_ +\
    [ SingleLineTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=GoalStrings.PLAN
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=True
      )

    , SingleLineTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=GoalStrings.REWARD
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=True
      )
    ]

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """

    style = deepcopy(StdTextBoxStyles.DEF_PAGE_HEADER_TXT)
    style.font_size_ = Font.GOAL_HEADER_TXT_SIZE

    return super().create_page_header\
      ( header_txt=self.PAGE_HEADER_TXT
      , style=style
      )
