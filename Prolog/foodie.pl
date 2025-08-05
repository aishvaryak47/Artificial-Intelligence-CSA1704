% Knowledge Base
likes(john, pizza).
likes(john, pasta).
likes(mary, salad).

% Rule
foodie(X) :- likes(X, pizza), likes(X, pasta).

% Sample Queries:
% ?- foodie(john).
% ?- foodie(mary).
