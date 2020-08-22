from lilaclib import *

def pre_build():
  deps = [
    'aiohttp',
    'babel',
  ]
  pypi_pre_build(
    pypi_name = 'aiogram',
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
    optdepends = [
      'python-aiohttp-socks: support for socks proxy',
    ],
    prepare = '''\
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \\
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \\
      -i aiogram/bot/base.py''',
  )

def post_build():
  pypi_post_build()
