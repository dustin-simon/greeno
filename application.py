print("Hello!")

import core.config.base.base as base

base.initialize()

print("I'm " + base.APPLICATION_NAME + "!")
print("Version: " + base.VERSION)
print("License: " + base.LICENSE)
print("Author: " + base.AUTHOR)
print("Copyright: " + base.COPYRIGHT)
