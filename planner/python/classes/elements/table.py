import svgwrite

from classes.elements.rows import DualLineRowGroup
from classes.elements.rows import RowGroup
from classes.elements.rows import LineRowGroup
from classes.elements.rows import TextRowGroup
from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle
from classes.elements.base_element import VerticalStack

from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class WriteTable(svgwrite.container.Group):
  """
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

