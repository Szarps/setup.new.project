# setup.new.project
Ready for that next project you been thinking about?  Here's a simple python script that will setup the folder structure for that, avoiding tedious setup and giving you some guideline of what goes where. Enjoy!

This was a small tool I made for myself in order to have some base structure of folders for doing bigger stuff in the future. As of today at the moment of posting I am learning some python and this was not just useful but good practice for managing files too!. At any rate, the code is all well commented if you want to edit it to your liking and I think is pretty straightforward.

## How to use
Pretty simple, this is a CLI script, just open your terminal, go to the specific directory of projects (e.g. ~/cool.stuff.code/ and type:
newproject.py <project name> <type>

If you are on linux even better since you can create an alias o throw it in some bin folder and forget about it.

The first flag (your project's name) can take anything a string can handle, you can opt in for "putting the name inside quotes" or not, the script is smart and will create a folder in the current directory your terminal is in with the name of the project and every folder for the kind of stuff you are going to need.

Here's some of the flags for <type>:
- "mini, script, cli": "Minimal / Scripts / Tiny CLI / Jupyter-heavy",
- "frontend, front, fe": "Frontend / React / Next.js / Vite",
- "backend, back, full, fs": "Standard backend / Full-stack"

Don't worry, if you get it wrong you will just get a simple error message, the format for using it and the list above of valid types. If you open it you can even add new ones for your custom needs and tinker around!
