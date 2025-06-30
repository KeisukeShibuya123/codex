import argparse
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def setup_logging(logfile: str) -> None:
    """Configure logging to file and stdout."""
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(logfile, encoding="utf-8")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)


def main(args: argparse.Namespace) -> None:
    """Main entry point."""
    logger.info("Start program with args: %s", args)
    try:
        logger.info("Processing...")
        # ... add application logic here ...
        logger.info("Done.")
    except Exception:
        logger.exception("Unhandled exception occurred")
        raise  # Re-raise if needed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample application")
    parser.add_argument("foo", help="Positional argument")
    parser.add_argument("--log", default="app.log", help="Log file name")
    parsed = parser.parse_args()
    setup_logging(parsed.log)
    main(parsed)
