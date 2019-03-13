import pandas as pandas
import numpy as np 


def cal_moving_averages(y):
#calculate ei moving average for each point
    moving_avgs = list()
    for i in range(len(y)):
        e = np.mean(y[:i+1])
        moving_avgs.append(e)
    return moving_avgs


def fit(y,p,q):
    models = list()
    n = len(y)
       
    e = cal_moving_averages(y)

    if p < q : 
        i = p + 1
    else:
        i = q + 1

    while(i < n+1):
        t = i
        var = list()
        b = list()
        while (t < i+p+q):
            v = reverse(y[t-p:t])            
            v.append(e[t])
            v.append(reverse(e[t-q:t]))

            var.append(v)

            b.append(y[t])

            t += 1

        a = np.array(var)
        b = np.array(b)
        m = np.linalg.solve(a,b)
        models.append(m)

    final model = (list)
    for j in range(p+q):
         
        for i in range(len(models)):
            m 
            
    