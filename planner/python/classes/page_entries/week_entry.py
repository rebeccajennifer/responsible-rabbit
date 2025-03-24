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
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from classes.elements.entry_group import EntryRow
from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import NumberedTable
from classes.elements.entry_table import PromptTable
from classes.elements.header_box import HeaderBox

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
    [ PromptTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_ACCOMPLISHMENTS
      , entry_row_count=4
      , pad_top=True
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_IMPROVEMENT
      , entry_row_count=4
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_GRATITUDE
      , entry_row_count=3
      , pad_top=True
      , show_outline=False
      )

    , HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=[Strings.WEEK_FULFILLMENT]
      , font=Font.FONT_FAMILY_HEADER
      , pad_top=True
      )
    ]

    # Calculate remaining height to evenly distribute spanning tables
    remaining_hght: int = self.calc_remaining_hght()

    self.entries_ = self.entries_ +\
    [ EntryTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_0
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_1
      , pad_top=True
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
    font_size: int = Font.WEEK_PAGE_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_HEADER

    page_header = super().create_page_header\
      ( header_txt=Strings.WEEK_PAGE_HEADER_0
      , font_size=font_size
      , font=font_family
      , box_fill_color=Colors.DEF_PAGE_HEADER_COLOR
      )

    return page_header

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
      , entry_row_count=5
      , pad_top=True
      , pad_bot=True
      , pad_rgt=True
      )
    )

    goal_row_0.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 2'
      , entry_row_count=5
      , pad_top=True
      , pad_bot=True
      , pad_lft=True
      )
    )

    goal_row_1.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 3'
      , entry_row_count=5
      , pad_top=True
      , pad_bot=True
      , pad_rgt=True
      )
    )

    goal_row_1.add_entry\
    (
      EntryTable\
      ( wdth=half_content_width
      , header_txt='Goal 4'
      , entry_row_count=5
      , pad_top=True
      , pad_bot=True
      , pad_lft=True
      )
    )

    self.entries_: list =\
    [ goal_row_0
    , goal_row_1
    , HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_CHECKLIST
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_top=True
      , pad_rgt=True
      )
    , PromptTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_LOOKING_FORWARD
      , entry_row_count=4
      , pad_top=True

      )
    ]

    """
    self.entries_: list =\
    [ PromptTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_ACCOMPLISHMENTS
      , entry_row_count=4
      , pad_top=True
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_IMPROVEMENT
      , entry_row_count=4
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.WEEK_GRATITUDE
      , entry_row_count=3
      , pad_top=True
      , show_outline=False
      )

    , HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=[Strings.WEEK_FULFILLMENT]
      , font=Font.FONT_FAMILY_HEADER
      , pad_top=True
      )
    ]

    # Calculate remaining height to evenly distribute spanning tables
    remaining_hght: int = self.calc_remaining_hght()

    self.entries_ = self.entries_ +\
    [ EntryTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_0
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.WEEK_FULFILLMENT_AREAS_1
      , pad_top=True
      )
    ]
    """

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.WEEK_PAGE_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_HEADER

    page_header = super().create_page_header\
      ( header_txt=Strings.WEEK_PAGE_HEADER_1
      , font_size=font_size
      , font=font_family
      , box_fill_color=Colors.DEF_PAGE_HEADER_COLOR
      )

    return page_header

