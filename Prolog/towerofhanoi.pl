% hanoi(N, Source, Destination, Auxiliary)
hanoi(1, Source, Destination, _) :-
    format('Move disk 1 from ~w to ~w~n', [Source, Destination]).

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),
    format('Move disk ~w from ~w to ~w~n', [N, Source, Destination]),
    hanoi(M, Auxiliary, Destination, Source).
