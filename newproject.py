#!/usr/bin/env python

from pathlib import Path
from sys import argv

# shorthand command for defining starting route
path = Path.cwd()

# Careful touching this here, the functions rely on position
# =================================================================================
folders: tuple = ("config", "data", "docs", "public", "scripts", "src", "tests", ".github")

sub_folders: tuple = ("app", "application", "domain", "e2e", "hooks", "integration", "lib", "style", "types", "unit", "infrastructure", "interfaces", "components", "ui", "layout", "utils", "features")
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
    print(f"Creating folder structure for minimal / script / CLI / Jupyter project {name}")
    # create folder for project passed by argument
    # create following folders
    # data, docs, scripts, src, tests
    #    create following sub-folders
    #    features, utils


# For projects of kind: "Standard backend / Full-stack"
def backend(name: str):
    print(f"Creating backend/fullstack folder structure for project named {name}")

    # Definimos la ruta base (donde estás parado + nombre del proyecto)
    base = path / name
    print(f"{base.absolute()}")

    # Definimos una subcarpeta (usando el operador / que pathlib entiende)
    sub = base / "src", base / "assests"
    print(f"{sub.absolute()}")

    # Creamos todo de una
    # sub.mkdir(parents=True, exist_ok=True)

    # create folder for project passed by argument
    # create following folders
    # src, tests, config, docs, scripts, .github
    #     sub_folders
    #     src -> application, domain, infrastructure, interfaces
    #     tests -> e2e, integration, unit


# For projects of kind: "Frontend / React / Next.js / Vite",
def frontend(name: str):
    print(f"Creating frontend folder structure for project {name}")
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
