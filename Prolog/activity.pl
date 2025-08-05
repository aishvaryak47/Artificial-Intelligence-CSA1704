% Facts
temperature(high).
humidity(high).

% Rules
suggest(go_beach) :- temperature(high), humidity(low).
suggest(stay_home) :- temperature(high), humidity(high).
suggest(go_hiking) :- temperature(low), humidity(low).

% Query format: ?- suggest(Activity).
