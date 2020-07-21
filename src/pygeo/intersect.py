from .objects import Ray, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    a=(ray._origin-sphere._center)
    i=(ray._direction)/np.sqrt(np.dot(ray._direction,ray._direction))
    b=np.square(np.dot(i,a))
    c=np.dot(a,a)-(sphere._radius)**2
    nabla=b-c
    if nabla<0:
        return NotImplemented
    elif nabla==0:
        d=[]
        d.append(-((np.dot(i,a))))
        return np.array(d)
    else:
        d_1=-((np.dot(i,a)))+nabla
        d_2=-((np.dot(i,a)))-nabla
        d=[]
        if d_1>=0 and d_2>=0:
            d.append(d_1)
            d.append(d_2)
            return np.array(d)
        elif d_1>=0 or d_2>=0:
            if d_1<d_2:
                d.append(d_2)
                return np.array(d)
            else:
                d.append(d_1)
                return np.array(d)
        else:
            return NotImplemented


def _intersect_ray_with_triangle(ray, triangle):
    ...


