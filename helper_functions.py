from constants import DEBUG
from typing import Literal, Union
from custom_typing import _SupportsWrite

import sys


def d_print(*args, sep: Union[str, None ]= ' ', end: Union[str, None] = '\n', file: Union[_SupportsWrite[str], None] = sys.stdout, flush: Literal[False] = False) -> None:
    if not DEBUG:
        return

    # print()
    print(*args, sep= sep, end= end, file= file, flush= flush)
    # print()
