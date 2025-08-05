% Facts: diet suggestions based on diseases
diet(diabetes, 'Low sugar, high fiber, whole grains').
diet(hypertension, 'Low salt, more fruits, leafy vegetables').
diet(obesity, 'Low carbs, high protein, avoid fried foods').
diet(anemia, 'Iron-rich foods like spinach, liver, red meat').
diet(ulcer, 'Avoid spicy food, include bananas, yogurt').

% Rule to suggest diet
suggest_diet(Disease, Diet) :- diet(Disease, Diet).
