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
#   Utility functions.
#_______________________________________________________________________

from os.path import isdir
from os.path import dirname
from os import mkdir
from os import remove
from pypdf import PdfReader
from pypdf import PdfWriter

from classes.style.style import PlannerFontStyle as Font
from classes.style.style import PlannerColors as Colors
from classes.constants.error_strings import ErrorStrings as Err
from classes.constants.dims import PlannerDims as Dims

from math import floor

import svgwrite

from svgwrite.text import Text
from svgwrite.container import Group


#_____________________________________________________________________
class PlannerUtils:
  """
  Utilities for planner.
  """

  #_____________________________________________________________________
  def calc_col_wdths\
    ( total_wdth: int
    , col_count: int
    , col_wdths: list
    ) -> list:
    """
    Calculates columns widths.

    Parameters
      col_count: Number of columns
      col_wdths: List of column widths. One element of list should be -1
                 -1 indicates to span that column to the remaining width
    """

    #___________________________________________________________________
    # Column width calculation and error handling
    #
    # If no column widths specified, or number of elements in column
    # width list does not match the number of columns, make all columns
    # equal.
    #___________________________________________________________________
    if ( (not col_wdths) or len(col_wdths) != col_count):
      col_wdths = col_count * [total_wdth / col_count]

    # List of col indices to span remaining width
    span_col_idx: list = []
    # Running sum of indicated column widths
    wdth_sum: int = 0

    for i in range(len(col_wdths)):
      if (col_wdths[i] == -1):
        span_col_idx = span_col_idx + [i]

      else:
        wdth_sum = wdth_sum + col_wdths[i]

    span_col_count: int = len(span_col_idx)

    # Replace col width elements that should span remaining space
    if (span_col_count):
      remainder_col_wdth: int = (total_wdth - wdth_sum) / span_col_count

      for i in range(span_col_count):
        col_wdths[span_col_idx[i]] = remainder_col_wdth

    return col_wdths

  #_____________________________________________________________________
  def split_txt_by_wdth\
  ( txt: str = ''
  , px_wdth: int = 0
  , font_size: int = Font.NORMAL_SIZE
  , font_family: int = Font.FONT_FAMILY_NORMAL
  ) -> list[str]:
    """
    Splits a given string into a list of lines, where each line fits
    within the specified width.

    Parameters
      txt         : Input text to wrap.
      px_wdth     : Maximum width (in pixels) allowed for each line.
      font_size   : Size of text font.
      font_family : Font of text.

    Returns
        List[str]: A list of strings, each representing a line of
        wrapped text.
    """

    if (font_size <= 0):
      raise ValueError

    max_chars_per_line: int =\
      floor(px_wdth / (font_size / Font.WDTH_MULTPLIER[font_family]))

    lines: list = []
    paragraphs: list = txt.split('\n')

    # Iterate through paragraphs
    for i in range(len(paragraphs)):

      para_words: list = paragraphs[i].split()
      current_line: str = ''

      for word in para_words:
          if len(current_line) + len(word) + 1 <= max_chars_per_line:
              current_line += (' ' if current_line else '') + word
          else:
              lines.append(current_line)
              current_line = word

      lines.append(current_line)

      # Don't add an extra line at the end of the text string list
      if (i != len(paragraphs) - 1):
        lines.append('')

    #___________________________________________________________________
    # TODO refactor logic - this feels hacky
    #___________________________________________________________________
    # Just return the original string if the text string doesn't need to
    # be split - the split code above will destroy intentional white
    # space which is sometimes used for headers.
    #___________________________________________________________________
    if (len(lines) == 1):
      lines = [txt]
    #___________________________________________________________________

    return lines

  #_____________________________________________________________________
  def get_hght_from_rows\
  ( hght: int = 0
  , row_count: int = 1
  , row_hght: int = 30
  ) -> tuple:
    """
    Returns total height and row height from number of rows. Will
    calculate row height if total height is given. Will calculate
    total height if row height is given. If both total height and row
    height are given, will recalculate row height.

    Parameters
      total_hght  : Total height of combined rows
      row_count   : Number of rows
      row_hght    : Height of rows

    Returns
      tuple       : (total height, row height)
    """

    if ( (not row_count) or (not hght and not row_hght)):
      raise ValueError(Err.INSUFFICIENT_ARGS)

    if (hght):
      row_hght = hght / row_count

    else:
      hght = row_hght * row_count

    return (hght, row_hght)

  #_____________________________________________________________________
  def add_outline\
  ( container = svgwrite
  , hght: int = 0
  , wdth: int = 0
  , outline_color: str = Colors.BORDER_COLOR
  , backgnd_color: str = 'none'
  ) -> svgwrite:
    """
    Creates rectangular outline around box.

    Parameters
      None
    """

    container.add\
    (
      svgwrite.shapes.Rect\
      ( size=(wdth, hght)
      , insert=(0,0)
      , stroke=outline_color
      , fill=backgnd_color
      , stroke_width=1
      )
    )

    return container

  #_____________________________________________________________________
  def inc(i: int = 0):
    """
    Generator that yields incrementing integers, similar to `i++` in C.

    Parameters
      i (int): Starting value (default is 0).

    Yields:
      int: The current counter value, starting from `i` and incrementing
      by 1.
    """
    while True:
      #_________________________________________________________________
      # Keyword yield pauses the function and returns a value to
      # caller, but keeps function’s state alive
      # so it can resume where it left off.
      #_________________________________________________________________
      yield i
      #_________________________________________________________________
      i += 1

  #_____________________________________________________________________
  def split_list(lst: list, n: int) -> list:
    """
    Splits a list into n approximately equal parts.

    Parameters
      lst (list): The list to be split.
      n (int)   : The number of parts to split the list into.

    Returns
      list: A list containing n sublists, each representing a part of
      the original list.
    """

    if n <= 0:
        raise ValueError('Number of parts must be a positive integer.')

    # Calculate the size of each part and the number of parts that need
    # to be one element larger to account for any remainder
    k, m = divmod(len(lst), n)

    result = []

    for i in range(n):

        # Calculate the start index for the i-th sublist
        # (i * k) gives the base start, min(i, m) distributes the
        # remainder
        start = i * k + min(i, m)

        # Calculate the end index for the i-th sublist
        end = (i + 1) * k + min(i + 1, m)

        result.append(lst[start:end])
    return result