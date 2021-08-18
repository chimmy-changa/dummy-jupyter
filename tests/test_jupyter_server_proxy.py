import os, inspect

import matlab_web_desktop_proxy
import jupyter_matlab_proxy
from pathlib import Path
from matlab_web_desktop_proxy import mwi_environment_variables as mwi_env


def test_get_env():
    port = 10000
    base_url = "foo/"
    actual_env_config = jupyter_matlab_proxy._get_env(port, base_url)

    expected_env_config = {
        mwi_env.get_env_name_app_port(): str(port),
        mwi_env.get_env_name_base_url(): f"{base_url}matlab",
        mwi_env.get_env_name_app_host(): "127.0.0.1",
        mwi_env.get_env_name_mhlm_context(): "MATLAB_JUPYTER",
    }

    assert actual_env_config == expected_env_config


def test_setup_matlab():
    """Tests for a valid Server Process Configuration Dictionary

    This test checks if the jupyter proxy returns the expected Server Process Configuration
    Dictionary for the Matlab process.
    """
    # Setup
    # port = 10000
    # base_url = "foo/"
    package_path = Path(inspect.getfile(matlab_web_desktop_proxy)).parent
    icon_path = str(package_path / "icons" / "matlab.svg")

    expected_matlab_setup = {
        "command": ["matlab-web-desktop-app", "--config", "jupyter_config"],
        "timeout": 100,
        "environment": jupyter_matlab_proxy._get_env,
        "absolute_url": True,
        "launcher_entry": {
            "title": "MATLAB",
            "icon_path": icon_path,
        },
    }

    actual_matlab_setup = jupyter_matlab_proxy.setup_matlab()

    assert expected_matlab_setup == actual_matlab_setup
    assert os.path.isfile(actual_matlab_setup["launcher_entry"]["icon_path"])
