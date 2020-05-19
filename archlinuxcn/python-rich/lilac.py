from lilaclib import *


def post_build():
    pypi_post_build()
    update_aur_repo()
