% https://www.hackerrank.com/challenges/eval-ex/

% The series expansion of e^x is given by:
%   1 + x + x^2/2! + x^3/3! + x^4/4! + ...
% Evaluate e^x for given values of x, by using the above expansion for the first 10 terms. 

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    {ok, [Cases]} = io:fread("", "~d"),
	cases(Cases).

% reun all N cases
cases(0) -> ok;
cases(N) ->
    {ok, [Num]} = io:fread("", "~f"),
    Res = e(Num, 10),
    io:fwrite("~f~n",[Res]),
    cases(N-1).

% calculate 'e-serie' sumatory
e(_, 0) -> 0;
e(Num, N) -> (exp(Num, N-1) / factorial(N-1)) + e(Num, N-1).

% calculates a^b
exp(_, 0) -> 1;
exp(A, B) -> A * exp(A, B-1).

% calcualtes N!
factorial(0) -> 1;
factorial(N) -> N * factorial(N-1).