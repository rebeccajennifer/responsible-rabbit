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
#   Layout for week . Populated with entry group for week.
#_______________________________________________________________________

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings

from classes.page_entries.free_write_prompt_entry import FreeWritePromptEntry
from classes.page_entries.free_write_entry import FreeWriteEntry
from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize


#_______________________________________________________________________
class FreeWriteLayout(TwoPageHalfLetterSize):

  #_____________________________________________________________________
  def  __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_LAYOUT_PATH
  , header_txt_0: str = ''
  , prompt_0: str = ''
  , header_txt_1: str = ''
  , prompt_1: str = ''
  ):

    self.header_txt_0_: str = header_txt_0
    self.prompt_0_: str = prompt_0

    self.header_txt_1_: str = header_txt_1
    self.prompt_1_: str = prompt_1

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
      FreeWritePromptEntry\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      , header_txt=self.header_txt_0_
      , prompt=self.prompt_0_
      )

    if (not self.header_txt_1_):
      self.content_1_ =\
        FreeWriteEntry\
        ( total_hght=self.content_hght_
        , total_wdth=self.content_wdth_
        , padding=Dims.BRD_MARGIN_PX
        , page_header_txt=self.header_txt_0_
        )

    else:
      self.content_1_ =\
        FreeWritePromptEntry\
        ( total_hght=self.content_hght_
        , total_wdth=self.content_wdth_
        , padding=Dims.BRD_MARGIN_PX
        , header_txt=self.header_txt_1_
        , prompt=self.prompt_1_
        )


    return

  #_____________________________________________________________________
  def add_content(self):
    super().add_content()
