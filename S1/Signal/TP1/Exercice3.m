%% Initialisation de matlab 
clc; clear all; close all;

%% Question 1 ;
% Define time vector to use in chirp function 
Fe = 2*6000; % 8000 à l'origine
T = 0:1/Fe:3;
F0 = 20;
F1 = 6000;
Y = chirp(T,F0,10,F1);
spectrogram(Y,256,250,256,1E3); 
soundsc(Y,Fe)

% Pourquoi la fréquence diminue? Ici on a demandé un sinus glissant, la
% fréquence bouge enfct du temps. A t, le chirp est un sinus, sa
% transformée de fourier en module vaut : 1/2 x masse de diract en f0 et
% -f0. Deux rais placées à la fréquence f0. Or la fréquence du chirp
% augmente. (déplacement vers la gauche pour -f0 vers la droite pour f0.
% Nous il va de 20 à 6000Hz, le spectre part de deux rais placée à 20 et
% -20 etc. On devrait entendre très grave jusqu'à très aigue. Or la
% fréquence diminue vers la fin. Pourquoi? Nous on joue un chirp, un sinus
% glissant discret, on a pas de temps continue. Comme il est discret, sa TF
% est périodique de période Fe (echantilonage) or ici Fe = 8000. Comme on
% aune periodicté, il y a un chevauchement. A T0 on périodise et on centre
% en la fréquence d'échantillonage, (donc en 16 000, 24000,... -8000, -16
% 000) etc etc. Il arrive un moment ou les deux fréquence se croisent en
% Fe/2 (ici 4000). En 2secondes ici (puisque que on v aà 6000 en 3sec) donc
% ne entend toutes les rais, on est moins sensible avec les aigues, donc la
% raie qui monte est moins perçue par l'oreil. On augmente donc la
% fréquence d'échantillonage  à Fe = 2*Fmax =12 000Hz ou plus.
