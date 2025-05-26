class AddlArgKeys:
  """
  Specifies valid keys for optional argument dictionaries used by page
  entries.

  This ensures a consistent interface while allowing individual entries
  to support custom behavior.
  """

  CYCLING_PROMPT_IDX: str = 'cycling_prompt_idx'
  HEADER_TXT        : str = 'header_txt'
  PROMPT            : str = 'prompt'