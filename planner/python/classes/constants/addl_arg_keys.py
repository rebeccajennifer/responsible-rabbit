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

  VISION_FUTURE_5YR : str = 'future_5yr'
  VISION_FUTURE_12W : str = 'future_12w'
  VISION_FUTURE_1YR : str = 'future_1yr'
  VISION_FUTURE_BAD : str = 'future_bad'