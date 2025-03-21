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
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font
from classes.elements.daily_schedule import DailySchedule as Sched
from classes.elements.header_box import HeaderBox
from classes.elements.entry_table import EntryTable
from classes.page_layouts.half_letter_layout import HalfLetterSize


#_______________________________________________________________________
class DayLayout(HalfLetterSize):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_DAY_LAYOUT_PATH):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( is_portrait=False
      , is_dbl_sided=is_dbl_sided
      , file_path=file_path
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

    insert_sched_x: int =\
      self.insert_pt_content_0_[0]\
    + self.content_wdth_ - self.schedule_wdth_

    insert_x_px: int = insert_sched_x
    insert_y_px: int = self.insert_pt_content_0_[1]

    self.schedule_['transform'] =\
      f'translate({insert_x_px}, {insert_y_px})'

    #self.pri_efforts_box_['transform'] =\
    #  f'translate({self.insert_pt_content_0_[0] }, {self.insert_pt_content_0_[1] + self.page_header_.hght_})'

    #self.layout_dwg_.add(self.pri_efforts_box_)
    self.layout_dwg_.add(self.schedule_)

    self.entry_: EntryTable =\
      EntryTable\
      ( wdth=self.content_wdth_ - self.schedule_.wdth_
      , hght=self.content_hght_0_
      , text_lst=['hello', 'trevor']
      , entry_row_count=20
      , pad_top=True
      , pad_lft=True
      )

    entry_insert_x: int = self.insert_pt_content_0_[0]\
      + Dims.BRD_MARGIN_PX * self.entry_.pad_lft_

    entry_insert_y: int = self.insert_pt_content_0_[1]\
      + Dims.BRD_MARGIN_PX * self.entry_.pad_top_

    self.entry_['transform'] =\
      f'translate({entry_insert_x},{entry_insert_y})'

    self.layout_dwg_.add(self.entry_)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables:
      self.schedule_

    Parameters:
      None

    Returns:
      None

    """

    super().create_content()

    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.25
    self.schedule_hght_: int = self.content_hght_0_

    self.schedule_ =\
      Sched\
      ( strt_time_str = Sched.DEF_STRT_24
      , stop_time_str = Sched.DEF_STOP_24
      , wdth=self.schedule_wdth_
      , hght=self.schedule_hght_
      , time_inc_min=30
      , use_24=True
      )

    self.main_content_wdth_: int = self.content_wdth_\
      - self.schedule_.wdth_\
      - Dims.BRD_MARGIN_PX

    #self.pri_efforts_box_ =\
    # EntryTable\
    #  ( wdth=main_content_wdth_
    #  , hght=self.content_hght_
    #  , text_lst=['Primary Efforts', 'Alignment']
    #  , font_size=Font.PROMPT_SIZE
    #  , font=Font.FONT_FAMILY_PROMPT
    #  )

    return

  #_____________________________________________________________________
  def create_page_headers(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.NORMAL_SIZE
    font_family: str = Font.FONT_FAMILY_NORMAL
    sp: str ='\u00A0\u00A0\u00A0'

    days: str =\
      'Mon' + sp + sp +\
      'Tue' + sp + sp +\
      'Wed' + sp + sp +\
      'Thu' + sp + sp +\
      'Fri' + sp + sp +\
      'Sat' + sp + sp +\
      'Sun'

    page_header_0 = super().create_page_header\
      ( header_txt=days
      , font_size=font_size
      )

    page_header_1 = super().create_page_header\
      ( header_txt=Strings.QUOTE0
      , font_size=font_size
      )

    date_str: str = '____ / ____ / 20 ____'

    insert_date_x: int = self.content_wdth_ - Font.TEXT_PADDING
    insert_date_y: int = font_size + Font.TEXT_PADDING

    date_txt: svgwrite.text.Text =\
      svgwrite.text.Text\
      ( text=date_str
      , insert=(insert_date_x, insert_date_y)
      , text_anchor='end'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL
      , font_size=font_size
      , font_family=font_family
      )

    page_header_0.add(date_txt)

    return page_header_0, page_header_1
