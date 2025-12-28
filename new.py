from module import * #import module all
# from module import simpleInterest, compoundInterest
# import module should use module.simpleInterest() and module.compoundInterest()

p = float(input("Enter principle: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))
print(f'Simple Interest is {simpleInterest(p,t,r):.3f}')
print(f'Compound Interest is {compoundInterest(p,t,r):.3f}')