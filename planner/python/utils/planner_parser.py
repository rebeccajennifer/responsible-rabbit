import argparse

from os import getcwd

#_______________________________________________________________________
class ParserStrings:

  PROGRAM_NAME: str =\
    'Planner Creator'

  PROGRAM_DESC: str =\
    'This program creates a planner to be used for goal setting '\
    ' and execution.'

  PROGRAM_EPI:  str =\
    'This is the epilog to the help menu.'

  DBL_SIDED_DESC: str =\
    'Use to modify the layouts to be printed double-sided.'

  OUT_DIR_DESC: str =\
    'Output directory.'

  PREVIEW_DESC: str = str(
    'Select to generate a preview of the planner. The preview is not '
    'intended to be printed.'
  )

  ENTRY_CFG_DESC: str = str(
    'Path to YAML file containing entry configurations. The data in '
    'this file will take precedence over other command line arguments.'
  )


#_______________________________________________________________________
class PlannerCreationParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = ParserStrings.PROGRAM_NAME
    parser.epilog = ParserStrings.PROGRAM_EPI
    parser.description = ParserStrings.PROGRAM_DESC

    parser.add_argument( '--preview'
      , '-p'
      , help=ParserStrings.PREVIEW_DESC
      , action='store_true'
      , required=False
      , default=False
    )

    parser.add_argument( '--dbl_sided'
      , '-d'
      , help=ParserStrings.DBL_SIDED_DESC
      , action='store_true'
      , required=False
      , default=False
    )

    parser.add_argument( '--out_dir'
      , '-o'
      , help=ParserStrings.OUT_DIR_DESC
      , action='store'
      , required=False
      , default='./'
    )

    parser.add_argument( '--entry_cfg'
      , '-c'
      , help=ParserStrings.ENTRY_CFG_DESC
      , action='store'
      , required=False
      , default=None
    )

    return

