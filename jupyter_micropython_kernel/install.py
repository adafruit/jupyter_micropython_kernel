"""
Install the jupyter micropython kernel configuration for this module
"""
import json
import logging
import os
import platform
import subprocess
import sys


logger = logging.getLogger(__name__)


kernel_config = {
    "argv": ["python3", "-m", "jupyter_micropython_kernel", "search", "115200", "-f", "{connection_file}"],
    "display_name": "MicroPython - Serial",
    "language": "micropython"
}


def jupyter_data_directories():
    jupyter_command = os.path.join(os.path.dirname(sys.executable), 'jupyter')
    directories = []
    with subprocess.Popen([jupyter_command, '--paths'], stdout=subprocess.PIPE) as proc:
        in_data = False
        for line in proc.stdout.readlines():
            line = line.decode()
            if not line[0].isspace():
                if line.startswith('data:'):
                    in_data = True
                else:
                    in_data = False
                continue
            if not in_data:
                continue
            directories.append(line.strip())
    return directories


def jupyter_data_directory():
    # Get all config directories
    possible_data_directories = jupyter_data_directories()

    # If running in a virtualenv default to the venv config directory
    venv_dir = os.environ.get('VIRTUAL_ENV', None)
    if venv_dir:
        venv_data_dir = os.path.join(venv_dir, 'share/jupyter')
        if venv_data_dir in possible_data_directories:
            logger.debug('Putting kernel in virtualenv share directory %r', venv_data_dir)
            return venv_data_dir

    return possible_data_directories[0]


def install_kernel():
    kernel_config_directory = os.path.join(jupyter_data_directory(), 'kernels/micropython')
    kernel_config_filename = os.path.join(kernel_config_directory, 'kernel.json')
    if not os.path.exists(kernel_config_directory):
        os.makedirs(kernel_config_directory)

    logger.info('Writing jupyter kernel to %r', kernel_config_filename)
    with open(kernel_config_filename, 'w') as fh:
        json.dump(kernel_config, fh, indent=4, sort_keys=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    install_kernel()
