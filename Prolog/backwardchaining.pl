knows(rainy).
if(rainy, wet).

prove(X) :- knows(X).
prove(X) :- if(Y, X), prove(Y).
