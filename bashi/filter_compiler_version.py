"""Filter rules basing on host and device compiler names and versions.

All rules implemented in this filter have an identifier that begins with "v" and follows a number. 
Examples: v1, v42, v678 ...

These identifiers are used in the test names, for example, to make it clear which test is testing 
which rule.
"""

from typing import Optional, IO
from bashi.types import ParameterValueTuple


def compiler_version_filter(
    row: ParameterValueTuple,
    output: Optional[IO[str]] = None,
) -> bool:
    """Filter rules basing on host and device compiler names and versions.

    Args:
        row (ParameterValueTuple): parameter-value-tuple to verify.
        output (Optional[IO[str]], optional): Writes the reason in the io object why the parameter
            value tuple does not pass the filter. If None, no information is provided. The default
            value is None.

    Returns:
        bool: True, if parameter-value-tuple is valid.
    """
    return True
