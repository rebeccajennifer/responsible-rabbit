from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from classes.elements.rows import RowGroup
from classes.elements.rows import LineRowGroup
from classes.elements.rows import TextRowGroup


#_______________________________________________________________________
class SimpleTable:
  """
  """

  def __init__(self
  , header_txt: str = ''
  , font_family: str = Font.FONT_FAMILY_NORMAL
  , font_size: int = Font.NORMAL_SIZE
  , total_hght: int = 0
  , total_wdth: int = 0
  , show_outline: bool = True
  , outline_color: str = Colors.BORDER_COLOR
  , backgnd_color: str = 'none'
  , row_hght: int = RowGroup.DEF_ROW_HGHT
  , y_offset: int = 0
  , inner_pad_top: bool = False
  , inner_pad_bot: bool = False
  , inner_pad_lft: bool = False
  , inner_pad_rgt: bool = False
  , obj_list: list = []



  ):
    """
    Parameters:
      header_txt  : Text contained in header
      font_family : Font of header text
      font_size   : Size of header text
      total_hght  : Total height of table - will be calculated if not given
      total_wdth  : Total width of table
    """

    return