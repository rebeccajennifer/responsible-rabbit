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

    parser.add_argument( '--dbl_sided'
      , help=ParserStrings.DBL_SIDED_DESC
      , action='store_true'
      , required=False
      , default=False
    )

    parser.add_argument( '--out_dir'
      , help='TODO'
      , action='store'
      , required=False
      , default='./'
    )


    return

