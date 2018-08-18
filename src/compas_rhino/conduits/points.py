from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas
from compas_rhino.conduits import Conduit

try:
    from Rhino.Geometry import Point3d
    from Rhino.Display.PointStyle import Simple

    from System.Collections.Generic import List
    from System.Drawing.Color import FromArgb

except ImportError:
    compas.raise_if_ironpython()


__author__     = ['Tom Van Mele <vanmelet@ethz.ch>', ]
__copyright__  = 'Copyright 2014, BLOCK Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'vanmelet@ethz.ch'


__all__ = ['PointsConduit', ]


class PointsConduit(Conduit):
    """A Rhino display conduit for points.

    Parameters
    ----------
    points : list of list of float
        The coordinates of the points.
    size : list of int, optional
        The size of the points.
        Default is ``3`` for all points.
    color : list of str or 3-tuple
        The individual colors of the points.
        Default is ``(255, 0, 0)`` for all points.

    Attributes
    ----------
    size
    color
    points : list of list of float
        

    Examples
    --------

    .. code-block:: python

        from random import randint
        import time

        from compas_rhino.conduits import PointsConduit

        points = [(1.0 * randint(0, 30), 1.0 * randint(0, 30), 0.0) for _ in range(100)]

        try:
            conduit = PointsConduit(points)
            conduit.Enabled = True

            for i in range(100):
                conduit.points = [(1.0 * randint(0, 30), 1.0 * randint(0, 30), 0.0) for _ in range(100)]
                conduit.redraw()
                time.sleep(0.1)

        except Exception as e:
            print(e)

        finally:
            conduit.Enabled = False
            del conduit

    """
    def __init__(self, points, size=None, color=None, **kwargs):
        super(PointsConduit, self).__init__(**kwargs)
        self._default_size = 3
        self._default_color = FromArgb(255, 0, 0)
        self._size = None
        self._color = None
        self.points = points or []
        self.size = size
        self.color = color

    @property
    def size(self):
        """list : Individual point sizes.

        Parameters
        ----------
        size : list of int
            The size of each point.

        """
        return self._thickness

    @size.setter
    def size(self, size):
        if size:
            p = len(self.points)
            s = len(size)
            if s < p:
                size += [self._default_size for i in range(p - s)]
            elif s > p:
                size[:] = size[:p]
            self._size = size

    @property
    def color(self):
        """list : Individual point colors.

        Parameters
        ----------
        color : list of str or 3-tuple
            The color specification of each point in hex or RGB(255) format.

        """
        return self._color
    
    @color.setter
    def color(self, color):
        if color:
            color[:] = [FromArgb(* color_to_rgb(c)) for c in color]
            p = len(self.points)
            c = len(color)
            if c < f:
                color += [self._default_color for i in range(f - c)]
            elif c > f:
                color[:] = color[:f]
            self._color = color

    def DrawForeground(self, e):
        if self.color:
            draw = e.Display.DrawPoint
            if self.size:
                for xyz, size, color in zip(self.points, self.size, self.color):
                    draw(Point3d(*xyz), Simple, size, color)
            else:
                for xyz, color in zip(self.points, self.color):
                    draw(Point3d(*xyz), Simple, self._default_size, color)
        elif self.size:
            draw = e.Display.DrawPoint
            if self.color:
                for xyz, size, color in zip(self.points, self.size, self.color):
                    draw(Point3d(*xyz), Simple, size, color)
            else:
                for xyz, size in zip(self.points, self.size):
                    draw(Point3d(*xyz), Simple, size, self._default_color)
        else:
            points = List[Point3d](len(self.points))
            for xyz in self.points:
                points.Add(Point3d(*xyz))
            e.Display.DrawPoints(points, Simple, self._default_size, self._default_color)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    from random import randint
    import time

    points = [(1.0 * randint(0, 30), 1.0 * randint(0, 30), 0.0) for _ in range(100)]

    try:
        conduit = PointsConduit(points)
        conduit.Enabled = True

        for i in range(100):
            conduit.points = [(1.0 * randint(0, 30), 1.0 * randint(0, 30), 0.0) for _ in range(100)]

            conduit.redraw()

            time.sleep(0.1)

    except Exception as e:
        print(e)

    finally:
        conduit.Enabled = False
        del conduit
