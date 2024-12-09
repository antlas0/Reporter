#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


from src.worker import Worker


if __name__ == "__main__":
    wrk = Worker()
    wrk.setup()
    wrk.run()
