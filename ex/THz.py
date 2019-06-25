#三阶极化率计算
r_0=input()
v_l=input()
A=input()
B=input()
x=eval(r_0)*(1+eval(A)*(eval(v_l)**2)+eval(B)*(eval(v_l)**2))
print("三阶极化率为{}".format(x))