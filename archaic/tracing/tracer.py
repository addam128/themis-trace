from os import system

from common.config import Config
from tracing.frida_trace_wrap import Analyzer
from tracing.filter import filter_file


def trace(config: Config):
    Analyzer(
        config
    ).extract_libcalls()

    filter_file(
        "{}/libcalls_{}.txt".format(config.data_dir, config.executable),
        "{}/libcalls_{}_filtered.txt".format(config.data_dir, config.executable)
    )

    system("rm {}/libcalls_{}.txt".format(config.data_dir, config.executable))