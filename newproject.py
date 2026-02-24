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
    [print(f"\"{k}\" for projects like:\n{v}\n") for k, v in projects.items()]
    print(f"Received: {' '.join(argv)}\n")
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
    flags: list = argv
    if len(flags) < 3:
        error()

    x = flags[(len(flags) - 1)]

    match x.lower():
        case "mini" | "script":
            print("coincidio con mini")
            # mini(argv)

        case "frontend" | "front":
            print("coincidio con frontend")
            # frontend(argv)

        case "backend" | "back" | "full":
            print("coincidio con backend")
            # backend(argv)

        case _:
            error()


if __name__ == '__main__':
    main()
