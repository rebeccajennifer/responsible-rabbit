
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

