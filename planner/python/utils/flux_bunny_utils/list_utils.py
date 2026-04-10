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
#   Copyright 2025, Rebecca Rashkin
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
#   List utility functions.
#_______________________________________________________________________


#_______________________________________________________________________
class ListUtils:
  """
  Utilities related to list operations.
  """

  #_____________________________________________________________________
  def split_list(lst: list, n: int) -> list:
    """
    Splits a list into n approximately equal parts.

    Parameters:
      lst (list): The list to be split.
      n (int)   : The number of parts to split the list into.

    Returns:
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