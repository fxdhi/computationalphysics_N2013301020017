function dla2d(nsum)
nsum=1000
r0=2;
r=8;
Rr=0.5;
L=2000;
Xhalf=floor(L/2);
Yhalf=Xhalf;
szPoints=sparse(L,L);
szPoints(Xhalf,Xhalf)=1;
nx=Xhalf;
ny=Yhalf;
n=0;
theta=2*pi*rand;
x=nx+r*cos(theta);
y=ny+r*sin(theta);
nx=round(x);
ny=round(y);
i=0;
j=1;
p=-1:1;
N2(Xhalf/2)=0;
N2(1)=1;
R=2;             %%用于计算生长维的一个变量
while n<nsum
    i=i+1;
    theta=2*pi*rand;
    x=nx+r0*cos(theta);
    y=ny+r0*sin(theta);
    nx=round(x);
    ny=round(y);
    if sqrt((nx-Xhalf)^2+(ny-Yhalf)^2)>r+20
        %theta=2*pi*rand;   
        nx=Xhalf+r*cos(theta);
        ny=Yhalf+r*sin(theta);
    elseif szPoints(nx-1,ny)+szPoints(nx+1,ny)+szPoints(nx,ny+1)+szPoints(nx,ny-1)>0&szPoints(nx,ny)==0
           szPoints(nx,ny)=1;
           n=n+1;
           s=sqrt((nx-Xhalf)^2+(ny-Yhalf)^2);
           k=round(s)+1;
           N2(k)=N2(k)+1;
           if s>R
               R=s;
               R1(j)=log(R/Rr);
               N1(j)=n;
               I(j)=i;
               j=j+1;
           end
           if s>r
              r=s+5;
          end 
   
       elseif szPoints(nx,ny)==1
           %theta=2*pi*rand;
           nx=Xhalf+r*cos(theta);
           ny=Yhalf+r*sin(theta);
       end
end
[u,v]=find(szPoints);
figure(1);
plot(u,v,'*');
%%%%%%%%%%%%%%%%%%%%%%%%%
%%分维采样数据分析整理
%%%%%%%%%%%%%%%%%%%%%%%%%
num=find(N2);
b=size(num,2);
for i=2:b
    N2(i)=N2(i)+N2(i-1);
    num(i)=N2(i);
    R2(i)=log(2*i);
end
R2(1)=[];
num(1)=[];
save num2 num;
save R2 R2;
figure(2);
plot(R2,log(num),'*');
%%%%%%%%%%%%%%%%%%%%%%%
%%生长维曲线绘制
%%%%%%%%%%%%%%%%%%%%%%%
figure(3);          %画回旋半径与其内粒子数的对数关系图
plot(R1,log(N1),'*');
%%%%%%%%%%%%%%%%%%%%%%%
%%粒子数量与运行步数的关系图绘制
%%%%%%%%%%%%%%%%%%%%%%%
%figure(4);%画凝聚粒子数量与运行步数的关系图
%%plot(N1,I,'o');

