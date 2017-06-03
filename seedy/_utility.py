"""Various internal-only utility functions for seedy."""

from __future__ import division
from __future__ import print_function

import platform

# The currently-running system.
_system = platform.system()

def format_human_readable(size, precision=1):
    """Format a byte count as a human-readable string.

    The conversion tries to respect the conventions of the running
    platform. For example, OS X (Darwin) systems define a KB as 1000B,
    while pretty much everyone else defines it as 1024B.

    :param: size a number specifying some number of bytes
    :type: size non-negative int, float, or convertible equivalent
    :return: a formatted human-readable string representing the input
             size
    """

    # Set definition of suffixes, depending on the system.
    if _system == "Darwin":
        dividand = 1000.0
    else:
        dividand = 1024.0

    # Check sign of input.
    if size < 0:
        raise ValueError("Negative size (" + str(size) + ").")

    # Progressively step up through the suffixes.
    size = float(size)
    for suffix in ['B ','KB','MB','GB','TB','PB','EB','ZB']:
        if size < dividand:
            format_str = '\%5.%sf\%s' % str(precision)
            return format_str % (size, suffix)
        size /= dividand

    # Default to yottabytes. (What's it like in the future?)
    format_str = '\%.%sf\%s' % str(precision)
    return "%.1f%s" % (size, 'YB')
