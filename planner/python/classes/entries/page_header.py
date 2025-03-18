import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

class PageHeader(svgwrite.container.Group):
  """
  Header for page.
  """

  def __init__(self
  , text: str = Strings.DEF_PAGE_HEADER
  , wdth: int = 0
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.HEAD_2_SIZE
  , font: str = Font.FONT_FAMILY_HEADER
  , box_fill_color: str = Colors.LIGHT_GREY
  , box_brdr_color: str = Colors.BORDER_COLOR
  ):

    super().__init__()

    self.text_ = text
    self.font_color_: str = font_color
    self.font_size_: int = font_size
    self.font_: str = font
    self.box_fill_color_: str = box_fill_color
    self.box_brdr_color_: str = box_brdr_color

    self.wdth_ = wdth
    self.hght_ = self.font_size_ + 2 * Font.TEXT_PADDING

    self.add(self.create_header())

    return

  def create_header(self) -> svgwrite.container.Group:
    """
    Creates page header.
    """

    group: svgwrite.container.Group = svgwrite.container.Group()

    header_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect\
      ( size=(self.wdth_, self.hght_)
      , insert=(0,0)
      , stroke=self.box_brdr_color_
      , fill=self.box_fill_color_
      )

    text_insert_x: int = Font.TEXT_PADDING
    text_insert_y: int = Font.TEXT_PADDING + self.font_size_

    header_txt: svgwrite.text.Text =\
      svgwrite.text.Text\
      ( text=self.text_
      , insert=(text_insert_x, text_insert_y)
      , text_anchor='start'
      , alignment_baseline='text-after-edge'
      , fill=self.font_color_
      , font_size=self.font_size_
      , font_family=self.font_
      )

    group.add(header_box)
    group.add(header_txt)

    return group

class DayHeader(PageHeader):
  """
  Page header for daily entry
  """



