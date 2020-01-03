%% Partie 1 : 

clc;clear all;close all;
% Question 1
[y1,Fs1] = audioread('JH.wav');
[y2,Fs2] = audioread('LVB.wav');
dt1 = 1/Fs1;
dt2 = 1/Fs2;
plot(0:dt1:((length(y1)-1)*dt1),y1)
figure()
plot(0:dt2:((length(y2)-1)*dt2),y2)

% Question 2
X1 = fft(y1,length(y1));
X2 = fft(y2,length(y2));
N1 = (Fs1/length(y1))*0:(length(y1)-1);
N2 = (Fs1/length(y2))*0:(length(y2)-1);
figure()
subplot(2,2,1)
plot(N1,abs(X1))
subplot(2,2,2)
plot(N2,abs(X2))
subplot(2,2,3)
plot(N1,angle(X1))
subplot(2,2,4)
plot(N2,angle(X2))

% Question 3 
Rand1 = 2*pi*rand((length(N1)/2)-1,1);
Rand2 = 2*pi*rand((length(N2)/2)-1,1);
R1 = [0 ;Rand1; 0;-Rand1(end:-1:1)];
R2 = [0 ;Rand2; 0;-Rand2(end:-1:1)];
ygen1 = abs(X1).*exp(1i.*R1);
ygen2 = abs(X2).*exp(1i.*R2);
Yf1 = ifft(ygen1);
Yf2 = ifft(ygen2);
sound(Yf1,Fs1)
sound(y1,Fs1)
sound(Yf2,Fs2)
sound(y2,Fs2)

% La modification de la phase donne du bruit et rend le son inintelligible.

% Question 5
% La phase de ces filtres dois vérifier une periodicité 

%% Partie 2 :

% Question 1 
V1 = ones(length(y1),1);
V2 = ones(length(y2),1);
R1p = angle(X1);
R2p = angle(X2);
Yp1 = ifft(V1.*exp(1i.*R1p));
Yp2 = real(ifft(V2.*exp(1i.*R2p)));
soundsc(Yp1,Fs1)
soundsc(Yp2,Fs2)

%% Partie 3 :

V1 = abs(X1).*exp(1i.*angle(X2));
V2 = abs(X2).*exp(1i.*angle(X1));
Yf1 = real(ifft(V1));
Yf2 = ifft(V2);
soundsc(Yf1,Fs1);
soundsc(Yf2,Fs2);