from lilaclib import *

def pre_build():
  deps = [
    'h11', 'h2', 'sniffio',
  ]
  pypi_pre_build(
    pypi_name = 'httpcore',
    provides = ['python-httpcore'],
    conflicts = ['python-httpcore'],
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
