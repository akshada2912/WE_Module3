from scipy.stats import binom
p=0.25
n=1000
q=1-p
num_sim=10000
num_1=240

def bf():
    cdf=binom.cdf(num_1-0.5,n,p)
    print(f"{1-cdf}")

def bs():
    count=0
    sims=binom.rvs(n,p,size=num_sim)
    for s in sims:
        if s>=num_1:
            count+=1
    print(f"{count/num_sim}")

bs()
bf()