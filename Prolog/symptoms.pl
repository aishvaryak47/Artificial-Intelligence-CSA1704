% Facts: Symptoms
symptom(fever).
symptom(cough).
symptom(sore_throat).
symptom(rash).
symptom(headache).
symptom(fatigue).
symptom(body_pain).
symptom(runny_nose).

% Rules: Diagnosis based on symptoms
disease(cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sore_throat).

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain),
    symptom(fatigue).

disease(measles) :-
    symptom(fever),
    symptom(rash),
    symptom(runny_nose),
    symptom(sore_throat).

disease(migraine) :-
    symptom(headache),
    symptom(fatigue),
    \+ symptom(fever).

% Main rule to diagnose
diagnose :-
    disease(D),
    write('You may have: '), write(D), nl,
    fail.  % backtracking to find all possible diseases
diagnose.
