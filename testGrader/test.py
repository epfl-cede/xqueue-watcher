import json, requests
from xqueue_watcher.grader import Grader

class testGrader(Grader):
    def grade(self, grader_path, grader_config, student_response, files):
        files = json.loads(files)
        errors = []
        files_access = []
        for name in files:
            url = files[name]
            response = requests.get(url)
            if response.status_code != 200:
                errors.append("File {} access error: {}".format(url, response.status_code))
            else:
                files_access.append("File={}, name={}, size={}".format(url, name, len(response.content)))
        if errors:
            return {
                'errors': errors,
                'tests': [],
                'correct': False,
                'score': 0,
            }
        else:
            return {
                "errors": [],
                "tests": [
                    [
                        "short-description",
                        "; ".join(files_access),
                        True,
                        "actual-output",
                        "actual-output"
                    ]
                ],
                "correct": True,
                "score": 1,
            }
