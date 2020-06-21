import numpy as np
import matplotlib.pyplot as plt

xu1=list(range(0,13))
   #2/29,  3/7     3/14    3/21    3/28    4/4      4/11    4/18    4/25    5/2        5/9         5/16       5/23
yu1=[64,    345,    1678,   22043,  121117, 312076, 530384,  738697, 955488, 1156744 ,  1342723,    1503684,   1650677 ]
reg=np.polyfit(xu1,yu1,12)
print('reg=',reg)

xu2 = list(range(0,14))
ry2 = np.polyval(reg,xu2)

plt.plot(xu1,yu1,'b^',label='f(x)',linestyle='--')
plt.plot(xu2,ry2,'r.',label='regression',linestyle='-.')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('date')
plt.ylabel('COV-19')

mse=np.sum((yu1-ry2)**2)/len(xu2)
print('mse=', mse)
print('13=', np.polyval(reg,13)) 
plt.show()
