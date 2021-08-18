# Copyright 2020-2021 The MathWorks, Inc.

import json
import os
from setuptools.command.build_py import build_py
from setuptools.command.sdist import sdist
from setuptools.command.install import install
import setuptools
from pathlib import Path
from shutil import which
from jupyter_matlab_proxy.jupyter_config import jupyter_config

tests_require = [
    "pytest",
    "pytest-env",
    "pytest-cov",
    "pytest-mock",
    "pytest-dependency",
    "pytest-aiohttp",
    "requests",
    "psutil",
    "aioresponses",
]

setuptools.setup(
    name="dummy-jupyter",
    version="0.2.0",
    url=jupyter_config["url"],
    author="The MathWorks, Inc.",
    description="MATLAB Web Desktop proxy",
    packages=setuptools.find_packages(exclude=["devel", "tests"]),
    package_dir={"dummy-jupyter": "jupyter_matlab_proxy"},
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    python_requires="~=3.7",
    # TODO: add the matlab_web_desktop under install requires.
    install_requires=["jupyter", "jupyter-server-proxy", "dummy-core"],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={"dev": ["aiohttp-devtools", "black"] + tests_require},
    entry_points={
        "jupyter_serverproxy_servers": ["matlab = jupyter_matlab_proxy:setup_matlab"],
        "matlab_web_desktop_proxy_configs": [
            "jupyter_config = jupyter_matlab_proxy.jupyter_config:jupyter_config"
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
