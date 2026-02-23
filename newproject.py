from pathlib import Path

path = Path()

folders: tuple = ("config", "data", "docs", "public", "scripts", "src", "tests", ".github")

sub_folders: tuple = ("app", "application", "domain", "e2e", "hooks", "integration", "lib", "style", "types", "unit", "infrastructure", "interfaces", "components", "ui", "layout", "utils", "features")

projects: dict = {
    "mini": "Minimal / Script / Tiny CLI / Jupyter-heavy",
    "frontend": "Frontend / React / Next.js / Vite",
    "backend": "Standard backend / full-stack"
}


def mini(name: String):
    print()
    # create folder for project passed by argument
    # create following folders
    # data, docs, scripts, src, tests
    #    create following sub-folders
    #    features, utils
    return print("Job done!")


def backend(name: String):
    print()
    # create folder for project passed by argument
    # create following folders
    # src, tests, config, docs, scripts, .github
    #     sub_folders
    #     src -> application, domain, infrastructure, interfaces
    #     tests -> e2e, integration, unit


def frontend(name: String):
    print()
    # folders
    # src, public, tests, docs, .github
    #     sub_folders
    #     src -> app, components, lib, hooks, styles, types
    #     components -> ui, features, layout


create = True


def main():
    print("Hello! This is a simple script to establish the workspace for your next project.")
    while create is True:
        x: list = input()
        print(x)

        match x:
            case _:
                print("\nPlease input a valid parameter following the next format:\n<project_name> <project_type>\n")
                print("Here's a list of options for types of projects:\n")
                [print(f"{k}: {v}") for k, v in projects.items()]












if __name__ == '__main__':
    main()
