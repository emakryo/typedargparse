import os
import unittest
import subprocess


class TestScripts(unittest.TestCase):

    def setUp(self):
        self.script_path = "scripts"

    def check(self, script, arguments, stdout):
        result = subprocess.run(
                'python ' + script + ' ' + arguments,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("Error in script:", script, arguments)
            print("stdout ############################################")
            print(result.stdout.decode())
            print("###################################################")
            print("stderr ############################################")
            print(result.stderr.decode())
            print("###################################################")
            self.assertEqual(result.returncode, 0)

        self.assertEqual(result.stdout.decode(), stdout)

    def test_one_str(self):
        self.check(os.path.join(self.script_path, "one_str.py"),
                   "foo", "foo\n")

    def test_one_int(self):
        self.check(os.path.join(self.script_path, "one_int.py"),
                   "2", "3\n")

    def test_one_float(self):
        self.check(os.path.join(self.script_path, "one_float.py"),
                   "2.3", "3.3\n")

if __name__ == "__main__":
    unittest.main()
