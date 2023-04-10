# ON-DEMAND COMPILATION OF SITE-LISP AND LOCAL PACKAGES

To compile all site-lisp on demand (repos/AUR packages, ELPA, MELPA,
 whatever), add

    (setq native-comp-deferred-compilation t)

to your `.emacs` file.

Or search the option in the editor's GUI configuration, set it
to true and save your `.emacs` file to add it to the file's
`custom-set-variables` array automatically.

