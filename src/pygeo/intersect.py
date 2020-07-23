from .objects import Point, Vector,Ray, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    a=(ray._origin._point-sphere._center._point)
    i=(ray._direction._vector)/np.sqrt(np.dot(ray._direction._vector,ray._direction._vector))
    b=np.square(np.dot(i,a))
    c=np.dot(a,a)-(sphere._radius)**2
    nabla=b-c
    point=[]
    if nabla<0:
        return NotImplemented
    elif nabla==0:
        d=-((np.dot(i,a)))
        point.append(((ray._direction._vector/np.linalg.norm(ray._direction._vector))*d)+ray._origin._point)
        p=np.array(point)
        return(np.round(p,2))
    else:
        d_1=-((np.dot(i,a)))+(nabla)**(1/2)
        d_2=-((np.dot(i,a)))-(nabla)**(1/2)
        if d_1>=0 and d_2>=0:
            point.append(((ray._direction._vector/np.linalg.norm(ray._direction._vector))*d_1)+ray._origin._point)
            point.append(((ray._direction._vector/np.linalg.norm(ray._direction._vector))*d_2)+ray._origin._point)
            p=np.array(point)
            return(np.round(p,2))
        elif d_1>=0 or d_2>=0:
            if d_1<d_2:
                point.append(((ray._direction._vector/np.linalg.norm(ray._direction._vector))*d_2)+ray._origin._point)
            else:
                point.append(((ray._direction._vector/np.linalg.norm(ray._direction._vector))*d_1)+ray._origin._point)
            p=np.array(point)
            return(np.round(p,2))
        else:
            return NotImplemented


def _intersect_ray_with_triangle(ray, triangle):
    ...
