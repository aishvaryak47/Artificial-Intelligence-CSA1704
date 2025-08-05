% Facts: person(Name, DOB).
% DOB format: date(DD, MM, YYYY)

person(john, date(15, 6, 1995)).
person(alice, date(23, 12, 1998)).
person(ravi, date(5, 9, 2001)).
person(sita, date(1, 1, 2000)).
person(kumar, date(30, 11, 1990)).

% Query example:
% ?- person(Name, date(_, _, 1998)).
% This will return names of people born in the year 1998.
