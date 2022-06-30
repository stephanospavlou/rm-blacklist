# rm-blacklist
Python wrapper for the Unix (*at the least the GNU*)
``rm`` command which checks every argument
to the command against a user maintained blacklist.

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

Finally, in the files ``rm-blacklist.py`` and
``blacklist.py``, edit the value of ``blacklist`` so that
it points (absolute path) to the file ``.blklst``, wherever
you may want to place it in your filesystem.

## Blacklisting files 
There are two ways you can add a file (or directory) to
the blacklist: manually or by using the script ``blacklist.py``.
Either way, it's probably best if the first file you blacklist
is ``.blklst`` itself.

### Manually
You can manually edit the file ``.blklst`` and
add the file(s) you want to blacklist. If you blacklist
files manually, place each file on a separate line and
use the file's absolute path. Lines starting with ``#``
will be ignored.

### Using ``blacklist.py``
The script ``blacklist.py`` automates the process and 
tries to make your life easier (especially when blacklisting
all of the files in a directory recursively). If you followed 
the aliasing instructions above, running
the following command will blacklist the passed files:

```
blacklist [-r] <file1> <file2> ...
```

The option ``-r`` is optional: if used, it will blacklist the 
directory passed as well as all other files (and directories)
contained within it recursively. This option is only recognized
if it is the first argument to ``blacklist.py``. If you are
attempting to blacklist a file that is literally named ``-r``,
you can do so by just not passing it as the first argument.

## Usage
**rm-blacklist** allows you to go on removing files as
before, probably without you even realizing it's there most
of the time. If you attempt however to remove a file you have
blacklisted, you will receive the following message:

```
Cannot rm <file>: file is blacklisted
```

The program ``rm`` is always called unless all of the arguments
are blacklisted; the arguments passed are identical to those
passed to ``rm-blacklist.py`` (although maybe in a different
order), minus those files that are blacklisted.
