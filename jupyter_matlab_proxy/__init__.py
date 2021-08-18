# Copyright 2020-2021 The MathWorks, Inc.

import inspect
import matlab_web_desktop_proxy
from pathlib import Path
from matlab_web_desktop_proxy import mwi_environment_variables as mwi_env


def _get_env(port, base_url):
    return {
        mwi_env.get_env_name_app_port(): str(port),
        mwi_env.get_env_name_base_url(): f"{base_url}matlab",
        mwi_env.get_env_name_app_host(): "127.0.0.1",
        mwi_env.get_env_name_mhlm_context(): "MATLAB_JUPYTER",
    }


def setup_matlab():
    package_path = Path(inspect.getfile(matlab_web_desktop_proxy)).parent
    icon_path = package_path / "icons" / "matlab.svg"

    return {
        "command": ["matlab-web-desktop-app", "--config", "jupyter_config"],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {"title": "MATLAB", "icon_path": str(icon_path)},
    }
