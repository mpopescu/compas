Geometry
********

* :mod:`compas.geometry`

The geometry package provides primitives (and shapes), transformations, and algorithms (for lack of a better word).
The primitives and transformations provide an object-oriented interface to the geometry processing algorithms.


Basic examples
==============

.. code-block:: python

    >>> x = [1.0, 0.0, 0.0]
    >>> y = [0.0, 1.0, 0.0]
    >>> add_vectors(x, y)
    [1.0, 1.0, 0.0]

.. code-block:: python

    >>> x = Vector(1.0, 0.0, 0.0)
    >>> y = Vector(0.0, 1.0, 0.0)
    >>> add_vectors(x, y)
    [1.0, 1.0, 0.0]

.. code-block:: python

    >>> x = Vector(1.0, 0.0, 0.0)
    >>> y = Vector(0.0, 1.0, 0.0)
    >>> x + y
    Vector(1.000, 1.000, 0.000)

.. code-block:: python

    >>> x = [1.0, 0.0, 0.0]
    >>> y = [0.0, 1.0, 0.0]
    >>> cross_vectors(x, y)
    [0.0, 0.0, 1.0]

.. code-block:: python

    >>> x = Vector(1.0, 0.0, 0.0)
    >>> y = Vector(0.0, 1.0, 0.0)
    >>> cross_vectors(x, y)
    [0.0, 0.0, 1.0]

.. code-block:: python

    >>> x = Vector(1.0, 0.0, 0.0)
    >>> y = Vector(0.0, 1.0, 0.0)
    >>> x.cross(y)
    Vector(0.000, 0.000, 1.000]

.. code-block:: python

    >>> points = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]]
    >>> area_polygon(points) == area_polygon(Polygon(points))
    True

.. code-block:: python

    >>> points = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]]
    >>> area_polygon(points) == Polygon(points).area()
    True

.. code-block:: python

    >>> points = pointcloud(50, (0, 50), (0, 10), (0, 20))
    >>> X = matrix_from_axis_and_angle([0.0, 0.0, 1.0], radians(30))
    >>> transform_points(points, X)


.. intersections

.. shape transformations

.. collections

.. numpy

