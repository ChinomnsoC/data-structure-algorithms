from typing import List


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        student_scores = {}

        for i in range(len(report)):
            score = 0  # float('-inf') # or 0?
            words_in_report = report[i].split()

            for word in words_in_report:
                if word in positive_set:
                    print(word)
                    score += 3
                if word in negative_set:
                    print(word)
                    score -= 1

            key = student_id[i]
            student_scores[key] = score

        sorted_ids = self.sort_student_scores(student_scores)

        print(student_scores)

        return sorted_ids[:k]

    def sort_student_scores(self, student_scores):
        sorted_ids = []

        sorted_items = sorted(student_scores.items(), key=lambda x: (-x[1], x[0]))

        print(sorted_items)
        for student_id, score in sorted_items:
            sorted_ids.append(student_id)

        return sorted_ids
    
    


positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is studious", "the student is smart"]
student_id = [1, 2]
k = 2

top_stu = Solution()
print(top_stu.topStudents(positive_feedback, negative_feedback, report, student_id, k))
