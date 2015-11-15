% https://www.hackerrank.com/challenges/fp-reverse-a-list/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    reverse().

reverse() ->
    reverse(io:fread("", "~d")).

reverse({ok, [Elem]}) ->
    reverse(io:fread("", "~d")),
    io:fwrite("~w~n",[Elem]);
reverse(eof) -> ok.