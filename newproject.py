#!/usr/bin/env python

from pathlib import Path
from sys import argv

# shorthand command for defining starting route
path = Path.cwd()

# Careful touching this here, the functions rely on position
# =================================================================================
folders: tuple = ["config", "data", "docs", "public", "scripts", "src", "tests", ".github"]
# 2/docs 3/public 4/scripts 5/src 6/tests

sub_folders: tuple = ["app", "application", "domain", "e2e", "hooks", "integration", "lib", "style", "types", "unit", "infrastructure", "interfaces", "components", "ui", "layout", "utils", "features"]  # 0..16

front_end: list = [folders[2], folders[3], folders[5], folders[6]]

full_stack: list = [folders[0], folders[2], folders[4], folders[5], folders[6]]

scripts: list = [folders[1], folders[2], folders[4], folders[5], folders[6]]

# =================================================================================

# List of commands and their associated proyect type.
# Serves only for helping the user.
projects: dict = {
    "mini": "Minimal / Scripts / Tiny CLI / Jupyter-heavy",
    "frontend": "Frontend / React / Next.js / Vite",
    "backend": "Standard backend / Full-stack"
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


def proj_name(a: list) -> str:
    a.pop()
    a.pop(0)
    b: str = " ".join(a)
    return b


# For projects of kind: "Minimal / Scripts / Tiny CLI / Jupyter-heavy"
def mini(name: str):
    print(f"Creating folder structure for minimal / script / CLI / Jupyter project {name}\n")
    print(f"{front_end}")
    # create folder for project passed by argument
    # create following folders
    # data, docs, scripts, src, tests
    #    create following sub-folders
    #    features, utils


# For projects of kind: "Standard backend / Full-stack"
def backend(name: str):
    print(f"Creating backend/fullstack folder structure for project named {name}\n")

    # Definimos la ruta base (donde estás parado + nombre del proyecto)
    base = Path(name)
    # print(f"{base} type {type(base)}")
    base.mkdir()
    # [print(f"{i}]") for i in Path.cwd().iterdir()]

    # Definimos una subcarpeta (usando el operador / que pathlib entiende)
    # sub = base / "src" / "application", base / "src" / "domain" / "infrastructure" / "interfaces"
    # print(f"{sub}")

    # Creamos todo de una
    # sub.mkdir(parents=True, exist_ok=True)
    # [print(f"{i}\n") for i in sub.iterdir()]

    # create folder for project passed by argument
    # src, tests, config, docs, scripts, .github
    #     sub_folders
    #     src -> application, domain, infrastructure, interfaces
    #     tests -> e2e, integration, unit


# For projects of kind: "Frontend / React / Next.js / Vite",
def frontend(name: str):
    print(f"Creating frontend folder structure for project {name}\n")
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
        case "mini" | "script" | "cli":
            print("coincidio con mini")
            x = proj_name(flags)
            mini(x)

        case "frontend" | "front" | "fe":
            print("coincidio con frontend")
            x = proj_name(flags)
            frontend(x)

        case "backend" | "back" | "full" | "fs":
            print("coincidio con backend")
            x = proj_name(flags)
            backend(x)

        case _:
            error()

    print("Job done!")


if __name__ == '__main__':
    main()
