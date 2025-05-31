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
#
#   Defines standardized string keys for optional argument dictionaries
#   used across planner page entries. These keys ensure consistency
#   while enabling flexible, entry-specific behavior.
#_______________________________________________________________________

class AddlArgKeys:
  """
  Specifies valid keys for optional argument dictionaries used by page
  entries.

  This ensures a consistent interface while allowing individual entries
  to support custom behavior.
  """

  CYCLING_PROMPT_IDX: str = 'cycling_prompt_idx'
  HEADER_TXT        : str = 'header_txt'
  PROMPT_TXT        : str = 'prompt'

  ENTRY_TYPE  : str = 'entry_type'
  ENTRY_ARGS  : str = 'entry_args'
