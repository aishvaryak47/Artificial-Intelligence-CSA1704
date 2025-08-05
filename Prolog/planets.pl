% planet(Name, DistanceFromSun_MillionKm, Diameter_Km, NumberOfMoons)
planet(mercury, 57.9, 4879, 0).
planet(venus, 108.2, 12104, 0).
planet(earth, 149.6, 12756, 1).
planet(mars, 227.9, 6792, 2).
planet(jupiter, 778.5, 142984, 79).
planet(saturn, 1433.5, 120536, 82).
planet(uranus, 2872.5, 51118, 27).
planet(neptune, 4495.1, 49528, 14).

% Query rule to get planets with more than N moons
has_more_moons_than(N, Planet) :-
    planet(Planet, _, _, Moons),
    Moons > N.
