import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from lilaclib import *

# 本地测试用
# from types import SimpleNamespace
# _G = SimpleNamespace(newver='v0.1.47')

_repo = "https://github.com/jswysnemc/mark-shot"


def _run(cmd, **kwargs):
    proc = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    if proc.returncode != 0:
        raise RuntimeError(f"{Path(cmd[0]).name} failed:\n{proc.stdout}{proc.stderr}")
    return proc


def pre_build():
    tag = _G.newver
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        out = Path(tmp) / "aur-work"
        _run(["git", "clone", "--quiet", "--depth", "1", "--branch", tag,
              f"{_repo}.git", str(repo)])
        _run([sys.executable, "scripts/packaging/prepare_aur.py",
              "--tag", tag, "--source-sha", tag, "--output", str(out)], cwd=repo)
        shutil.copyfile(out / "PKGBUILD", "PKGBUILD")

    # 构建机的 rustc 默认用 lld 链接，读不懂 makepkg 的 -flto 给 cc crate 编出的
    # GCC LTO 对象（libspa-sys / onig_sys），链接时报符号未定义。关掉 C 侧 LTO 即可，
    # 与上游对自家 C/汇编用 -fno-lto 的做法一致；Rust 侧的 lto="thin" 不受影响。
    # 上游给三个构建脚本的默认并行度都是 2，专用构建机上按核数压满。
    with open("PKGBUILD", "a") as f:
        f.write("\noptions+=('!lto')\n")
        f.write('export MARK_SHOT_BUILD_JOBS="${MARK_SHOT_BUILD_JOBS:-$(nproc)}"\n')


def post_build():
    git_add_files(["PKGBUILD"])
    git_commit()
