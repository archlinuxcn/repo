from lilaclib import *

depends = [
  ('rust-nightly', 'rust-std-nightly-x86_64-unknown-linux-gnu'),
  ('rust-nightly', 'rust-nightly'),
  ('rust-nightly', 'cargo-nightly'),
]

pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
