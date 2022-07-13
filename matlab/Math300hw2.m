%% question 1

A1 = [2 -1 4
    9 6 2
    1 3 8];

B1 = [1 1 1
    1 1 1
    1 1 1 ];

X1 = [3
    6
    8];

Y1 = [5 10 15];

% A * B
q1p1 = A1 * B1;

% A * x
q1p2 = A1 * X1;

% x' * B
q1p3 = X1' * B1;

% B * y
%q1p4 = B1 * Y1;
%Error using  * 
%Incorrect dimensions for matrix multiplication. Check that the number of columns in the first
%matrix matches the number of rows in the second matrix. To operate on each element of the matrix
%individually, use TIMES (.*) for elementwise multiplication.


% x * A
%q1p5 = X1 * A1;
%Error using  * 
%Incorrect dimensions for matrix multiplication. Check that the number of columns in the first
%matrix matches the number of rows in the second matrix. To operate on each element of the matrix
%individually, use TIMES (.*) for elementwise multiplication.

% x * Y
q1p6 = X1 * Y1;

% y * X
q1p7 = Y1 * X1;

% x * Y'
%q1p8 = X1 * Y1
%Error using  * 
%Incorrect dimensions for matrix multiplication. Check that the number of columns in the first
%matrix matches the number of rows in the second matrix. To operate on each element of the matrix
%individually, use TIMES (.*) for elementwise multiplication.


% x .* y
q1p9 = X1 .* Y1;

% A .* B
q1p10 = A1 .* B1;


%% question 2

A2 = [1 1 1
    1 2 3
    1 3 6];

B2 = [1
    5
    2];

detofA = det(A2);

rankofA = rank(A2);

x2ver1 = A2\B2;

x2ver2 = inv(A2)*B2;
%less accurate?

%% question 3

A3 = [1 1
    1 2
    1 3];

B3 = [1
    5
    10];

x3 = A3\B3;

testB = A3 * x3;

x = 1:100;
yplot1 = 1 - x;
yplot2 = (1 - x)/2;
yplot3 = (10 - x)/3;

plot(x,yplot1,x,yplot2,x,yplot3);

%as seen as the plot there are no solutions for the system of linear
%equations

%% question 4x,

totalnum = 0;
count2 = 0;
count = 0;
while totalnum < 20
     count = count + 1;
     totalnum = totalnum + rand();
end

disp(count);

%% question 5

t = 0:0.001:2*pi;
%t = 1:1000;

xplot = 1 + cos(2*t);
yplot = -1 + 3*sin(4*t);

plot(xplot,yplot);
