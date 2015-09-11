#hooks
├── hooks
│   ├── pre_gen_project.py
│   └── post_gen_project.py

you should use Python scripts (with extension .py) for your hooks, as these can be run on any platform. However, if you intend for your template to only be run on a single platform, a shell script (or .bat file on Windows) can be a quicker alternative.
