print("Hello!")

import core.config.base.base as base_config
import core.config.sys.sys as sys_config

def print_base_config():
    print("I'm " + base_config.APPLICATION_NAME + "!")
    print("Version: " + base_config.VERSION)
    print("License: " + base_config.LICENSE)
    print("Author: " + base_config.AUTHOR)
    print("Copyright: " + base_config.COPYRIGHT)

base_config.initialize()
print_base_config()
