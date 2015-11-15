% https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    filter(1).

filter(Pos) ->
    filter(Pos, io:fread("", "~d")).

filter(Pos, {ok, [Elem]}) when Pos rem 2 == 0 ->
    io:fwrite("~w~n",[Elem]),
    filter(Pos + 1, io:fread("", "~d"));
filter(Pos, {ok, [_]}) ->
    filter(Pos + 1, io:fread("", "~d"));
filter(_, eof) -> ok.