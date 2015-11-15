% https://www.hackerrank.com/challenges/fp-list-replication/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    {ok, [N]} = io:fread("", "~d"),
	replicate(N).

replicate(N)->
    replicate(N, io:fread("", "~d")).

replicate(N, {ok, [E|_]})->
    print_times(N, E),
    replicate(N, io:fread("", "~d"));
replicate(_, eof)-> ok.

print_times(0, E) -> ok;
print_times(N, E) -> 
    io:fwrite("~w~n",[E]),
    print_times(N-1, E).