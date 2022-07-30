"""
set up default logging
"""

from pathlib import Path
import os
import sys

from loguru import logger

# filepath

LOG_DIR_PATH = Path.cwd() / "{{cookicutter.package_name}}_logs"
LOG_DIR_PATH.mkdir(exist_ok=True)

base_name = {{cookicutter.package_name}}
{% raw -%}
LOG_PATH = LOG_DIR_PATH / f"_{base_name}_{{time}}.log"
{% endraw -%}

# remove default handlers
logger.remove()

logger.add(sys.stdout,format={"{time}_{message}"}, level="DEBUG",colorized=True)
logger.add(LOG_PATH,serialize=True,rotation="50 MB")