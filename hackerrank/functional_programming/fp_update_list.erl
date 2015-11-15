% https://www.hackerrank.com/challenges/fp-update-list/

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    L1 = read_list(),
	L2 = update(L1),
    print_list(L2).

update([]) -> [];
update([Elem|L]) ->
    [abs(Elem)|update(L)].

% read list from io, pushing back
read_list() ->
    read_list(io:fread("", "~d")).
read_list(eof) -> [];
read_list({ok, [Elem]}) ->    
    [Elem|read_list(io:fread("", "~d"))].

print_list([]) -> ok;
print_list([Elem|L]) ->
    io:fwrite("~w~n",[Elem]),
    print_list(L).