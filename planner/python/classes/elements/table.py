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
import svgwrite.container

from classes.elements.base_element import HorizontalStack
from classes.elements.base_element import VerticalStack
from classes.elements.row_group import DualLineRowGroup
from classes.elements.row_group import LineRowGroup
from classes.elements.row_group import TextRowGroup
from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle
from classes.style.style import PlannerColors as Colors
from classes.style.std_styles import StdLineRowGroupStyles

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
  , pri_line_style: LineRowGroupStyle =\
      StdLineRowGroupStyles.ONE_THIRD_OFFSET
  , sec_line_style: LineRowGroupStyle =\
      StdLineRowGroupStyles.DOTTED

  ):
    """
    Parameters:
      total_wdth    : Total width of table
      total_hght    : Total height of table
      header_txt    : Text contained in header
      text_style    : Style used for text header
      row_count     : Number of table rows
      show_outline  : If true, will outline the table
      inner_pad_lft : Add padding to the left side of column
      inner_pad_rgt : Add padding to the right side of column
    """

    super().__init__()

    self.total_wdth_ = total_wdth

    self.header_ =\
      TextRowGroup\
      ( text=header_txt
      , total_wdth=total_wdth
      , style=text_style
      )

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
      , pri_line_style=pri_line_style
      , sec_line_style=sec_line_style
      )

    self.total_hght_: int=\
      self.header_.total_hght_ + self.line_rows_.total_hght_

    self.add(VerticalStack([self.header_, self.line_rows_]))

    if (show_outline):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      , outline_color=Colors.BORDER_COLOR
      )

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
      )

    if (total_hght):
      line_row_hght = total_hght - self.header_.total_hght_

    else:
      line_row_hght = 0

    line_row_hght, row_hght = Utils.get_hght_from_rows\
      ( total_hght=line_row_hght
      , row_count=row_count
      )

    style: LineRowGroupStyle = LineRowGroupStyle()
    style.inner_pad_lft_ = inner_pad_lft
    style.inner_pad_rgt_ = inner_pad_rgt

    self.line_rows_: LineRowGroup=\
      LineRowGroup\
      ( total_wdth=self.total_wdth_
      , total_hght=line_row_hght
      , row_count=row_count
      , style=style
      )

    self.total_hght_: int=\
      self.header_.total_hght_ + self.line_rows_.total_hght_

    self.add(VerticalStack([self.header_, self.line_rows_]))

    if (show_outline):
      Utils.add_outline\
      ( container=self
      , hght=self.total_hght_
      , wdth=self.total_wdth_
      , outline_color=Colors.BORDER_COLOR
      )

    return

#_______________________________________________________________________
class ColumnTable(svgwrite.container.Group):

  def __init__(self
  , total_wdth: int = 0
  , total_hght: int = 0
  , header_txt_lst: list = []
  , text_style: TextBoxStyle = TextBoxStyle()
  , row_count: int = 1
  , col_wdths: list = []
  , show_outline: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , TableType = 0
  ):
    """
    Parameters:
      header_txt_lst  : List of headers for table.

      total_wdth    : Total width of table
      total_hght    : Total height of table
      header_txt_lst: List of text in headers
      text_style    : Style used for text header
      col_wdths     : Width of columns,
                      -1 indicates to equally fill all available space
      show_outline  : If true, will outline the table
      inner_pad_lft : Add padding to the left side of columns
      inner_pad_rgt : Add padding to the right side of columns
    """

    super().__init__()

    if (not TableType):
      TableType = SingleLineTable

    columns: list = []

    col_wdths: list = Utils.calc_col_wdths(total_wdth=total_wdth
      , col_count=len(header_txt_lst)
      , col_wdths=col_wdths
      )

    for i in range(len(header_txt_lst)):

      columns.append( TableType\
        ( total_wdth=col_wdths[i]
        , total_hght=total_hght
        , header_txt=header_txt_lst[i]
        , text_style=text_style
        , row_count=row_count
        , inner_pad_lft=inner_pad_lft
        , inner_pad_rgt=inner_pad_rgt
        )
      )

    self.total_hght_ = columns[0].total_hght_
    self.total_wdth_ = total_wdth

    self.add(HorizontalStack(obj_list=columns))

    if (show_outline):
      Utils.add_outline(self, hght=self.total_hght_, wdth=self.total_wdth_)


