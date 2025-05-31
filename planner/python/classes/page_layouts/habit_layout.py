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
#   Layout for habit tracker. Habit tracker is divider.
#_______________________________________________________________________

from os import path

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.habit_entry import HabitTracker
from classes.page_layouts.half_letter_divider import DividerPage


#_______________________________________________________________________
class HabitLayout(DividerPage):

  #_____________________________________________________________________
  def  __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_name: str = Strings.DEF_HABIT_LAYOUT_PATH
  , out_dir: str = ''
  , divider_pos: int = 0
  ):

    super().__init__\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_name=file_name
      , out_dir=out_dir
      , divider_pos=divider_pos
      , divider_str='Today'
      )
    return

  #_____________________________________________________________________
  def create_content(self):
    super().create_content()

    self.content_0_ =\
      HabitTracker\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      )

    self.content_1_ =\
      HabitTracker\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    super().add_content()
