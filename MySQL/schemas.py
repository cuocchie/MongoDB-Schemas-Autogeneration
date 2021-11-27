class Classes:
    tablename = 'classes'

    class_id = 'class_id'
    name = 'name'
    is_specialized = 'is_specialized'


class Grades:
    tablename = 'grades'

    grade_id = "grade_id"
    lang = 'lang'
    math = 'math'


class Students:
    tablename = 'students'

    student_id = 'student_id'
    name = 'name'
    grade_id = 'grade_id'
    class_id = 'class_id'