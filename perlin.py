import math
#====================================================================
#Perlin Noise Function: int x|int y
#--------------------------------------------------------------------
def noise2D(x,y):
	n = x + y * 57
	n = (n<<13)^n
	return (1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff)/1073741824.0)
#some tests for noise function:
#--------------------------------------------------------------------
#print noise2D(10,50)
#print noise2D(1,3)
#print noise2D(10,50)
#====================================================================
#Interpolation
#--------------------------------------------------------------------
def cos_interpolation(a,b,x):
	ft = x * 3.1415927
	f = (1 - math.cos(ft)) * 0.5
	return (a * (1 - f) + b * f)
#====================================================================
#Smooth Pixel Color: float x|float y
#--------------------------------------------------------------------
def smoothed_noise2D(x,y):
	corners = (noise2D(x-1,y-1) + noise2D(x+1,y-1) + noise2D(x-1,y+1) + noise2D(x+1,y+1))/16
	sides = (noise2D(x-1,y) + noise2D(x+1,y) + noise2D(x,y-1) + noise2D(x,y+1))/8
	center = noise2D(x,y)/4
	return (corners + sides + center)
#====================================================================
#Smoothed and Interpolated Noise: float x|float y
#--------------------------------------------------------------------
def compile_noise(x,y):
	int_x = int(x)
	frac_x = x - int_x
	int_y = int(y)
	frac_y = y - int_y
	v1 = smoothed_noise2D(int_x,int_y)
	v2 = smoothed_noise2D(int_x + 1,int_y)
	v3 = smoothed_noise2D(int_x,int_y + 1)
	v4 = smoothed_noise2D(int_x + 1,int_y + 1)
	i1 = cos_interpolation(v1,v2,frac_x)
	i2 = cos_interpolation(v3,v4,frac_x)
	return cos_interpolation(i1,i2,frac_y)
#====================================================================
#Perlin Noise 2D: float x|float y|float factor
#--------------------------------------------------------------------
def perlin_noise2D(x,y,factor):
	total = 0
	persistence = 0.5
	frequency = 0.25
	amplitude = 1
	num_octaves = 12
	x+= (factor)
	y+= (factor)
	for i in range(0,num_octaves):
		total += compile_noise(x * frequency,y * frequency) * amplitude
		amplitude *= persistence
		frequency *= 2
	#color matching
	#total = abs(total)
	#res = int(total * 255.0)
	return total
#print perlin_noise2D(1.4,2.5,3.4)
