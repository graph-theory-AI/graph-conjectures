"""Smoke test: build the exact solver and check two published cop numbers."""
import os, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "scripts")
DATA = os.path.join(HERE, "..", "data")
PETERSEN_G6 = "IheA@GUAo"   # Petersen graph, cop number 3


@unittest.skipUnless(shutil.which("gcc"), "gcc not available")
class CopwinSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.exe = os.path.join(cls.tmp, "copwin2")
        subprocess.check_call(["gcc", "-O2", "-fopenmp", "-o", cls.exe,
                               os.path.join(SRC, "copwin2.c")], cwd=SRC)

    def run_solver(self, args, g6):
        out = subprocess.run([self.exe, *args], input=g6 + "\n", capture_output=True,
                             text=True, env={**os.environ, "OMP_NUM_THREADS": "2"}, check=True).stdout
        return out

    def test_petersen_is_3(self):
        self.assertIn(" c=3 ", self.run_solver(["-c", "4", "-e"], PETERSEN_G6))

    def test_robertson_is_4(self):
        g6 = open(os.path.join(DATA, "robertson.g6")).read().strip()
        self.assertIn(" c=4 ", self.run_solver(["-c", "5", "-e"], g6))


if __name__ == "__main__":
    unittest.main()
