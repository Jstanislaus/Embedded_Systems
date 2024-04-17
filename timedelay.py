import matplotlib.pyplot as plt
import numpy

array =[]
data =open('timedelay_data.txt','r')
while True:
    line = data.readline()
    if line =='':
        print('hi')
        break
    line = line.split(',')
    print(line)
    line[0]=int(line[0])
    line[1]=float(line[1].strip())
    array.append(line)
print(array)
plt.figure()
plt.plot(array)
plt.show()


