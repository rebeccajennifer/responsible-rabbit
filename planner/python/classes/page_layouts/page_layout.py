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
#   Half-letter sheet layout
#_______________________________________________________________________

import cairosvg
import svgwrite

from os.path import join
from typing import Tuple

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.page_layouts.half_page_layout import HalfPageLayout
from flux_bunny_utils.file_utils import FileUtils
from utils.utils import PlannerUtils as Utils


#_______________________________________________________________________
class PageLayout(svgwrite.Drawing):
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  PDF_SUB_DIR: str = 'pdf'
  SVG_SUB_DIR: str = 'svg'

  #_____________________________________________________________________
  def __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_name_no_ext: str = Strings.DEF_LAYOUT_PATH
  , out_dir: str = '.'
  , entry_0_type: type = None
  , entry_0_args: dict = {}
  , entry_1_type: type = None
  , entry_1_args: dict = {}
  , rgt_bndr_mrgn: bool = False
  ):
    """
    Parameters
      is_portrait       : Is full page portrait orientation.
      is_dbl_sided      : Is page to be printed double-sided
      file_path         : This should go away
      file_name_no_ext  : Name of file without extension
      out_dir           : Path to output directory
      entry_0_type      : Type of entry on left or top of page
                          e.g. day_entry, month_entry
      entry_0_args      : Arguments for left or top entry
      entry_1_type      : Type of entry on right or bottom of page
                          e.g. day_entry, month_entry
      entry_1_args      : Arguments for right or bottom entry
      rgt_bndr_mrgn     :  Use the binder margin on the right side
    """

    self.is_portrait_   : bool  = is_portrait
    self.is_dbl_sided_  : bool  = is_dbl_sided
    self.rgt_bndr_mrgn_ : bool  = rgt_bndr_mrgn
    self.file_name_no_ext_ : str = file_name_no_ext

    #___________________________________________________________________
    # Verify directory
    FileUtils.verify_dir(out_dir)
    self.out_dir_       : str   = out_dir

    self.pdf_dir_ : str = join(out_dir, self.PDF_SUB_DIR)
    svg_dir       : str = join(out_dir, self.SVG_SUB_DIR)

    FileUtils.verify_dir(svg_dir)
    FileUtils.verify_dir(self.pdf_dir_)

    self.svg_file_path_: str =\
      join(svg_dir, file_name_no_ext + '.svg')

    #___________________________________________________________________
    if (not entry_0_type):
      self.entry_0_type_: type = HalfPageLayout
    else:
      self.entry_0_type_: type = entry_0_type

    if (not entry_1_type):
      self.entry_1_type_: type = HalfPageLayout
    else:
      self.entry_1_type_: type = entry_1_type

    self.entry_0_args_ = entry_0_args
    self.entry_1_args_ = entry_1_args

    self.total_hght_ = Dims.LETTER_SIZE_WIDTH_PX
    self.total_wdth_ = Dims.LETTER_SIZE_LNGTH_PX

    #___________________________________________________________________
    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH_IN)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH_IN)

    super().__init__\
      ( self.svg_file_path_
      , profile='tiny'
      , size=(wdth, hght)
      )
    #___________________________________________________________________

    self.content_wdth_, self.content_hght_ =\
       Dims.calc_border_size(self.is_portrait_)

    # Content insertion points for top left
    self.calc_border_insert_pts()
    self.create_content()
    self.add_content()

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Creates page borders, page header, content.

    Parameters
      None

    Returns
      None
    """

    EntryType0: type = self.entry_0_type_
    EntryType1: type = self.entry_1_type_

    self.content_0_ =\
      EntryType0\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      , addl_args=self.entry_0_args_
      )

    self.content_1_ =\
      EntryType1\
      ( total_wdth=self.content_wdth_
      , total_hght=self.content_hght_
      , addl_args=self.entry_1_args_
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    """
    Adds content as class variables to page.

    Parameters
      None

    Returns
      None
    """

    x: int = self.insert_pt_border_0_[0]
    y: int = self.insert_pt_border_0_[1]
    self.content_0_['transform'] = f'translate({x}, {y})'

    x: int = self.insert_pt_border_1_[0]
    y: int = self.insert_pt_border_1_[1]
    self.content_1_['transform'] = f'translate({x}, {y})'

    self.add(self.content_0_)
    self.add(self.content_1_)

    return

  #_____________________________________________________________________
  def calc_border_insert_pts(self) -> None:
    """
    Determines top left insertion points for content boxes and borders.

    Side Effects
      Adds class variables for insertion points.
    """

    content_wdth: int = self.content_wdth_
    content_hght: int = self.content_hght_

    if (self.is_portrait_):
      insert_pos00 = Dims.STD_MARGIN_PX
      insert_pos01 = Dims.BND_MARGIN_PX

      insert_pos10 = Dims.STD_MARGIN_PX
      insert_pos11 = content_hght\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos01 = Dims.STD_MARGIN_PX

    else:
      insert_pos00 = Dims.BND_MARGIN_PX
      insert_pos01 = Dims.STD_MARGIN_PX
      insert_pos11 = Dims.STD_MARGIN_PX

      insert_pos10 = content_wdth\
        + Dims.STD_MARGIN_PX\
        + 2 * Dims.BND_MARGIN_PX

      if (self.is_dbl_sided_):
        insert_pos00 = Dims.STD_MARGIN_PX

    # Modify insertion point of right content to allow for binder
    # margin on right side
    if (self.rgt_bndr_mrgn_):
      insert_pos10 = content_wdth\
        + 2 * Dims.STD_MARGIN_PX\
        + Dims.BND_MARGIN_PX

    insert_pos0: Tuple = (insert_pos00, insert_pos01)
    insert_pos1: Tuple = (insert_pos10, insert_pos11)

    self.insert_pt_border_0_: int =  insert_pos0
    self.insert_pt_border_1_: int =  insert_pos1

    return


  #_____________________________________________________________________
  def save_pdf(self):
    """
    Saves layout as pdf.

    Parameters
      out_dir: Path to output directory

    Side Effects
      Saves layout to pdf in output directory.

    Returns
      None
    """


    self.save()
    cairosvg.svg2pdf\
    ( url=self.svg_file_path_
    , write_to=join\
      ( self.pdf_dir_
      , f'{self.file_name_no_ext_}.pdf'
      )
    )