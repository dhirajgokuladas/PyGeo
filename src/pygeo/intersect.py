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
        # return False
    elif nabla==0:
        d=-((np.dot(i,a)))
        return d
        # return True
    else:
        d_1=-((np.dot(i,a)))+nabla
        d_2=-((np.dot(i,a)))-nabla
        if d_1>=0 and d_2>=0:
            # if d_1<d_2:
            #     return d_1
            # else:
            #     return d_2
            # return True
            return d_1, d_2
        elif d_1>=0 or d_2>=0:
            if d_1<d_2:
                return d_2
            else:
                 return d_1
            # return True
        else:
            return d_1
            # return False


def _intersect_ray_with_triangle(ray, triangle):
    ...


ray=Ray((1.2,-1.2,0),(0,1.2,0))
sphere=Sphere((0,0,0),1)
d_1,d_2=_intersect_ray_with_sphere(ray,sphere)
point_1=((ray._direction/np.linalg.norm(ray._direction))*d_1)+ray._origin
point_2=((ray._direction/np.linalg.norm(ray._direction))*d_2)+ray._origin
print(point_1)
print(point_2)

ray=Ray((2,0,0),(0,1,0))
sphere=Sphere((0,0,0),1)
d=_intersect_ray_with_sphere(ray,sphere)
point=((ray._direction/np.linalg.norm(ray._direction))*d)+ray._origin
print(point)