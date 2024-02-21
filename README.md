# rm-blacklist
Python wrapper for the POSIX ``rm`` command that checks every argument against a
user maintained blacklist.

## Installation
Clone this repository with the command:

```
git clone https://github.com/stephanospavlou/rm-blacklist
```

Add the following aliases to your shell:

```
alias rm="PATH/TO/rm-blacklist.py"
alias blacklist="PATH/TO/blacklist.py"
```

Then, in the files ``rm-blacklist.py`` and ``blacklist.py``, edit the value of
the constant ``blacklistPath`` so  that it points (absolute path) to the file
``.blklst``, wherever you may want to place it in your filesystem.

And finally, ensure that both ``rm-blacklist.py`` and ``blacklist.py`` are
executable.

## Blacklisting files
### Using ``blacklist.py``
The helper script ``blacklist.py`` can be used to add files (or directories) to
the blacklist. Using it looks like this:

```
blacklist [-r] <file | directory> <file2 | directory> ...
```

The flag ``-r`` is optional: If used, it will blacklist the directory passed
as well as all files (and directories) contained within it recursively. This
flag is only recognized if it is used as the first argument to the script.

Note that blacklisting a directory without using the ``-r`` flag prevents 
deletion of the directory by ``rm`` **but not its contents**. That is:

```
$ blacklist dir
$ rm -rf dir
$ rm-blacklist: either dir or its contents are blacklisted
```
``rm-blacklist`` catches blacklisted directory.

```
$ blacklist dir
$ rm -rf dir/*
$ 
```
``rm-blacklist`` does not prevent the deletion of the contents of
``blacklisted_dir``.

``blacklist.py`` does not check whether or not a file (or directory) has already
been blacklisted before adding it to the blacklist.

### Manually
Alternatively, files can be manually blacklisted. This can be done by placing
the absolute path of each file you wish to blacklist on a separate line in
``.blklst``. Lines starting with ``#`` will be ignored.

Remember: Blacklisting a directory only prevents the deletion of the *directory*
by ``rm``, **not its contents**.
