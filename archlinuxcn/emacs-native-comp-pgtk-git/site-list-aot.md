# ON-DEMAND COMPILATION OF SITE-LISP AND LOCAL PACKAGES

To compile all site-lisp on demand (repos/AUR packages, ELPA, MELPA,
 whatever), add

    (setq comp-deferred-compilation t)

to your `.emacs` file.
