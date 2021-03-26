import numpy as np
import math
a=np.array([1,2,3])
print(a.ndim)
b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
c=np.zeros((2,3))
d=np.ones((2,3))
e=np.random.rand(2,3)
f=np.arange(10,50,2)
g=np.linspace(10,50,40+1)#create array of 40 numbers excatly withot truncation of fraction due to difference of bases
h=np.array([[10,20,30,40],[3,5,4,3]])
i=np.array([[1,2,3,4],[3,4,5,6]])
print(h+i)# arthmetic operations on matrix with same dimebsion are allowed
print(h*i)
fahrenhiet=np.array([0,-10,-5,-15,0])
celsius=(fahrenhiet-31)*(5/9)#conversion using multiple arthemitic operations
print(celsius>20)#check if any celsius value is larger than 20
#same to find even numbers etc..
#matrix product use @ not *
d=np.array([1,3,3,4])
print(h@d)
#to find type of array values
print(d.dtype)
# type of resulting array under operation is upcasted i.e int32*float32 will be more likely float32
# we can use sum, min,max,mean for our matrix/arrays
print((h@d).mean())
#we can use reshape for arrays
print(np.arange(1,21).reshape(4,5))
#%%
#lets use images library in combination with numpy
from PIL import Image
from IPython.display import display
disp=Image.open('LenovoWallPaper.jpg')
display(disp)#image not displayed :(
z=np.array(disp)
print(z)
#%% # dimension are the horizontal px and vertical px multiplied by 3(red,green,blue)
# values are 16**2 from 0 to 16**2-1 (hexa) shades of those color each when displayed they are reshaped by dimensions
#for every px there 2**24 values
#0 for each color is total black while 255 is total white
#so that qulifies us to invert colors of image
mask=np.full(z.shape,255)#full of 255 of the same shape as z
m=mask-z#substract
m=m.astype(np.uint8)#convert to supported image values
display(Image.fromarray(m))#print inverted image in jupyter
#reshape image will create modified image 
#resha=np.reshape(m,(9,16))
#%%
#Indexing
#for 1D array we treat it like a list
print(d[0])
#for multidimensional array we use integer array indexing
print(h[0][0])# 1st value is row 2nd is column 
#add elements from array to a new array
l=np.array(h[0][0],h[1][1])
#%%
#Bolean Index to chose elements
print(h[h>4])
#Slicing Matrix
b=np.array([1,2,3,4,5])
print(b[:3])
print(b[2:4])
#for multidimensional array
o=np.random.rand(3,3)
print(o[0:1])#get first and second row and all columns
print(o[:2,1:3])#get first and second row ,also first and second column
#slice or array is a view into data, which means modifying them will change their values in original array
##% datasets
#you can import datasets from your main directory using the following
#data=np.genfromtxt("yourpath",delimiter=';',skip_header=1) #delimiter is when to create new row from set
#different methods of slicing
print(o[:,0:1])#vertical output #means all rows and first column
print(o[:,0])#horizonatl output
#selective
print(o[:,[1,2]])
#slicing backwards
print(o[:,-1])
#data=np.genfromtxt("yourpath",delimiter=';',skip_header==1,name=('column1','column2',)) #dub each column of data
#data['column1'][0:2] #find first 2 values of column nammed column 1
#we can convert and make arthemitc operation on them as well
#data[data['column1']==1][0:2] print first 2 values of before which has value 1
#called boolean masking
