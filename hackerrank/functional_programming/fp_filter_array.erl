% https://www.hackerrank.com/challenges/fp-filter-array/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    {ok, [Limit]} = io:fread("", "~d"),
    filter(Limit).

filter(Limit) ->
    filter(Limit, io:fread("", "~d")).

filter(_, eof) -> ok;
filter(Limit, {ok, [Elem]}) ->
    print(Limit, Elem),
    filter(Limit, io:fread("", "~d")).

print(Limit, Elem) when Elem < Limit ->
    io:fwrite("~w~n",[Elem]);
print(_, _) -> ok.