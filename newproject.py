#!/usr/bin/env python

from pathlib import Path
from sys import argv

# Careful touching this here, the functions rely on position
# =================================================================================
folders: tuple = ("config", "data", "docs", "public", "scripts", "src", "tests")
# 2/docs 3/public 4/scripts 5/src 6/tests

sub_folders: tuple = ("app", "application", "domain", "e2e", "hooks", "infrastructure", "integration", "interfaces", "lib", "styles", "types", "unit", "components", "ui", "layout", "utils", "features")
# 0..16

front_end: tuple = (folders[2], folders[3], folders[5], folders[6])
front_sub: tuple = (sub_folders[0], sub_folders[12], sub_folders[8], sub_folders[4], sub_folders[9], sub_folders[10])
front_comp: tuple = (sub_folders[16], sub_folders[14], sub_folders[13])

full_stack: tuple = (folders[0], folders[2], folders[4], folders[5], folders[6])
full_src: tuple = (sub_folders[1], sub_folders[2], sub_folders[5], sub_folders[7])
full_tests: tuple = (sub_folders[3], sub_folders[6], sub_folders[11])

scripts: tuple = (folders[1], folders[2], folders[4], folders[5], folders[6])
scripts_sub: tuple = (sub_folders[15], sub_folders[16])
# =================================================================================

# List of commands and their associated proyect type.
# Serves only for helping the user.
projects: dict = {
    "mini, script, cli": "Minimal / Scripts / Tiny CLI / Jupyter-heavy",
    "frontend, front, fe": "Frontend / React / Next.js / Vite",
    "backend, back, full, fs": "Standard backend / Full-stack"
}


# Handles invalid inputs
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


def create(name: str, proj: list) -> None:
    [Path(name, i).mkdir(parents=True, exist_ok=True) for i in proj]


def create_sub(name: str, folder: str, proj_sub: list):
    [Path(name, folder, i).mkdir(parents=True, exist_ok=True) for i in proj_sub]


def mini(name: str) -> None:
    print(f"Creating minimal folder structure for script / CLI / Jupyter project '{name}'\n---------")
    create(name, scripts)
    create_sub(name, "src", scripts_sub)


def backend(name: str) -> None:
    print(f"Creating backend/fullstack folder structure for project '{name}'\n---------")
    create(name, full_stack)
    create_sub(name, "src", full_src)
    create_sub(name, "tests", full_tests)


# For projects of kind: "Frontend / React / Next.js / Vite",
def frontend(name: str) -> None:
    print(f"Creating frontend folder structure for project '{name}'\n---------")
    create(name, front_end)
    create_sub(name, "src", front_sub)
    create_sub(name, "src/components", front_comp)
    # folders
    # src, public, tests, docs
    #     sub_folders
    #     src -> app, components, lib, hooks, styles, types
    #     components -> ui, features, layout


def main() -> None:
    flags: list = argv
    if len(flags) < 3:
        error()

    x = flags[(len(flags) - 1)]

    match x.lower():
        case "mini" | "script" | "cli":
            x = " ".join(argv[1:-1])
            mini(x)

        case "frontend" | "front" | "fe":
            x = " ".join(argv[1:-1])
            frontend(x)

        case "backend" | "back" | "full" | "fs":
            x = " ".join(argv[1:-1])
            backend(x)

        case _:
            error()

    print("Job done!")


if __name__ == '__main__':
    main()
