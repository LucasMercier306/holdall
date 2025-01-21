import fire
from rbk_ctl.module.core import Core


def main():
    """Point d'entrée CLI pour rbk-ctl."""
    fire.Fire(Core)