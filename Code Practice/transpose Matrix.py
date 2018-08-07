import numpy

m=[[1,2],[3,4],[5,6]]
for row in m:
    print row

column_major= [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
print column_major

# using zip

t_matrix=zip(*m)
print t_matrix

#using numpy
print numpy.transpose(m)

