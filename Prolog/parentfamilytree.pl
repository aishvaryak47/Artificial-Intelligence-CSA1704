% Facts
parent(john, mary).
parent(john, david).
parent(mary, alice).
parent(david, tom).

male(john).
male(david).
male(tom).
female(mary).
female(alice).

% Rules
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
