#!/bin/bash

set -e

# get SSH server started
/usr/sbin/sshd -D &

# get jupyter running
jupyter lab --port "&{JUPYTER_PORT}" --ip 0.0.0.0 --no-browser --config /root/.jupyter/jupyter_notegook_config.py