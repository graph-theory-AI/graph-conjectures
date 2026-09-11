"""Check published cop numbers and graph6 input with an OpenMP-capable compiler."""
import os
import shlex
import shutil
import subprocess
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "scripts")
DATA = os.path.join(HERE, "..", "data")
PETERSEN_G6 = "IheA@GUAo"   # Petersen graph, cop number 3


class CopwinSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cc = shlex.split(os.environ.get("CC", "gcc"))
        if not cc or not shutil.which(cc[0]):
            raise unittest.SkipTest("C compiler not found; set CC to an OpenMP-capable compiler")
        compile_flags = shlex.split(os.environ.get("CPPFLAGS", ""))
        compile_flags += shlex.split(os.environ.get("CFLAGS", "-O2 -fopenmp"))
        link_flags = shlex.split(os.environ.get("LDFLAGS", ""))
        link_flags += shlex.split(os.environ.get("LDLIBS", ""))

        tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(tmp.cleanup)
        cls.exe = os.path.join(tmp.name, "copwin2")
        probe_source = (
            "#include <omp.h>\n"
            "#ifndef _OPENMP\n"
            '#error "OpenMP support is required"\n'
            "#endif\n"
            "int main(void) { return omp_get_max_threads() < 1; }\n"
        )
        probe_path = os.path.join(tmp.name, "openmp_probe.c")
        with open(probe_path, "w") as probe_file:
            probe_file.write(probe_source)
        probe = subprocess.run(
            [*cc, *compile_flags, probe_path, "-o",
             os.path.join(tmp.name, "openmp_probe"), *link_flags],
            capture_output=True, text=True,
        )
        if probe.returncode:
            raise unittest.SkipTest(
                "OpenMP compile/link probe failed; configure CC, CPPFLAGS, CFLAGS, "
                "LDFLAGS and LDLIBS (see docs/computations.md): " + probe.stderr.strip()
            )
        # Once the toolchain works, solver compilation errors must fail the tests.
        subprocess.check_call(
            [*cc, *compile_flags, "-o", cls.exe, os.path.join(SRC, "copwin2.c"),
             *link_flags], cwd=SRC,
        )

    def run_raw(self, args, g6):
        return subprocess.run([self.exe, *args], input=g6 + "\n", capture_output=True,
                              text=True, env={**os.environ, "OMP_NUM_THREADS": "2"})

    def run_solver(self, args, g6):
        proc = self.run_raw(args, g6)
        proc.check_returncode()
        return proc.stdout

    def test_petersen_is_3(self):
        self.assertIn(" c=3 ", self.run_solver(["-c", "4", "-e"], PETERSEN_G6))

    def test_graph6_header_preserves_first_graph(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=repr(newline)):
                graphs = newline.join((">>graph6<<" + PETERSEN_G6, "A_", ""))
                lines = self.run_solver(["-c", "4", "-e"], graphs).splitlines()
                self.assertEqual([line.split()[0] for line in lines], [PETERSEN_G6, "A_"])
                self.assertIn(" c=3 ", lines[0])
                self.assertIn(" c=1 ", lines[1])

    def test_standalone_graph6_header(self):
        lines = self.run_solver(["-c", "4", "-e"], ">>graph6<<\n\n" + PETERSEN_G6).splitlines()
        self.assertEqual(len(lines), 1)
        self.assertIn(" c=3 ", lines[0])

    def test_truncated_or_invalid_graph6_is_rejected(self):
        # A truncated payload, an out-of-range payload character and a bare header must be
        # skipped with a diagnostic instead of being decoded from whatever follows in memory.
        for bad in (PETERSEN_G6[:4], PETERSEN_G6[:-1] + " ", "I"):
            with self.subTest(bad=bad):
                proc = self.run_raw(["-c", "4", "-e"], bad + "\n" + PETERSEN_G6)
                self.assertEqual(proc.returncode, 0)
                self.assertIn("bad g6", proc.stderr)
                lines = proc.stdout.splitlines()
                self.assertEqual(len(lines), 1)
                self.assertIn(" c=3 ", lines[0])

    def test_bad_arguments_are_rejected(self):
        for args in (["-c"], [], ["0"], ["20"], ["-c", "25"], ["-x", "3"]):
            with self.subTest(args=args):
                proc = self.run_raw(args, PETERSEN_G6)
                self.assertEqual(proc.returncode, 2)
                self.assertIn("usage", proc.stderr)
                self.assertEqual(proc.stdout, "")

    def test_robertson_is_4(self):
        with open(os.path.join(DATA, "robertson.g6")) as graph_file:
            g6 = graph_file.read().strip()
        self.assertIn(" c=4 ", self.run_solver(["-c", "5", "-e"], g6))


if __name__ == "__main__":
    unittest.main()
