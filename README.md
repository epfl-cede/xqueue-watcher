xqueue_watcher
==========

This is an implementation of a polling [XQueue](https://github.com/edx/xqueue) client and grader.


Running
=======

```
source venv/bin/activate
python -m xqueue_watcher -d staging/
```


JSON configuration file
=======================
	{
		"test-123": {
			"SERVER": "http://127.0.0.1:18040",
			"CONNECTIONS": 1,
			"AUTH": ["lms", "lms"],
			"HANDLERS": [
				{
					"HANDLER": "xqueue_watcher.grader.Grader",
					"KWARGS": {
						"grader_root": "/path/to/course/graders/",
					}
				}
			]
		}
	}

* `test-123`: the name of the queue
* `SERVER`: XQueue server address
* `AUTH`: list of username, password
* `CONNECTIONS`: how many threads to spawn to watch the queue
* `HANDLERS`: list of callables that will be called for each queue submission
	* `HANDLER`: callable name
	* `KWARGS`: optional keyword arguments to apply during instantiation


xqueue_watcher.grader.Grader
========================
To implement a pull grader:

Subclass xqueue_watcher.grader.Grader and override the `grade` method. Then add your grader to the config like `"handler": "my_module.MyGrader"`. The arguments for the `grade` method are:
	* `grader_path`: absolute path to the grader defined for the current problem
	* `grader_config`: other configuration particular to the problem
	* `student_response`: student-supplied code


Sandboxing
==========
To sandbox python, use [CodeJail](https://github.com/edx/codejail). In your handler configuration, add:

	"CODEJAIL": {
		"name": "python",
		"python_bin": "/path/to/sandbox/python",
		"user": "sandbox_username"
	}

Then, `codejail_python` will automatically be added to the kwargs for your handler. You can then import codejail.jail_code and run `jail_code("python", code...)`. You can define multiple sandboxes and use them as in `jail_code("special-python", ...)`


EPFL Setup
=====

```
virtualenv -p /usr/local/bin/python2.7 venv
source venv/bin/activate
make install requirements
make test
```

```
python -m xqueue_watcher -d .
```

Here is Sandbox curse https://test-courseware.epfl.ch/courses/course-v1:EPFL+Sandbox01+x/courseware/2f40a30e24fc4ccc908919cc3a7e5a05/12256998e61c4523bf9bb1c7f59f0dbd/1?activate_block_id=block-v1%3AEPFL%2BSandbox01%2Bx%2Btype%40vertical%2Bblock%4065196331ded740808e50f621d15e885e
