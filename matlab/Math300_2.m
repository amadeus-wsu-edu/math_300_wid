A = [1 2 ; 3 4];
B = [5 6 ; 7 8];

C = A*B; 
D = A.*B;

E = A.^2;

F = A^2;

A1 = [1 2 ; 3 4 ; 5 6];

C2 = A';

D1 = A';

matrix1 = [1,1,1;1,1,1;1,1,1];
matrix2 = [0,0,0;0,0,0;0,0,0];
matrix3 = [1,0,0;0,1,0;0,0,1];

v = 1:10;
w = 1:2:10;

matrix4 = [1,2,3;4,5,6;7,8,9];
disp(matrix4(2,2));

disp(matrix4(2,1:3));
disp(matrix4(1:3,1));

numa = rand;
message = ['The result is: ' num2str(numa)];
disp(message);

%% variables
a=3;

%% Code
if a > 0
    x = 0;
elseif a < 0
    x = 1;
else
    x = 2;
end

%% Code 2
N = 10;
for a1 = 1:N
    disp('a1');
end 

vector1 = 1:10;
sum = 0;
for j = vector1
    sum = sum + j;
end

%% while loops

randomx = randi(1000);
disp(randomx)

while randomx <= 500
    randomx = randi(1000);
    disp(randomx)
end

% && vs ||
% && == AND, || == OR


%% 11jul
failed = true;
numoftries = 0;

while failed
    numoftries = numoftries + 1;
    dice1 = randi(6);
    dice2 = randi(6);
    if dice1 == 6 && dice1 == dice2
        failed = false;
    end
end
disp(numoftries);

%% 12 jul

l = 10;
N = 10;

h = l/N;

f(1) = 0;

for n = 1:N
    f(n+1) = f(n)+ h*(n^2 + n + 1);
end

x = linspace(0,l,N+1);
plot(x,f);

