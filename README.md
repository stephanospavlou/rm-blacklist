# rm-blacklist
Python wrapper for rm, checks every argument against
a user maintained blacklist

## Installation
Clone this repository with the command

```
git clone https://github.com/stephanospavlou/rm-blacklist
```

Add the following aliases to your shell

```
alias rm="PATH/TO/rm-blacklist.py"
alias blacklist="PATH/TO/blacklist.py"
```

Finally, in the files ``rm-blacklist.py`` and
``blacklist.py``, edit the value of ``blacklist`` so that
it points (absolute path) to the file ``.blklst``, wherever
you may want to place it in your filesystem.

## Blacklisting files 
There are two ways you can add a file (or directory) to
the blacklist: manually or using the script ``blacklist.py``.
Either way, it's probably best if the first file you blacklist
is ``.blklst``.

### Manually
You can manually edit the file ``.blklst`` and
add the file(s) you want to blacklist. If you blacklist
files manually, place each file on a separate line and
use the file's absolute path. Lines starting with ``#``
will be ignored.

### Using ``blacklist.py``
If you followed the aliasing instructions above, running
the following command will add files to the blacklist:

```
blacklist <file1> <file2> ...
```

## Usage
rm-blacklist allows you to continue removing files as
before. If you attempt however to remove a blacklisted
file, you will receive the following message:

```
Cannot rm <file>: file is blacklisted
```

The program ``rm`` is always called; the arguments passed
are identical to those passed to ``rm-blacklist.py``, minus
those files that are blacklisted.
