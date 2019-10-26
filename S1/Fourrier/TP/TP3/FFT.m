function [Yn] = FFT(l,Xm)
%FFT Summary of this function goes here
%   Detailed explanation goes here
if (l == 0)
   Yn = Xm; 
   return
else
    Yn = zeros(1,2^l);
    m = 2^l;
    n = m/2;
    A = FFT(l-1,X0(l,Xm));
    B = FFT(l-1,X1(l,Xm));
    for k=1:(m/2)
        Yn(k) = A(k) + exp(-(2*1i*pi*(k-1))/m)*B(k);
    end
    for k=((m/2)+1):(2^l)
       Yn(k) =  A(k-n) + exp(-(2*1i*pi*(k-1))/m)*B(k-n);
    end
end

end

