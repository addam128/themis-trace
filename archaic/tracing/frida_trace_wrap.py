import subprocess
import os

from common.config import Config

class Analyzer:

    def __init__(self, config) -> None:

        self.config = config
        self._exec_path = "{}/{}".format(config.bin_dir, config.executable)

        self._traced_functions = set()
        self._load_function_names(config.traced_libcalls_file)

    def _spawn_target(self):
        changed_env = os.environ.copy()
        changed_env["LD_LIBRARY_PATH"] = self.config.lib_dir
        proc = subprocess.Popen(
            [self._exec_path, *self.config.args],
            env=changed_env
        )
        return proc

    def _attach_trace(self, pid: int, outname: str):
        # simply via bash atm, as we dont want to reimplement frida-trace

        cmd = ["frida-trace"]
        for function in self._traced_functions:
            cmd.append("-i")
            cmd.append(function.strip())
        cmd.append("-p")
        cmd.append("{}".format(pid))

        print(' '.join(cmd))
        with open(outname, "w") as file:
            trace_process = subprocess.Popen(
                cmd,
                stdout=file,
                stdin=subprocess.DEVNULL
            )
            return trace_process

    def extract_libcalls(self, pid):

        if pid is None:
            proc = self._spawn_target()
            pid = proc.pid
        self._attach_trace(pid, "{}/libcalls_{}.txt".format(self.config.data_dir, self.config.executable))

    def _load_function_names(self, filename):

        with open(filename, "r") as file:
            for line in file:
                self._traced_functions.add(line)


