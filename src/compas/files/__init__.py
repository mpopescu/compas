"""
********************************************************************************
files
********************************************************************************

.. currentmodule:: compas.files


Classes
=======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    OBJ
    OBJReader
    OBJParser
    PLY
    PLYReader
    PLYParser
    STL
    STLReader
    STLParser
    URDF
    URDFParser
    XML
    XMLReader

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .amf import *  # noqa: F401 F403
from .dxf import *  # noqa: F401 F403
from .las import *  # noqa: F401 F403
from .obj import *  # noqa: F401 F403
from .off import *  # noqa: F401 F403
from .ply import *  # noqa: F401 F403
from .stl import *  # noqa: F401 F403
from .urdf import *  # noqa: F401 F403
from .xml_ import *  # noqa: F401 F403

__all__ = [name for name in dir() if not name.startswith('_')]
