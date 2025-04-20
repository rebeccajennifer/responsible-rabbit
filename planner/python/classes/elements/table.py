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
#   Defines classes used to create tables.
#_______________________________________________________________________

import svgwrite

from classes.elements.base_element import VerticalStack
from classes.elements.rows import DualLineRowGroup
from classes.elements.rows import LineRowGroup
from classes.elements.rows import TextRowGroup
from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle

from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class DualLineTable(svgwrite.container.Group):
  """
  Table element with dual lines intended for writing.
  """

  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , header_txt: str = ''
  , text_style: TextBoxStyle = TextBoxStyle()
  , row_count: int = 1
  , show_outline: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  ):
    """
    Parameters:
      total_wdth  : Total width of table
      total_hght  : Total height of table
      header_txt  : Text contained in header
      text_style  : Style used for text header
      row_count   : Number of table rows
    """

    super().__init__()

    self.total_wdth_ = total_wdth

    self.header_ =\
      TextRowGroup\
      ( text=header_txt
      , total_wdth=total_wdth
      , style=text_style
      ).text_row_group_

    if (total_hght):
      line_row_hght = total_hght - self.header_.total_hght_

    else:
      line_row_hght = 0

    line_row_hght, row_hght = Utils.get_hght_from_rows\
      ( total_hght=line_row_hght
      , row_count=row_count
      )

    self.line_rows_: DualLineRowGroup =\
      DualLineRowGroup\
      ( total_wdth=self.total_wdth_
      , total_hght=line_row_hght
      , row_count=row_count
      , inner_pad_lft=inner_pad_lft
      , inner_pad_rgt=inner_pad_rgt
      )

    self.total_hght_: int=\
      self.header_.total_hght_ + self.line_rows_.total_hght_

    if (show_outline):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      )

    self.add(VerticalStack([self.header_, self.line_rows_]))

    return

#_______________________________________________________________________
class SingleLineTable(svgwrite.container.Group):
  """
  Table element with dual lines intended for writing.
  """

  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , header_txt: str = ''
  , text_style: TextBoxStyle = TextBoxStyle()
  , row_count: int = 1
  , show_outline: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  ):
    """
    Parameters:
      total_wdth  : Total width of table
      total_hght  : Total height of table
      header_txt  : Text contained in header
      text_style  : Style used for text header
      row_count   : Number of table rows
    """

    super().__init__()

    self.total_wdth_ = total_wdth

    self.header_ =\
      TextRowGroup\
      ( text=header_txt
      , total_wdth=total_wdth
      , style=text_style
      ).text_row_group_

    if (total_hght):
      line_row_hght = total_hght - self.header_.total_hght_

    else:
      line_row_hght = 0

    line_row_hght, row_hght = Utils.get_hght_from_rows\
      ( total_hght=line_row_hght
      , row_count=row_count
      )

    self.line_rows_: LineRowGroup=\
      LineRowGroup\
      ( total_wdth=self.total_wdth_
      , total_hght=line_row_hght
      , row_count=row_count
      , inner_pad_lft=inner_pad_lft
      , inner_pad_rgt=inner_pad_rgt
      ).svg_group_

    self.total_hght_: int=\
      self.header_.total_hght_ + self.line_rows_.total_hght_

    if (show_outline):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      )

    self.add(VerticalStack([self.header_, self.line_rows_]))

    return

