% Graph edges: edge(Node, Neighbor, Cost)
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 1).
edge(c, e, 5).
edge(d, f, 4).
edge(e, f, 2).

% Heuristic values: h(Node, Value)
h(a, 5).
h(b, 3).
h(c, 4).
h(d, 2).
h(e, 6).
h(f, 0).  % Goal node

% Best First Search
best_first_search(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% If head of path is goal, return path
bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).

% Continue search
bfs([[Current|Rest]|Paths], Goal, Result) :-
    findall([Next,Current|Rest],
            (edge(Current, Next, _), \+ member(Next, [Current|Rest])),
            NewPaths),
    append(Paths, NewPaths, TempPaths),
    sort_paths(TempPaths, Sorted),
    bfs(Sorted, Goal, Result).

% Sort paths based on heuristic of head node
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_heuristic([Node|_], H) :- h(Node, H).
