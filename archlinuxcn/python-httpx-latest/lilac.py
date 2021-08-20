from lilaclib import *

def pre_build():
  deps = [
    'charset-normalizer',
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
    depends_setuptools = False,
    optdepends = [
      'python-h2: HTTP/2 support',
      'python-brotli: decoding for "brotli" compressed responses',
      'python-brotlicffi: decoding for "brotli" compressed responses',
    ],
    prepare = '''\
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \\
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \\
      -i httpx/_config.py''',
  )

def post_build():
  pypi_post_build()
