from lilaclib import git_pkgbuild_commit

def pre_build():
  pass

def post_build():
  git_pkgbuild_commit()
