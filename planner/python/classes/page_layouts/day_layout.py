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
#   Layout for daily entry. Populated with DayEntry.
#_______________________________________________________________________

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.free_write_entry import FreeWriteEntry

from classes.page_entries.day_entry import DayEntry
from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize


#_______________________________________________________________________
class OneDayLayout(TwoPageHalfLetterSize):

  #_____________________________________________________________________
  def  __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_DAY_LAYOUT_PATH
  ):
    super().__init__\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=file_path
      )
    return

  #_____________________________________________________________________
  def create_content(self):
    super().create_content()

    self.content_0_ =\
      DayEntry\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      , cycling_prompt_idx=2
      )

    self.content_1_ =\
      DayEntry\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      , cycling_prompt_idx=3
      )
#      FreeWriteEntry\
#      ( total_hght=self.content_hght_
#      , total_wdth=self.content_wdth_
#      , padding=Dims.BRD_MARGIN_PX
#      , page_header_txt=Strings.QUOTE0
#      )
#
    return

  #_____________________________________________________________________
  def add_content(self):
    super().add_content()
