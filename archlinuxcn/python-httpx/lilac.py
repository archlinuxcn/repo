from lilaclib import *

def pre_build():
  deps = [
    'urllib3', 'h11', 'h2', 'chardet', 'hstspreload', 'idna',
    'rfc3986', 'sniffio',
  ]
  pypi_pre_build(
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
    optdepends = ['python-brotlipy: decoding for "brotli" compressed responses'],
    prepare = '''\
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \\
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \\
      -i httpx/config.py''',
  )

def post_build():
  pypi_post_build()
  update_aur_repo()
