import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""

    def __init__(self,direction,origin):
        if not isinstance(direction,Vector):
            raise TypeError(f"Direction is not of class vector but {type(direction)}")
        if not isinstance(origin,Point):
            raise TypeError(f"Origin is not of class point but {type(origin)}")
        self._direction=direction
        self._origin=origin
    
    def __repr__(self):
        return f"Ray with direction {self._direction.tolist()} and origin {self._origin.tolist()}"
    
    def __eq__(self, other):
        if isinstance(other, Ray) :
            return (np.array_equal(other._direction,self._direction) and np.array_equal(other._origin,self._origin))
        return False

class Sphere:
    """A sphere."""

    def __init__(self,center,radius):
        if not isinstance(center,Point):
            raise TypeError(f"Center is not of class point but {type(center)}")
        self._center=center
        self._radius=radius
    
    def __repr__(self):
        return f"Sphere with center {self._center.tolist()} and radius {self._radius}"

    def __eq__(self,other):
        if isinstance(other,Sphere):
            return (np.array_equal(other._center,self._center) and (other._radius==self._radius))
        return False


class Triangle:
    """A triangle."""

    ...
