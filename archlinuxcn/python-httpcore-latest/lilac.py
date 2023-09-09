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
    pep517 = True,
    makedepends = ['python-hatchling', 'python-hatch-fancy-pypi-readme'],
    optdepends = [
      'python-h2: HTTP/2 support',
      'python-socksio: for SOCKS support',
      'python-trio: for trio backend',
    ],
  )

def post_build():
  pypi_post_build()
