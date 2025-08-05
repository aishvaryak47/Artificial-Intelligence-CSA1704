% student(StudentName, SubjectCode).
student(ravi, cs101).
student(meena, cs102).
student(kumar, cs101).
student(sita, cs103).

% teacher(TeacherName, SubjectCode).
teacher(dr_singh, cs101).
teacher(ms_jaya, cs102).
teacher(mr_raju, cs103).

% subject(SubjectCode, SubjectName).
subject(cs101, 'Artificial Intelligence').
subject(cs102, 'Machine Learning').
subject(cs103, 'Data Science').

% Rule to find teacher of a student
teacher_of_student(Student, Teacher) :-
    student(Student, SubCode),
    teacher(Teacher, SubCode).

% Rule to find subject handled by teacher
subject_by_teacher(Teacher, SubjectName) :-
    teacher(Teacher, SubCode),
    subject(SubCode, SubjectName).
