Terminfo Entries
================

:Author: Sebastian J. Bronner <waschtl@sbronner.com>
:Date: 2023-02-12
:URL: https://aur.archlinux.org/packages/st

The Problem
-----------

Most Linux-based distributions will have their terminfo entries in the
``ncurses`` package. These live in ``/usr/share/terminfo``. There you will find
several entries for ``st``. Up until ``ncurses-6.1`` as packaged in ArchLinux,
these, did not work well with then-current versions of ``st``.

Specifically, I have observed the following issues when using the terminfo
entries supplied with those versions of ``ncurses``:

* Start ``st``.
* Run ``tmux`` in the ``st`` window.
* Run ``nvim`` in ``tmux``.

  * ``tmux`` will crash immediately with the following message:

    .. code:: console

       [lost server]
                    %

* Run ``w3m`` with any URL in ``tmux``.

  * ``w3m`` will not react to any key presses (most notably the arrow keys and
    ``q``) and must be terminated with ``killall w3m``.
  * The command line returned where ``w3m`` was running will show all the
    missing keypresses.

For reference, I performed these tests using the following software versions:
``st`` 0.8.2, ``tmux`` 2.9_a, ``neovim`` 0.4.2, and ``w3m``
0.5.3.git20190105-1.

The Workaround
--------------

The affected versions of all software packages have since been updated and the
issue has been resolved. However, when connecting to older remote systems using
``ssh`` in ``st``, those remote systems may still be affected. In those cases,
it would help to copy over ``st``'s terminfo file and generate user-level
terminfo entries:

.. code:: shell

   rsync /usr/share/st/st.info <remote>:
   ssh <remote> tic -sx st.info

The generated terminfo database will most likely be placed in ``~/.terminfo``.
The command will print the actual location used. Unfortunately, these files
need to be kept up to date by hand. Actually they should probably be removed as
soon as a new version of ``ncurses`` is installed on the remote system.
