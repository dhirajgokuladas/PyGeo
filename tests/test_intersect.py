from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle
import numpy as np

# intersect


# _intersect_ray_with_sphere

def test__intersect_given_sphere_ray__not_intersected__return_NotImplimented():
    assert (_intersect_ray_with_sphere(Ray((2,0,0),(0,2,0)),Sphere((0,0,0),1))) is NotImplemented

def test__intersect_given_sphere_ray__intersected_one_point_d_grater_than_0():
    assert (_intersect_ray_with_sphere(Ray(((2**(1/2)),-(2**(1/2)),0),(0,(2**(1/2)),0)),Sphere((0,0,0),1))>=np.array([0]))

def test__intersect_given_sphere_ray__intersected_two_point_d_grater_then_0():
    assert (_intersect_ray_with_sphere(Ray((1.2,-1.2,0),(0,1.2,0)),Sphere((0,0,0),1)).all()>=np.array([0,0]).all())

def test__intersect_given_sphere_ray__not_intersected_two_point_d_less_than_0__return_NotImplimented():
    assert (_intersect_ray_with_sphere(Ray((1,1,0),(1,1,0)),Sphere((0,0,0),1))) is NotImplemented

# _intersect_ray_with_triangle
