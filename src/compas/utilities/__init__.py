"""
********************************************************************************
utilities
********************************************************************************

.. currentmodule:: compas.utilities


async
=====

.. autosummary::
    :toctree: generated/
    :nosignatures:

    await_callback


colors
======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    i_to_rgb
    i_to_red
    i_to_green
    i_to_blue
    i_to_white
    i_to_black
    rgb_to_hex
    color_to_colordict
    color_to_rgb


datetime
========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    timestamp
    now


itertools
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    take
    tabulate
    tail
    consume
    nth
    all_equal
    quantify
    padnone
    ncycles
    dotproduct
    flatten
    repeatfunc
    pairwise
    window
    roundrobin
    powerset
    unique_justseen
    iter_except
    first_true
    random_permutation
    random_combination
    random_combination_with_replacement


maps
====

.. autosummary::
    :toctree: generated/
    :nosignatures:

    geometric_key
    reverse_geometric_key
    geometric_key2
    normalize_values


profiling
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    print_profile


"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .animation import *  # noqa: F401 F403
from .async_ import *  # noqa: F401 F403
from .coercing import *  # noqa: F401 F403
from .colors import *  # noqa: F401 F403
from .datetime_ import *  # noqa: F401 F403
from .decorators import *  # noqa: F401 F403
# from .descriptors import *  # noqa: F401 F403
from .encoders import *  # noqa: F401 F403
from .functions import *  # noqa: F401 F403
from .itertools_ import *  # noqa: F401 F403
from .maps import *  # noqa: F401 F403
from .profiling import *  # noqa: F401 F403
from .remote import *  # noqa: F401 F403
from .statistics import *  # noqa: F401 F403
from .xfunc import *  # noqa: F401 F403


__all__ = [name for name in dir() if not name.startswith('_')]
