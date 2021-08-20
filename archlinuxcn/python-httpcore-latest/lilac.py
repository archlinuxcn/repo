from lilaclib import *

def pre_build():
  deps = [
    'h11', 'sniffio', 'anyio',
  ]
  pypi_pre_build(
    pypi_name = 'httpcore',
    provides = ['python-httpcore'],
    conflicts = ['python-httpcore'],
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
    optdepends = [
      'python-h2: HTTP/2 support',
    ],
  )

def post_build():
  pypi_post_build()
