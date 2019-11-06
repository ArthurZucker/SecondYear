%% Initialisation de matlab
clc;clear all; close all;
%% Donées:
T       = 2; %2 secondes 
Fs      = 8000;
dt      = 1/Fs;
a       = [0.1 1 5];
A       =[1 2];
alpha   = [0.1 0.5 0.75];
phi     = [0 pi/4 pi/2];
U = @(t) 1*(t>=0);
r = @(a,t) t*a;
rectangle = @(A,alpha,t) A*((alpha/55)>mod(t,1/55)).*(t>0) + A*((alpha/55)>mod(-t,1/55)).*(t<0);
sinu = @(A,phi,t) A*sin(t*55*2*pi + phi);
col = ['r' 'g' 'b' 'y' 'm' 'c' 'k'];
%% Question 1 :
t_vect = -1:dt:1; 
%% Question 2 :
% Modélisation de la rampe
figure(1)
for i=1:length(a)
    R(i,:) = r(a(i),t_vect);
    plot(t_vect,R(i,:),'col',col(i),'linewidth',2);
    hold on;
end
legend('a = 0.1','a = 1','a = 5')
xlabel('temps')
ylabel('$f(t) = a*t$','interpreter','latex')
title("Représentation de l'évolution d'une fonction rampe Pour différentes valeur")
% Modélisation du rectangle pour diférentes valeurs de A et a
figure(2)
for i=1:length(A)
    for j=1:length(alpha)
        REC((length(A)+1)*(i-1)+j,:) = rectangle(A(i),alpha(j),t_vect);
        plot(t_vect,REC(length(A)*(i-1)+j,:),'linewidth',2);
        lege((length(A)+1)*(i-1)+j) = "A = " + A(i) + ", $\alpha$ = " + alpha(j);
        hold on;
    end
end
legend(lege,'interpreter','latex');
xlabel('temps')
ylabel('$f(t) = a*T*alpha$','interpreter','latex')
title("Représentation de l'évolution d'une fonction carrée Pour différentes valeur")
% Modélisation des sinusoïdes 
figure(3)
for i=1:length(A)
    for j=1:length(phi)
        SI((length(A)+1)*(i-1)+j ,:) = sinu(A(i),phi(j),t_vect);
        plot(t_vect,SI(length(A)*(i-1)+j ,:),'linewidth',2);
        lege2((length(A)+1)*(i-1)+j) = "A = " + A(i) + ", $\phi$ = " + phi(j);
        hold on;
    end
end
legend(lege2,'interpreter','latex');
xlabel('temps')
ylabel('$f(t) = sin(A*t +phi)$','interpreter','latex')
title("Représentation de l'évolution d'une fonction sinisoidale Pour différentes valeur")

%% Question 3 
% Calculons la puissance moyenne des signaux 
f = 1/Fs;
for i=1:size(REC,1)
    Pui_rec(i) = f*sum(REC(i,:).^2);
end
for i=1:size(SI,1)
    Pui_sin(i) = f*sum(SI(i,:).^2);
end
for i=1:size(R,1)
    Pui_r(i) = f*sum(R(i,:).^2);
end
