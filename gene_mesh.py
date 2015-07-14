
f = open('zs_stru', 'w')
resolution = 20
x_size = 100
y_size = 100

x_min = -resolution*(x_size/2)
y_min = -resolution*(y_size/2)

x = x_min
for i in range(x_size):
    y = y_min
    for j in range(y_size):
        f.write(str(x)+'\t'+str(y)+'\n')
        y = y+resolution
    x=x+resolution

f.close()

