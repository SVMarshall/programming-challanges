% https://www.hackerrank.com/challenges/fp-list-length/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    count().

count() ->
    count(0, io:fread("", "~d")).

count(N, {ok, _}) ->
    count(N + 1, io:fread("", "~d"));
count(N, eof) ->
    io:fwrite("~w~n",[N]).