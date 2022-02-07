
class Config:

    def __init__(self) -> None:
        self.lib_dir = "/opt/libs/"
        self.bin_dir = "/opt/binaries/"
        self.data_dir = "./archaic/data/"
        self.traced_libcalls_file = "./archaic/trace_conf/libc_i_o.txt"
        self.executable = ""
        self.args = ["toth@192.168.1.10", "sleep 5 & uname -a & sleep 5 & uname -a"]

