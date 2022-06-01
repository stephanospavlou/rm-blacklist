# rm-blacklist
Python wrapper for rm, checking every argument against
a blacklist

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
it points to the file ``.blklst``, wherever you may want
to place it in your filesystem.
