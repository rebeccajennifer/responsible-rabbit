import svgwrite

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from classes.elements.base_element import BaseElement
from classes.elements.rows import RowGroup
from classes.elements.rows import LineRowGroup
from classes.elements.rows import LineRowGroupStyle
from classes.elements.rows import TextRowGroup
from classes.style.table_style import TextBoxStyle


#_______________________________________________________________________
class SimpleTable(svgwrite.container.Group):
  """
  """

  def __init__(self
  , header_txt: str = ''
  , style: TextBoxStyle = TextBoxStyle()
  ):
    """
    Parameters:
      header_txt  : Text contained in header
      font_family : Font of header text
      font_size   : Size of header text
      total_hght  : Total height of table - will be calculated if not given
      total_wdth  : Total width of table
    """

    super().__init__()

    self.header_ =\
      TextRowGroup\
      ( total_wdth=style.total_wdth_
      , total_hght=style.total_hght_
      , show_outline=style.show_outline_
      , outline_color= Colors.BORDER_COLOR
      , backgnd_color=Colors.FLUX_RED
      , text=header_txt
      , font_size= Font.NORMAL_SIZE
      , font_family= Font.FONT_FAMILY_NORMAL
      , font_color= Colors.NORMAL_TXT
      , line_spc=1
      ).text_row_group_

    self.total_hght_ = self.header_.total_hght_
    self.add(self.header_)

    return