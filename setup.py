"""Setup for {{cookiecutter.repo_name}}XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='{{cookiecutter.repo_name}}-xblock',
    version='0.1',
    author="wwj718",
    author_email="wuwenjie718@gmail.com",
    description='XBlock to use {{cookiecutter.repo_name}}',
    packages=[
        '{{cookiecutter.repo_name}}',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            '{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}:{{cookiecutter.repo_name}}XBlock',
        ]
    },
    package_data=package_data("{{cookiecutter.repo_name}}", "static"),
)
