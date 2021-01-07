import json, requests
from xqueue_watcher.grader import Grader

class tutorGrader(Grader):
    def grade(self, student_response, files):
        return {
            "errors": [],
            "tests": [
                [
                    "short-description",
                    "Well done!",
                    True,
                    "actual-output",
                    "actual-output"
                ]
            ],
            "correct": True,
            "score": .9,
        }
