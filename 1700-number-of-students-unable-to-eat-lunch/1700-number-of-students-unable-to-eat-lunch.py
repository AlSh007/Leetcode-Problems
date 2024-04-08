class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = 0
        square_student_count = 0
        
        for student in students:
            if student == 0:
                circle_student_count += 1
            else:
                square_student_count += 1
        
        for sandwich in sandwiches:
            if sandwich == 0 and circle_student_count == 0:
                return square_student_count
            
            if sandwich == 1 and square_student_count == 0:
                return circle_student_count
            
            if sandwich == 0:
                circle_student_count -= 1
            else:
                square_student_count -= 1
        
        return 0