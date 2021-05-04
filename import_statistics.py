import statistics
from statistics import mean

experi_grp = [11, 4, 8, 34, 89, 65, 9, 13, 55, 78, 90, 64, 85, 42, 78, 99, 47]

x = statistics.mean(experi_grp)

print ("Mean of x : ", x)

contr_grp =  [ 1, 98, 17, 33, 56, 28, 76, 8, 5, 20, 77, 31, 94, 37, 43, 28, 71]


y = statistics.mean(contr_grp)

print ("Mean of y : ", y)

diff_obser =   x - y
print (diff_obser)