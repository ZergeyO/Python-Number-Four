import numpy as np
from scipy.special import spherical_jn as jn
from scipy.special import spherical_yn as yn

c = 3e8

class RCScalculations:

    def __init__(self, D, f_min, f_max, ):
        self.r=np.longdouble(D/2)
        self.frequency=np.linspace(f_min, f_max, 100)
        self.lentgh=0
        self.k=0
        self.RCS=np.zeros_like(self.frequency)

    def H_coef(self, n, kr):
        return np.clongdouble(jn(n, kr)+1j*yn(n, kr))
    
    def A_coef(self, n):
        numerator= np.longdouble(jn(n, self.k*self.r))
        divider= self.H_coef(n,self.k*self.r)
        return np.divide(numerator, divider)
    
    def B_coef(self, n):
        numerator = self.k * self.r * np.longdouble(jn(n-1, self.k * self.r)) - n * np.longdouble(jn(n, self.k * self.r))
        divider = self.k * self.r * self.H_coef(n-1, self.k * self.r) - n * self.H_coef(n, self.k * self.r)
        return np.divide(numerator, divider)
    
    def RCScalculate(self):
        for i in range(0, 100):
            summ=0;
            self.lentgh= np.longdouble(c / self.frequency[i])
            self.k = np.longdouble(2 * np.pi / self.lentgh)
            for n in range(1, 51):
                summ+=((-1)**n)*(n+0.5)*(self.B_coef(n)-self.A_coef(n))**2
            summ= (np.abs(summ)*(self.lentgh**2)/np.pi)
            self.RCS[i]=summ
            

    def GetFrequency(self):
        return self.frequency
    
    def GetRCS(self):
        return self.RCS
    
    def GetLentgh(self):
        return self.lentgh
