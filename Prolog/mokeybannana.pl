% State format: state(MonkeyPos, MonkeyStatus, BoxPos, HasBanana)

% Base case: monkey has banana
can_get(state(_, _, _, has)).

% Monkey climbs box when at same position
can_get(state(P, on_floor, P, not)) :- 
    can_get(state(P, on_box, P, not)).

% Monkey grasps banana when on box at banana's position
can_get(state(middle, on_box, middle, not)) :- 
    can_get(state(_, _, _, has)).

% Monkey pushes box from one position to another
can_get(state(P1, on_floor, P1, not)) :- 
    move(P1, P2),
    can_get(state(P2, on_floor, P2, not)).

% Monkey moves to another position
can_get(state(P1, on_floor, B, not)) :- 
    move(P1, P2),
    can_get(state(P2, on_floor, B, not)).

% Possible positions
move(left, middle).
move(middle, left).
move(right, middle).
move(middle, right).
