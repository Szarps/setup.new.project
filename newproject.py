#!/usr/bin/env python

from pathlib import Path
from sys import argv

path = Path()

folders: tuple = ("config", "data", "docs", "public", "scripts", "src", "tests", ".github")

sub_folders: tuple = ("app", "application", "domain", "e2e", "hooks", "integration", "lib", "style", "types", "unit", "infrastructure", "interfaces", "components", "ui", "layout", "utils", "features")

projects: dict = {
    "mini": "Minimal / Scripts / Tiny CLI / Jupyter-heavy",
    "frontend": "Frontend / React / Next.js / Vite",
    "backend": "Standard backend / Full-stack"
}


def error() -> None:
    print(
        "\nPlease input a valid parameter following the next "
        "format:\n<project name> <project type> (spaces are valid too!)\n"
    )
    print("Here's a list of options for types of projects:\n")
    [print(f"{k}: {v}") for k, v in projects.items()]
    print(f"\nReceived: {' '.join(argv)}\n")
    print("Failed to get valid input, exiting.")
    exit()


def mini(name: str):
    print()
    # create folder for project passed by argument
    # create following folders
    # data, docs, scripts, src, tests
    #    create following sub-folders
    #    features, utils
    return print("Job done!")


def backend(name: str):
    print()
    # create folder for project passed by argument
    # create following folders
    # src, tests, config, docs, scripts, .github
    #     sub_folders
    #     src -> application, domain, infrastructure, interfaces
    #     tests -> e2e, integration, unit


def frontend(name: str):
    print()
    # folders
    # src, public, tests, docs, .github
    #     sub_folders
    #     src -> app, components, lib, hooks, styles, types
    #     components -> ui, features, layout


def main():
    if len(argv) < 3:
        error()

    print(argv)


if __name__ == '__main__':
    main()
