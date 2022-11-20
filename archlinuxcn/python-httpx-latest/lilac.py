from lilaclib import *

def pre_build():
  deps = [
    'sniffio',
    'rfc3986',
    'httpcore-latest',
    'idna',
  ]
  pypi_pre_build(
    pypi_name = 'httpx',
    provides = ['python-httpx'],
    conflicts = ['python-httpx'],
    depends = [f'python-{x}' for x in deps],
    pep517 = True,
    makedepends = ['python-hatchling', 'python-hatch-fancy-pypi-readme'],
    optdepends = [
      'python-h2: HTTP/2 support',
      'python-brotli: decoding for "brotli" compressed responses',
      'python-brotlicffi: decoding for "brotli" compressed responses',
      'python-socksio: SOCKS proxy support',
      'python-click: command line client support',
      'python-rich: command line client support',
      'python-pygments: command line client support',
      'python-trio: alternative async library',
    ],
    prepare = '''\
  sed -i '/certifi/d' pyproject.toml
  sed -e '/import certifi/d' \\
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \\
      -i httpx/_config.py''',
  )

def post_build():
  pypi_post_build()
