import argparse
import os

from common.config import Config
from tracing.tracer import trace



def parse_args():

    parser = argparse.ArgumentParser("themis")
    parser.add_argument("--pid", type=int, help="Pid if process was started separately")
    
    return parser.parse_args()


def main():

    args = parse_args()
    config = Config()
    pid = args.pid
        
    print("Setting up kernel for tracing...")
    print("sudo sysctl kernel.yama.ptrace_scope=0")
    #os.system("sudo sysctl kernel.yama.ptrace_scope=0") -- docker does not need this

    trace(config=config, pid=pid)

        

if __name__ == '__main__':
    main()

