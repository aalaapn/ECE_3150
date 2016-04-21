close all

IB = 5e-6:1e-8:50e-6;
Rmax = .0482./IB;
figure
plot(IB,Rmax)
title('10.1 A')
xlabel('I_B (A)')
ylabel('R (\Omega)')
text(1.5e-5,4000,'R_{max} = .0482/I_B')
text(1.5e-5,500,'R_{min} = 0')

go = 8e-5;
gm = .00566;
ro = 1/go;
Cgd = 10e-15;
Cgs = 30e-15;
Rs = 2000;

hz = logspace(6,12,1000);
w = 2*pi*hz;
Hout = (gm*.5*ro)./(1+j.*w.*Cgd.*ro/2);
figure
HoutdB = 10*log10(abs(Hout).^2);
semilogx(hz,HoutdB)
x = HoutdB(1);
for i = 1:length(hz)
    if HoutdB(i) <= x-3
        x = hz(i);
        break
    end
end
line([x x],[-30 40])
text(3e9,30,['-3dB at f = ',num2str(x, '%8.3e'),' Hz'])
title('10.2 D')
xlabel('f (Hz)')
ylabel('dB')

Ha = (-gm+j*w*Cgd)./(go+go+gm+j*w*(Cgd+Cgs)-go.*Hout);
figure
HadB = 10*log10(abs(Ha).^2);
semilogx(hz,HadB)
x = HadB(1);
for i = 1:length(hz)
    if HadB(i) <= x-3
        x = hz(i);
        break
    end
end
line([x x],[-15 10])
text(2e9,5,['-3dB at f = ',num2str(x, '%8.3e'),' Hz'])
title('10.2 F')
xlabel('f (Hz)')
ylabel('dB')

Hin = 1./(1+j*w*(Cgs+Cgd)*Rs-j*w*Cgd*Rs.*Ha);
figure
HindB = 10*log10(abs(Hin).^2);
semilogx(hz,HindB)
x = HindB(1);
for i = 1:length(hz)
    if HindB(i) <= x-3
        x = hz(i);
        break
    end
end
line([x x],[-60 10])
text(1.5e9,0,['-3dB at f = ',num2str(x, '%8.3e'),' Hz'])
title('10.2 G')
xlabel('f (Hz)')
ylabel('dB')

Htot = Hout.*Ha.*Hin;
figure
HtotdB = 10*log10(abs(Htot).^2);
semilogx(hz,HtotdB)
x = HtotdB(1);
for i = 1:length(hz)
    if HtotdB(i) <= x-3
        x = hz(i);
        break
    end
end
line([x x],[-100 40])
text(2e9,30,['-3dB at f = ',num2str(x, '%8.3e'),' Hz'])
title('10.2 J')
xlabel('f (Hz)')
ylabel('dB')

Hcodea = (-gm+j*w*Cgd)./(go+go+j*w*Cgd);
Hcodein = 1./(1+j*w*(Cgs+Cgd)*Rs-j*w*Cgd*Rs.*Hcodea);
Hcode = Hcodea.*Hcodein;
figure
HcodedB = 10*log10(abs(Hcode).^2);
semilogx(hz,HcodedB)
x = HcodedB(1);
for i = 1:length(hz)
    if HcodedB(i) <= x-3
        x = hz(i);
        break
    end
end
line([x x],[-60 40])
text(2e8,30,['-3dB at f = ',num2str(x, '%8.3e'),' Hz'])
title('10.2 K')
xlabel('f (Hz)')
ylabel('dB')