clc; clear all
n = [1 5 10 50 100];
col = ['r' 'g' 'b' 'k'];
Dn = @(N,t) (1/(2*pi)).*(sin((N+0.5).*t))./sin(t/2);
T2 = [-pi :0.01 :pi];
A = [];
for i=1:4
    for j=1:length(T2)
        A(i,j) = Dn(n(i),T2(j));
    end
    plot(T2,A(i,:));
    hold on
end
global a b
a = -pi 
b = pi
Rn = @(f,n1,N) ((b-a)/n1)*sum(f(N,a+(0:(n1-1)).*((b-a)/n1)));
Rabs = @(f,n1,N) ((b-a)/n1)*sum(abs(f(N,a+(0:(n1-1)).*((b-a)/n1))));
res = []
for i=1:5
    res(i)  = Rn(Dn,200,n(i));
end
figure()
plot(n,res)
title("$g(t)$ pour k",'interpreter','latex')
res2 =[]
for i=1:5
    res2(i)  = Rabs(Dn,200,n(i));
end
figure()
plot(n,res2)
title("$g(t)$ pour k",'interpreter','latex')
