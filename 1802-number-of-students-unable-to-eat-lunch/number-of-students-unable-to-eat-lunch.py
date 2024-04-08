class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable_to_eat = 0
        i = 0

        while i < len(students):
            top = sandwiches[0]
            if students[0] == top:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
            else:
                popped_stud = students.pop(0)
                students.append(popped_stud)
                i += 1
        return len(students)


