"""module with utils functions"""
import os
import argparse


def server_args_parser():
    """args parser for server"""
    parser = argparse.ArgumentParser(description='server_args')

    default = os.path.dirname(os.path.abspath(__file__))

    parser.add_argument('--searchpath',
                        type=str,
                        default=default,
                        help='search path')
    args = parser.parse_args()
    return args
