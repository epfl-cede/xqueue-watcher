from xqueue_watcher.grader import Grader

class testGrader(Grader):
    def grade(self, grader_path, grader_config, student_response):
        print("student_response={}".format(student_response))
        result_0 = {
            'errors': [],
            'tests': [],
            'correct': False,
            'score': 0,
        }
        result_1 = {
            "errors": [],
            "tests": [
                [
                    "short-description",
                    "long-description",
                    True,
                    "actual-output",
                    "actual-output"
                ]
            ],
            "correct": True,
            "score": 1,
        }
        return result_1
