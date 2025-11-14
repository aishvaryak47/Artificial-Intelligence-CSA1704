fact(rainy).
fact(cloudy).

rule(cloudy, rain).
rule(rain, wet).

forward :- fact(X), rule(X, Y), \+ fact(Y), assert(fact(Y)), fail.
forward.

show_facts :- fact(X), write(X), nl, fail.
