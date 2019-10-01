%% Question A
% Question 1
global a b 
a = -2
b =  2
k = [1 5 50 100];
g = @(s) (1-abs(s)).*(abs(s)<=1);
g = @(s) (exp(-s.*s)./sqrt(pi))
gk = @(s,k) k.*g(k.*s);
n = [5 10 50 100];
Rn = @(f,n1,k) ((b-a)/n1)*sum(f(a+(0:(n1-1)).*((b-a)/n1),k));
res =[]
mat = []
col = ['r' 'g' 'b' 'k'];
s = [-1:0.01:1];
figure()
plot(s,gk(s,1))
title("$g(t)$ pour k",'interpreter','latex')
for i=2:4
    line(s,gk(s,k(i)),'Color',col(i));
end
legend("k=1","k=5","k=10","k=50")
for i=1:4
    for j=1:4
        res(j)  = Rn(gk,100,k(i));
    end
    mat(i,:) = res;
end
figure()
plot(k,mat(1,:))
title("$g(t)$ pour k",'interpreter','latex')
for i=2:4
    line(k,mat(i,:),'Color',col(i));
end
legend("$k=1$","$k=5$","$k=10$","$k=50$",'interpreter','latex')
% Question 4 
xsi = @(x) (x>=-1).*(x<=1).*0.5;
conv = @(t,s,k) xsi((t-s)).*gk(s,k);
Rn2 = @(t,n1,i) ((b-a)/n1).*sum(conv(t,(a+(0:(n1-1)).*(b-a)/n1),i));
n = 1000
T = a+[0:n].*((b-a)/n)
Ra = [];
for i=1:length(k)
    for j=1:n+1
        Ra(i,j) =Rn2(T(j),n,k(i));
    end
end
Ra

for i=1:4
    figure()
    plot(T,Ra(i,:),'Color','red')
    line(x,xsi(x))
    line(s,gk(s,k(i)),'Color',col(i));
    axis([-3 3 -0.5 1])
end