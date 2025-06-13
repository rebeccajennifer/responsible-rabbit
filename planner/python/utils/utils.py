import svgwrite.container
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

    Parameters:
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

    Parameters:
      txt         : The input text to wrap.
      px_wdth     : The maximum width (in pixels) allowed for each line.
      font_size   : Size of text font
      font_family : Font of text

    Returns:
        List[str]: A list of strings, each representing a line of wrapped text.
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
  ( total_hght: int = 0
  , row_count: int = 1
  , row_hght: int = 30
  ) -> tuple:
    """
    Returns total height and row height from number of rows. Will
    calculate row height if total height is given. Will calculate
    total height if row height is given. If both total height and row
    height are given, will recalculate row height.

    Parameters:
      total_hght  : Total height of combined rows
      row_count   : Number of rows
      row_hght    : Height of rows

    Returns:
      tuple       : (total height, row height)
    """

    if ( (not row_count) or (not total_hght and not row_hght)):
      raise ValueError(Err.INSUFFICIENT_ARGS)

    if (total_hght):
      row_hght = total_hght / row_count

    else:
      total_hght = row_hght * row_count

    return (total_hght, row_hght)

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

    Parameters:
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




