import perlin
import random
#print perlin.perlin_noise2D(1.4,2.3,5.6)

#list of lists like in classic array:
#full list will look like this:
#[[this is list_row_1],
# [this is list row_2]]
#list = [['a','b','c','d','e'],['h','i','j','k','l']]  
#print list[0][0] #a
#print list[0][4] #e

height_map = []
heights = []
width = 2
length = 7
print "width = ",width,"length = ",length
fac = random.randint(0,1000)
print "fac: ",fac
for i in range(0,width):
	for j in range(0,length):
		heights.append(perlin.perlin_noise2D(i,j,fac))
	height_map.append(heights)
	heights = []
#height_map for testing triangle_map
#height_map = [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]]
print "this is rect height map:"
print height_map
print "=============================================================="
#====================================================================
#Triangle Map
#list of triangles:
#[[coord of tr1],[coord of tr2],...]
#each triangle list contains 3 lists[vertexes] of coordinates(x,y,z):
#[[tr1: [x1,y1,z1],[x2,y2,z2],[x3,y3,z3]],[tr2],...]
# vertex numbers of top_right and bottom_left triangle:
# 1+------+3
#  |      |   
#  |      |     
#  +------+
# 3        2
#--------------------------------------------------------------------
triangle_map = []
for i in range(0,len(height_map)):
	for j in range(0,len(height_map[0])):
		#bottom triangle:
		triangle = []
		vertex_1 = [i,height_map[i][j],j]
		#last in a column:
		if (i != len(height_map)-1):
			#not last in a col:
			#last in a row:
			if (j == len(height_map[0])-1):
				vertex_2 = [i+1,height_map[i+1][j],j+1]
			else: #not last in row:
				vertex_2 = [i+1,height_map[i+1][j+1],j+1]
			vertex_3 = [i+1,height_map[i+1][j],j]
		else:
			if (j == len(height_map[0])-1):
				vertex_2 = [i+1,height_map[i][j],j+1]
			else:
				vertex_2 = [i+1,height_map[i][j+1],j+1]
			vertex_3 = [i+1,height_map[i][j],j]
		triangle.append(vertex_1)
		triangle.append(vertex_2)
		triangle.append(vertex_3)
		triangle_map.append(triangle)
		#top triangle:
		triangle = []
		triangle.append(vertex_1)
		#last in a column:
		if (i != len(height_map)-1):
			#not last in a col:
			#last in a row:
			if (j == len(height_map[0])-1):
				vertex_2 = [i+1,height_map[i+1][j],j+1]
				vertex_3 = [i,height_map[i][j],j+1]
			else: #not last in row:
				vertex_2 = [i+1,height_map[i+1][j+1],j+1]
				vertex_3 = [i,height_map[i][j+1],j+1]
		else:
			if (j == len(height_map[0])-1):
				vertex_2 = [i+1,height_map[i][j],j+1]
				vertex_3 = [i,height_map[i][j],j+1]
			else:
				vertex_2 = [i+1,height_map[i][j+1],j+1]
				vertex_3 = [i,height_map[i][j+1],j+1]
		triangle.append(vertex_2)
		triangle.append(vertex_3)
		triangle_map.append(triangle)
print "triangle map:"
print triangle_map
print "=============================================================="
print "triangles in total = ",len(triangle_map)
