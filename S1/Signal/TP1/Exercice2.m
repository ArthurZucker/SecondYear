%% Initialisation de matlab
clc;clear all; close all;
%% Question 1:  Preparation des fichiers à traiter
load('son1.mat'); load('son2.mat');
%% Question 2 :
Fech = 44100;
N = size(son1,1);
t_vect = (0 : N - 1)/Fech; % abscisses temporelles
f_vect = (0 : N-1)*(Fech/N);



figure(2)
subplot(2,2,1)
plot(t_vect,son1)
subplot(2,2,2)
plot(f_vect,abs(fft(son1)))
subplot(2,2,3)
plot(t_vect,son2)
subplot(2,2,4)
plot(f_vect,abs(fft(son2)))
tot = son1(:,1);
for i=2:size(son1,2)
    sound(tot,Fech);
    tot = tot + son1(:,i);
    pause(0.4)
end

tot = son2(:,1);
for i=2:size(son2,2)
    sound(tot,Fech);
    tot = tot + son2(:,i);
    pause(0.4)
end

% Observer le spectre pour savoir où est l'energie