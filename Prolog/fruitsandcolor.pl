% Facts: fruit and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(kiwi, green).
fruit_color(blueberry, blue).
fruit_color(pineapple, yellow).

% Sample query to use:
% ?- fruit_color(Fruit, yellow).
% Prolog will backtrack and list all fruits that are yellow.
