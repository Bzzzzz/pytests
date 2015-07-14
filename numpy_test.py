import numpy as np

f = open('zs_out_gs','r')

lines = f.readlines()
array =np.zeros(10000)

i=0
for line in lines:
    z = line.split()[2]
    z = eval(z)
    array[i]=z
    i=i+1

print array
re_array=array.reshape(100,100)
print re_array
x_camera,y_camera=(420, -560)
resolution = 20
x_min = -1000
y_min = -1000
z_camera = re_array[(x_camera-x_min)/resolution][(y_camera-y_min)/resolution]
print z_camera

