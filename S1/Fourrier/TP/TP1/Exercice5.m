clc; clear all
f = @(t) (t<=pi).*(t>0) -(t>=-pi).*(t<=0);
t = linspace(-pi,pi,100);
plot(t,f(t));
fchap =@(k) (1i/(pi.*k)).*(((-1)^k)-1);
Sn = [];
n = [1 5 10 50 100 200 1000];

figure()
plot(t,f(t))
hold on;
for i=1:length(n) % grand N 
    S = 0;
    for k=(-n(i)):n(i)
        if k~=0
         S = S + real(fchap(k).*exp(1i.*k.*t));
        end
    end
    Sn(i,:)=S;
    plot(t,S)
    hold on
end
figure()
hold on;
for i=1:length(n) % grand N 
    S = 0;
    for k=(-n(i)):n(i)
        if k~=0
         S = S + real(2*pi*fchap(k)^2.*exp(1i.*k.*t));
        end
    end
    Sn(i,:)=S;
    plot(t,S)
    hold on
end