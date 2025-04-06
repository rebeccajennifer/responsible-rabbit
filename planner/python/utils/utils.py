from classes.constants.style import PlannerFontStyle as Font
from classes.constants.style import PlannerColors as Colors

from math import floor
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
  def create_wrapped_text\
  ( text: str = ''
  , wdth: int = 0
  , font_size: int = Font.NORMAL_SIZE
  , font_family: int = Font.FONT_FAMILY_NORMAL
  ) -> Text:
    """
    SVGs do not support blocks of wrapped text. This function will take
    string and split it into multiple
    """

    if (font_size <= 0):
      raise ValueError

    max_chars_per_line: int = floor(wdth / (font_size / 2))

    lines: list = []

    words: list = text.split()

    current_line=''

    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    print(lines)

    group: Group = Group()
    line_inc: int = 1.2 * font_size
    text_y: int = 0

    for line in lines:
      txt: Text = Text\
      ( line
      , insert=(0, text_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL_TXT
      , font_size=Font.LITTLE_SIZE
      , font_family=Font.FONT_FAMILY_NORMAL
      )

      text_y = text_y + line_inc

      group.add(txt)

    return group

