"""
********************************************************************************
numerical
********************************************************************************

.. currentmodule:: compas.numerical

.. note::

    For many functions, multiple implementations are available using various backends.
    If no backend is specified, the function is assumed to be implemented in pure Python.
    The suffix `_numpy` indicates that the function uses Numpy and/or Scipy.
    Some of the other possibilities are `_alglib`, `_cpp`, `_matlab`, `_sympy`.

    On most platforms, all variants are directly available.
    In Rhino, only the pure Python and the `_alglib` variants can be used directly.
    All others have to be accessed through an `XFunc` or an `RPC` service.


Solvers
=======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    descent_numpy
    devo_numpy
    dr
    dr_numpy
    drx_numpy
    fd_numpy
    ga
    moga
    pca_numpy
    topop_numpy


Linalg
======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    nullspace
    rank
    dof
    pivots
    nonpivots
    rref
    rref_sympy
    rref_matlab
    chofactor
    lufactorized
    uvw_lengths
    normrow
    normalizerow
    rot90
    solve_with_known
    spsolve_with_known


Matrices
========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    adjacency_matrix
    degree_matrix
    connectivity_matrix
    laplacian_matrix
    face_matrix
    mass_matrix
    equilibrium_matrix


Operators
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    grad


Utilities
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    float_formatter
    set_array_print_precision
    unset_array_print_precision


"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas

if not compas.IPY:
    from .linalg import *  # noqa: F401 F403
    from .matrices import *  # noqa: F401 F403
    from .operators import *  # noqa: F401 F403
    from .utilities import *  # noqa: F401 F403

from .topop import *  # noqa: F401 F403
from .pca import *  # noqa: F401 F403
from .ga import *  # noqa: F401 F403
from .fd import *  # noqa: F401 F403
from .drx import *  # noqa: F401 F403
from .dr import *  # noqa: F401 F403
from .devo import *  # noqa: F401 F403
from .descent import *  # noqa: F401 F403


__all__ = [name for name in dir() if not name.startswith('_')]
