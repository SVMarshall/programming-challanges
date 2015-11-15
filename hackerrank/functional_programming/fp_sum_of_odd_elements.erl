% https://www.hackerrank.com/challenges/fp-sum-of-odd-elements/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    sum_odd().

sum_odd() ->
    sum_odd(0, io:fread("", "~d")).

sum_odd(Sum, {ok, [Elem]}) when Elem rem 2 /= 0 ->
    sum_odd(Sum + Elem, io:fread("", "~d"));
sum_odd(Sum, {ok, [_]}) ->
    sum_odd(Sum, io:fread("", "~d"));
sum_odd(Sum, eof) -> 
    io:fwrite("~w~n",[Sum]).