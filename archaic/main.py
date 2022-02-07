import argparse
import os

from archaic.common.config import Config
from archaic.tracing.tracer import trace



def parse_args():

    parser = argparse.ArgumentParser("themis")
    parser.add_argument("--module", type=str, choices=["trace"], help="functionality to invoke", required=True)
    
    return parser.parse_args()


def main():

    args = parse_args()
    config = Config()
    module = args.module

    if module == "trace":
        
        print("Setting up kernel for tracing...")
        print("sudo sysctl kernel.yama.ptrace_scope=0")
        os.system("sudo sysctl kernel.yama.ptrace_scope=0")

        trace(config=config)

        

if __name__ == '__main__':
    main()

