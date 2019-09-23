# pyLearning
Some scripts during learning python. 

## arc.py
get the points of arc by three key points.
### get_arc_points
`get_arc_points(center, p1, p2,step=0.01)`
- **center**: center point of the arc.
- **p1**: one end point of the arc.
- **p2**: the other end point of the arc.
- **step**: the step of angle(radian).
#### Example
```python
from arc import get_arc_points
import matplotlib.pyplot as plt
# key points of arc.
P1=[0,1,1]
P2=[1,0,1]
C=[0,0,0]
# get points of arc
arc=get_arc_points(C,P1,P2,0.01)
# show the result
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(arc[0,:],arc[1,:],arc[2,:])
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.scatter3D(P1[0],P1[1],P1[2])
ax.scatter3D(P2[0], P2[1], P2[2])
ax.scatter3D(C[0], C[1], C[2])
plt.show()
```

### Others
Email: cug_xia@gmail.com

Blog: https://blog.cuger.cn
