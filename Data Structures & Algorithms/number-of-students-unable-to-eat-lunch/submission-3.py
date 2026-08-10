class Solution:
    from collections import deque
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_c, num_s = 0, 0
        for s in students:
            if s == 0:
                num_c += 1
            else:
                num_s += 1
        students = deque(students)
        i = 0
        while len(students) > 0 and i < len(sandwiches):
            if sandwiches[i] == 0 and num_c == 0:
                return num_s
            if sandwiches[i] == 1 and num_s == 0:
                return num_c
            curr = students.popleft()
            if sandwiches[i] == curr:
                i += 1
                if curr == 0:
                    num_c -= 1
                else:
                    num_s -= 1
            else:
                students.append(curr)
        return len(students)
            
