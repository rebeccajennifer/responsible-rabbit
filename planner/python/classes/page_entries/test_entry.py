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
#   Entry for testing. Will not be used in final product.
#_______________________________________________________________________

import svgwrite.container

from copy import deepcopy

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.std_styles import StdTextBoxStyles
from classes.style.style import PlannerFontStyle as Font

from classes.elements.base_element import VerticalStack
from classes.elements.base_element import HorizontalStack
from classes.elements.row_group import TextRowGroup
from classes.elements.table import DualLineTable
from classes.elements.table import SingleLineTable
from classes.elements.table import ColumnTable

from classes.page_layouts.half_page_layout import HalfPageLayout


#_______________________________________________________________________
class TestEntry(HalfPageLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , addl_args=addl_args
    )

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Parameters:
      None

    Side Effects:
      Populates self.entries_ class variable.

    Returns:
      None
    """
    super().create_content()

    style  = deepcopy(StdTextBoxStyles.LTE_BACK_HEADER_FONT)
    style.line_spc_=1

    fill_hght: int = self.calc_remaining_hght_per_element(3)
    fill_hght: int = self.calc_remaining_hght_per_element(2)
    fill_hght: int = self.calc_remaining_hght_per_element(1)

    test0=ColumnTable\
          ( total_wdth=self.content_wdth_
          #, total_hght=fill_hght
          , total_hght=100
          #, total_hght=self.content_hght_
          , header_txt_lst=['','','']
          , text_style=style
          , row_count=2
          , show_outline=True
          )

    test1= deepcopy(test0)
    test2= deepcopy(test0)

    obj_list=[test0, test1, test2]
    obj_list=[test0]
    obj_list=[test0, test1]

    #x: VerticalStack = VerticalStack( add_top_pad=False, obj_list=obj_list)

    #fill_hght: int = self.calc_remaining_hght_per_element(1)
    #test1=ColumnTable\
    #      ( total_wdth=self.content_wdth_
    #      , total_hght=fill_hght
    #      , header_txt_lst=Strings.WEEK_FULFILLMENT_AREAS_0
    #      , text_style=style
    #      , row_count=2
    #      , show_outline=True
    #      )



    #self.entries_.append(x)
    self.entries_ = obj_list
    #self.entries_.append(test0)
    #self.entries_.append(test1)
    #self.entries_.append(test2)

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """

    return super().create_page_header\
      (header_txt=Strings.DEF_PAGE_HEADER_TXT)