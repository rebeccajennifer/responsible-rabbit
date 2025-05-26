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
  FILE_PATH         : str = 'file_path'

  FUTURE_5YR  : str = 'future_5yr'
  FUTURE_12W  : str = 'future_12w'
  FUTURE_1YR  : str = 'future_1yr'
  FUTURE_BAD  : str = 'future_bad'

  ENTRY_TYPE  : str = 'entry_type'
  ENTRY_ARGS  : str = 'entry_args'