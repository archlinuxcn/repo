from lilaclib import *

def pre_build():
  deps = ['aiosasl', 'aioopenssl', 'babel', 'dnspython', 'lxml', 'multidict', 'sortedcollections', 'pyopenssl', 'pyasn1', 'pyasn1-modules', 'tzlocal']
  pypi_pre_build(
    pypi_name = 'aioxmpp',
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
  )

def post_build():
  pypi_post_build()
