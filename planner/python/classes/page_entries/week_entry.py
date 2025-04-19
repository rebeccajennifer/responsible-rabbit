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
#   Entry for week. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerFontStyle as Font

from classes.elements.base_element import VerticalStack
from classes.elements.entry_group import EntryRow
from classes.elements.entry_table import EntryTable
from classes.elements.header_box import HeaderBox
from classes.elements.rows import TextRowGroup
from classes.elements.table import WriteTable

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class WeekEntry0(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , padding=padding
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
    [ WriteTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_ACCOMPLISHMENTS
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , show_outline=False
      , row_count=2
      , inner_pad_lft=True
      , inner_pad_rgt=True
      )

    , WriteTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_LESSONS_LEARNED
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=3
      , show_outline=True
      )

    , WriteTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_UNFINISHED_BUSINESS
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=2
      , show_outline=False
      )

      , VerticalStack\
        (
          [
             TextRowGroup\
            ( total_wdth=self.content_wdth_
            , text=Strings.WEEK_VISUALIZATION_HEADER
            , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
            ).text_row_group_

          , WriteTable\
            ( total_wdth=self.content_wdth_
            , total_hght=150
            , header_txt=Strings.WEEK_VISUALIZATION_PROMPT
            , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
            , show_outline=True
            )
          ]
        )

    , WriteTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_IMPROVEMENT
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=2
      , show_outline=False
      )
    , WriteTable\
      ( total_wdth=self.content_wdth_
      , header_txt=Strings.WEEK_LOOKING_FORWARD
      , text_style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
      , row_count=1
      , show_outline=False
      )

    ]

    fill_hght: int = self.calc_remaining_hght_per_element()

    self.entries_.insert(4,
      WriteTable\
      ( total_wdth=self.content_wdth_
      , total_hght=fill_hght
      , header_txt=Strings.WEEK_GRATITUDE
      , text_style=StdTextBoxStyles.MED_BACK_HEADER_FONT
      , row_count=1
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
      (header_txt=Strings.WEEK_PAGE_HEADER_0)

#_______________________________________________________________________
class WeekEntry1(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , padding=padding
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

    half_content_width: int = self.content_wdth_ / 2

    goal_row_0: EntryRow = EntryRow()
    goal_row_1: EntryRow = EntryRow()

    goal_row_0.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 1'
      , row_count=3
      , pad_rgt=True
      , show_outline=False
      )
    )

    goal_row_0.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 2'
      , row_count=3
      , pad_lft=True
      , show_outline=False
      )
    )

    goal_row_1.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 3'
      , row_count=3
      , pad_rgt=True
      , show_outline=False
      )
    )

    goal_row_1.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 4'
      , row_count=3
      , pad_lft=True
      , show_outline=False
      )
    )

    self.entries_: list =\
    [ EntryTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_HABIT_TRACKER_HEADINGS
      , box_fill_color='none'
      , font=Font.FONT_FAMILY_NORMAL
      , col_count=10
      , col_wdths=[-1, 40] + 7 * [25] + [40]
      , row_count=6
      )

    , goal_row_0
    , goal_row_1

    , HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_CHECKLIST
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_rgt=True
      )

    , HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=[Strings.WEEK_FULFILLMENT]
      , font=Font.FONT_FAMILY_HEADER
      )
    ]

    # Calculate remaining height to evenly distribute spanning tables
    fill_hght: int = self.calc_remaining_hght_per_element(2)

    self.entries_ = self.entries_ +\
    [ EntryTable\
      ( wdth=self.content_wdth_
      , hght=fill_hght
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_0
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , hght=fill_hght
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_1
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
    return\
      super().create_page_header(header_txt=Strings.WEEK_PAGE_HEADER_1)