import unittest
import subprocess


class TestScripts(unittest.TestCase):

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

    def test_one_argument(self):
        self.check("script_one_argument.py", "foo", "foo\n")

if __name__ == "__main__":
    unittest.main()
