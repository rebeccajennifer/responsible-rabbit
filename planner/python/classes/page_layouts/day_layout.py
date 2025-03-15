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

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.entries.daily_schedule import DailySchedule as Sched
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
    Constructor for class. Assumes portrait orientation
    """
    super().__init__(
      is_portrait=False, is_dbl_sided=is_dbl_sided, file_path=file_path)

  #_____________________________________________________________________
  def add_content(self) -> None:

    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.25
    self.schedule_hght_: int = self.content_hght_

    self.schedule_ =\
      Sched.create_daily_schedule\
      ( wdth=self.schedule_wdth_
      , hght=self.schedule_hght_
      )

    insert_x_px: int = Dims.inch_to_px(self.insert_pt_0_[0])
    insert_y_px: int = Dims.inch_to_px(self.insert_pt_0_[1])

    self.schedule_['transform'] = f'translate({insert_x_px}, {insert_y_px})'

    self.layout_dwg_.add\
    (
      self.schedule_
    )


