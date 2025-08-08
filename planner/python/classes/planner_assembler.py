from os.path import join

from utils.utils import PlannerUtils as Utils
from classes.constants.addl_arg_keys import AddlArgKeys as Keys
from classes.constants.page_order import DblSidePages
from classes.constants.page_order import OneSidePages
from classes.constants.page_order import PreviewPages
from classes.constants.page_order import OptionlPages
from classes.page_layouts.page_layout import PageLayout


#_______________________________________________________________________
class PdfPrefix:
  """
  File prefixes for grouped PDFs.
  """

  INTR: str = 'main-intr'
  WEEK: str = 'main-week'

  XTRA: str = 'xtra-xtra'
  DAYS: str = 'xtra-days'
  NITE: str = 'xtra-nite'
  ACE_: str = 'xtra-ace_'


#_______________________________________________________________________
class PageGroup():
  """
  Represents a pdf page group.

  Attributes:
    group_pdf_name: Name of combined pdf.

    pages:  List of page information containing individual
            file name - used in pdf and svg naming,
            entry type and entry arguments.

            Takes the form:

            [ { 'file_name': 'group_0_pg_0'
              , 'LeftEntry': {'entry_type': EntryType, 'entry_args: {}'}
              , 'RghtEntry': {'entry_type': EntryType, 'entry_args: {}'}
              }
            , { 'file_name': 'group_0_pg_1'
              , 'LeftEntry': {'entry_type': EntryType, 'entry_args: {}'}
              , 'RghtEntry': {'entry_type': EntryType, 'entry_args: {}'}
              }
            ]
  """

  group_counter = Utils.inc()

  #_____________________________________________________________________
  def __init__( self, group_name: str, layouts: list):
    """
    Parameters:
      group_name: Used in naming individual and grouped pdf.

      layouts   : List of layouts in the following form:

        [ { LeftEntry: {'entry_type': EntryType, 'entry_args: {}'}
          , RghtEntry: {'entry_type': EntryType, 'entry_args: {}'}
          }
        , { LeftEntry: {'entry_type': EntryType, 'entry_args: {}'}
          , RghtEntry: {'entry_type': EntryType, 'entry_args: {}'}
          }
        ]
    """

    self.group_pdf_name =\
      f'__{str(next(self.group_counter))}__{group_name}.pdf'

    self.pages      : list = layouts
    self.file_names : list = []

    # Used for page naming
    counter = Utils.inc()

    # Add key for filename to layouts
    for pg in (self.pages):
      fname: str = f'{group_name}{next(counter):02}'
      pg[Keys.NAME] = fname
      self.file_names.append(fname)

    return


#_______________________________________________________________________
class PlannerAssembler:
  """
  Functions used to assemble planner.
  """

  def __init__(self
  , is_portrait: bool = True
  , is_dbl_sided: bool = False
  , is_preview: bool = False
  , out_dir: str = '.'
  ):
    """
    Parameters:
      is_portrait  : True - Full page to be printed in portrait
                     orientation.

      is_dbl_sided : True - Pages are to be printed double-sided

      out_dir      : Output directory for files
    """

    self.make_page_groups\
    ( is_dbl_sided=is_dbl_sided
    , is_preview=is_preview)

    #_____________________________________________________________________
    # Iterate through list containing layout arguments and create
    # for each layout
    #_____________________________________________________________________
    for group in self.page_groups:

      for pg in group.pages:

        layout =\
          PageLayout\
          ( is_portrait=is_portrait
          , is_dbl_sided=is_dbl_sided
          , file_name_no_ext=pg[Keys.NAME]
          , out_dir=out_dir
          , entry_0_type=pg[Keys.LEFT][Keys.ENTRY_TYPE]
          , entry_0_args=pg[Keys.LEFT][Keys.ENTRY_ARGS]
          , entry_1_type=pg[Keys.RGHT][Keys.ENTRY_TYPE]
          , entry_1_args=pg[Keys.RGHT][Keys.ENTRY_ARGS]
          )
        layout.save_pdf()

      self.group_pdfs(group, out_dir)

  #_______________________________________________________________________
  def group_pdfs(self
  , page_group: PageGroup
  , out_dir: str = '.'
  ) -> None:
    """
    Combines pdfs in groups.

    Parameters:
      page_group: List of pages.
      out_dir   : Output directory

    Side Effects:
      Creates combined pdfs. Removes original pdfs if that section is

    Returns:
      None
    """

    pdf_out_dir: str = join(out_dir, 'pdf')

    pdf_paths: list =\
      [join(pdf_out_dir, n + '.pdf') for n in page_group.file_names]

    combo_pdf_path: str = join(pdf_out_dir, page_group.group_pdf_name)
    Utils.combine_pdfs(pdf_paths, combo_pdf_path)

    return

  #_____________________________________________________________________
  def make_page_groups\
  ( self
  , is_dbl_sided: bool = False
  , is_preview: bool = False
  ) -> None:
    """
    Sets page groups according to if pages are to be printed double-
    sided or if they are for the preview.

    """

    self.page_groups: list = []

    if(is_preview):
      PageType = PreviewPages
    elif (is_dbl_sided):
      PageType = DblSidePages
    else:
      PageType = OneSidePages

    group0: PageGroup =\
      PageGroup\
      ( group_name=PdfPrefix.INTR
      , layouts=PageType.INTR_LAYOUTS
      )

    group1: PageGroup =\
      PageGroup\
      ( group_name=PdfPrefix.WEEK
      , layouts=PageType.WEEK_LAYOUTS
      )

    group2: PageGroup =\
      PageGroup\
      ( group_name=PdfPrefix.XTRA
      , layouts=OptionlPages.XTRA_LAYOUTS
      )

    self.page_groups: list =\
      [ group0
      , group1
      , group2
      ]

    return

