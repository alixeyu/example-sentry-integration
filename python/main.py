import argparse
import logging
import os

import sentry_sdk

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if os.environ.get("DSN", ""):
    logger.info("Set up Sentry...")
    sentry_sdk.init(dsn=os.environ.get("DSN"),
                    environment="development",
                    traces_sample_rate=1.0)


def div(x, y):
    logger.info(f"Divide {y} into {x}")
    return x / y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="div", usage="python main.py x y")
    parser.add_argument("x", action="store", default=0, type=int)
    parser.add_argument("y", action="store", default=0, type=int)

    args = parser.parse_args()
    print(div(args.x, args.y))
