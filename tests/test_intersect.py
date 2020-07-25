from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Point,Vector, Ray, Sphere, Triangle
import numpy as np

# intersect


# _intersect_ray_with_sphere

def test__intersect_given_sphere_ray__not_intersected__return_NotImplimented():
    assert (_intersect_ray_with_sphere(Ray(direction=Vector((2,0,0)),origin=Point((0,2,0))),Sphere(center=Point((0,0,0)),radius=1))) is NotImplemented
def test__intersect_given_sphere_ray__intersected_one_point_d_grater_than_0():
    assert (_intersect_ray_with_sphere(Ray(direction=Vector((2,0,0)),origin=Point((0,1,0))),Sphere(center=Point((0,0,0)),radius=1))==np.array([[0.,1.,0.]])).all()
def test__intersect_given_sphere_ray__intersected_two_point_d_grater_then_0():
    assert (_intersect_ray_with_sphere(Ray(direction=Vector((1,-1,0)),origin=Point((0,1,0))),Sphere(center=Point((0,0,0)),radius=1))==np.array([[1., 0., 0.],[0., 1., 0.]])).all()
def test__intersect_given_sphere_ray__not_intersected_two_point_d_less_than_0__return_NotImplimented():
    assert (_intersect_ray_with_sphere(Ray(direction=Vector((1,1,0)),origin=Point((1,1,0))),Sphere(center=Point((0,0,0)),radius=1))) is NotImplemented

# _intersect_ray_with_triangle
