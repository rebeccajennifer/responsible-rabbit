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
#   Half-letter sheet layout
#_______________________________________________________________________

import svgwrite

from typing import Tuple
from copy import deepcopy

import svgwrite.container

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.page_layouts.half_letter_one_page import OnePageHalfLetterLayout


#_______________________________________________________________________
class TwoPageHalfLetterSize(svgwrite.Drawing):
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_LAYOUT_PATH
  , entry_0_type: type = None
  , entry_0_args: dict = {}
  , entry_1_type: type = None
  , entry_1_args: dict = {}
  ):

    self.is_portrait_   : bool  = is_portrait
    self.is_dbl_sided_  : bool  = is_dbl_sided
    self.file_path_     : str   = file_path

    #___________________________________________________________________
    # entry_type is type of page, e.g. day_entry, week_entry, etc
    #___________________________________________________________________
    if (not entry_0_type):
      self.entry_0_type_: type = OnePageHalfLetterLayout
    else:
      self.entry_0_type_: type = entry_0_type

    if (not entry_1_type):
      self.entry_1_type_: type = OnePageHalfLetterLayout
    else:
      self.entry_1_type_: type = entry_1_type

    self.entry_0_args_ = entry_0_args
    self.entry_1_args_ = entry_1_args

    #___________________________________________________________________
    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)

    super().__init__\
      ( self.file_path_
      , profile='tiny'
      , size=(wdth, hght)
      )
    #___________________________________________________________________

    self.content_wdth_, self.content_hght_ =\
       Dims.calc_border_size(self.is_portrait_)

    # Content insertion points for top left
    self.calc_border_insert_pts()
    self.create_content()
    self.add_content()

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Creates page borders, page header, content.

    Parameters:
      None

    Returns:
      None
    """

    EntryType0: type = self.entry_0_type_
    EntryType1: type = self.entry_1_type_

    self.content_0_ =\
      EntryType0\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      , addl_args=self.entry_0_args_
      )

    self.content_1_ =\
      EntryType1\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      , addl_args=self.entry_1_args_
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds content as class variables to page.

    Parameters:
      None

    Returns:
      None
    """

    x: int = self.insert_pt_border_0_[0]
    y: int = self.insert_pt_border_0_[1]
    self.content_0_['transform'] = f'translate({x}, {y})'

    x: int = self.insert_pt_border_1_[0]
    y: int = self.insert_pt_border_1_[1]
    self.content_1_['transform'] = f'translate({x}, {y})'

    self.add(self.content_0_)
    self.add(self.content_1_)

    return

  #_____________________________________________________________________
  def calc_border_insert_pts(self) -> None:
    """
    Determines top left insertion points for content boxes and borders.

    Side Effects:
      Adds class variables for insertion points.
    """

    content_wdth: int = self.content_wdth_
    content_hght: int = self.content_hght_

    if (self.is_portrait_):
      insert_pos00 = Dims.STD_MARGIN_PX
      insert_pos01 = Dims.BND_MARGIN_PX

      insert_pos10 = Dims.STD_MARGIN_PX
      insert_pos11 = content_hght\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos01 = Dims.STD_MARGIN_PX

    else:
      insert_pos00 = Dims.BND_MARGIN_PX
      insert_pos01 = Dims.STD_MARGIN_PX
      insert_pos11 = Dims.STD_MARGIN_PX

      insert_pos10 = content_wdth\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos00 = Dims.STD_MARGIN_PX

    insert_pos0: Tuple = (insert_pos00, insert_pos01)
    insert_pos1: Tuple = (insert_pos10, insert_pos11)

    self.insert_pt_border_0_: int =  insert_pos0
    self.insert_pt_border_1_: int =  insert_pos1

    return
