import argparse
import os

from serde.toml import from_toml

from src.common.config import Config
from src.tracing.tracer import trace



def parse_args():

    parser = argparse.ArgumentParser("themis")
    parser.add_argument("--module", type=str, choices=["trace"], help="functionality to invoke", required=True)
    parser.add_argument("--conf", type=str, default="./themis/config.toml", help="set different config file")
    
    return parser.parse_args()


def main():

    args = parse_args()

    conf_path = args.conf

    with open(conf_path, "r") as config_file:
        config = from_toml(Config, config_file.read())

    
    module = args.module
    graph = None

    if module == "trace":
        
        print("Setting up kernel for tracing...")
        print("sudo sysctl kernel.yama.ptrace_scope=0")
        os.system("sudo sysctl kernel.yama.ptrace_scope=0")

        trace(config=config)

        

if __name__ == '__main__':
    main()

