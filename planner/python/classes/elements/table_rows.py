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
#   Block of rows for tables.
#_______________________________________________________________________

import svgwrite

from classes.constants.dims import PlannerDims as Dims
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors
from utils.utils import PlannerUtils as Utils

from classes.elements.rows import Rows
#_______________________________________________________________________
class TableRows(Rows):

  #_____________________________________________________________________
  def create_content(self):
    """
    Parameters:
      None

    Side Effects:
      Populates class variables for entries.
    """

    super().create_content()

    self.rows_: svgwrite.container.Group =\
      self.create_row_lines\
      ( total_len=self.content_wdth_
      , pad_lft=self.inner_pad_lft_
      , pad_rgt=self.inner_pad_rgt_
      , y_offset= 0
      , y_coord=self.y_coord_
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds svgwrite objects to class.

    Parameters:
      None

    Returns:
      None
    """

    self.add(self.rows_)
    return

  #_____________________________________________________________________
  def create_row_lines(self
    , total_len: int = 0
    , pad_lft: bool = False
    , pad_rgt: bool = False
    , y_offset: int = 0
    , y_coord: list = []
    ) -> svgwrite.container.Group:
    """
    Creates group of lines.

    Parameters:
      total_len : Total length of line / width of column
                  Does not account for padding; padding will reduce
                  the actual drawn length
      pad_lft   : Add padding to left, modifies length of drawn line
      pad_rgt   : Add padding to right, modifies length of drawn line
      y_coord   : List of y coordinates for line insertion
    """

    start_padding: int = Font.TEXT_PADDING/2 * pad_lft
    end_padding:   int = Font.TEXT_PADDING/2 * pad_rgt
    line_len:      int = total_len - start_padding - end_padding
    insert_x:      int = start_padding + self.insert_x_

    row_group: svgwrite.container.Group = svgwrite.container.Group()

    for y in y_coord:

      insert_y: int = y - y_offset

      row_line: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(insert_x, insert_y)
        , end=(insert_x + line_len, insert_y)
        , stroke=self.row_color_
        )

      row_group.add(row_line)

    return row_group

#_______________________________________________________________________
class DoubleTableRows(TableRows):
  """
  Double line rows for better spacing to allow for letter descenders,
  i.e. the bottom part of letters g, j, p, q, y
  """

  #_____________________________________________________________________
  def create_content(self):
    """
    Add two lines
    """

    super().create_content()

    y_coord: list = self.get_y_of_rows()

    y_offset: int = self.row_hght_ / 3

    self.double_rows_: svgwrite.container.Group =\
      self.create_row_lines\
      ( total_len=self.content_wdth_
      , pad_lft=self.inner_pad_lft_
      , pad_rgt=self.inner_pad_rgt_
      , y_offset=y_offset
      , y_coord=y_coord
      )

    return

  #_____________________________________________________________________
  def add_content(self) -> None:
    """
    Adds extra guideline row to table.

    Parameters:
      None

    Returns:
      None
    """

    super().add_content()
    self.add(self.double_rows_)
    return

