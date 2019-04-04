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
    print(y)
    print(type(y))
    
    if p < q : 
        i = p + 1
    else:
        i = q + 1

    while(i < n+1):
        t = i
        var = list()
        b = list()
        while (t < i+p+q):
            v = []
            v.append(list(reversed(y[t-p:t])))
            
            for item in reversed(y[t-p:t]):
                v.append(item)
            v.append(e[t])
            v.append(list(reversed(e[t-q:t])))
            var.append(v)

            b.append(y[t])

            t += 1

        a = np.array(var)
        b = np.array(b)
        m = np.linalg.solve(a,b)
        models.append(m)
        i = i+1

    final_model = dict()
    ar = list()
    ma = list()
    for j in range(p):
        a = list()
        for i in range(len(models)):
            a.append(models[i][j])
        mean = np.mean(a)
        ar.append(mean)

    for j in range(p,q):
        a = list()
        for i in range(len(models)):
            a.append(models[i][j])
        mean = np.mean(a)
        ma.append(mean)

    final_model['ar'] = ar
    final_model['ma'] = ma
    print(final_model)
    return final_model 

def fixed_fit(y):
    models = list()
    n = len(y) 
    e = cal_moving_averages(y)
    
    models = list()
    i = 2
    while i<n:
        a = list()
        b = list()
        coeff = list()
        
        a.append(y[i-1])
        a.append(e[i-1])
        
        b.append(y[i-2])
        b.append(e[i-2])
        
        c = list()
        c.append(y[i])
        c.append(y[i-1])
        
        coeff.append(a)
        coeff.append(b)
        
        m = np.linalg.solve(coeff,c)
        #print(m)
        models.append(list(m))
        i = i+1
    
    ar = 0
    ma = 0
    
    a = list()
    for i in range(len(models)):
        a.append(models[i][0])
    ar = np.mean(a)

    a = list()
    for i in range(len(models)):
        a.append(models[i][1])
    ma = np.mean(a)

    return ar,ma