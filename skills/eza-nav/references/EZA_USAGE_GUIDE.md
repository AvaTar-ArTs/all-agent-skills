# eza Usage Guide

Last updated: 2026-05-18 07:57:38

## Purpose

`eza` is installed at `/usr/local/bin/eza` and should be used instead of `ls` for directory listings in this workspace.

Version discovered locally:

```text
Version:
eza - A modern, maintained replacement for ls
v0.23.4 [+git]
https://github.com/eza-community/eza
```

## Core Rule

Use `eza` for listing files and directories. Avoid `ls`.

## Common Replacements

| Old intent | Use |
|---|---|
| basic listing | `eza /path` |
| long listing | `eza -l /path` |
| include hidden files | `eza -la /path` |
| one entry per line | `eza -1 /path` |
| inspect directory itself, not contents | `eza -ld /path` |
| tree view | `eza -T /path` |
| tree with depth | `eza -T -L 2 /path` |
| sort by size | `eza -la --sort=size /path` |
| sort newest first | `eza -la --sort=modified --reverse /path` |
| directories first | `eza -la --group-directories-first /path` |
| show symlink targets | `eza -la --show-symlinks /path` |
| show macOS/BSD flags | `eza -laO /path` |
| show Git status | `eza -la --git /path` |
| ignore gitignored files | `eza -la --git-ignore /path` |

## Best Everyday Commands

### Clean long listing

```bash
eza -lah --group-directories-first ~/.gemini
```

### Hidden files plus symlink targets

```bash
eza -lah --show-symlinks ~/.gemini
```

### Tree, limited depth

```bash
eza -T -L 2 --group-directories-first ~/.gemini
```

### Tree with hidden files

```bash
eza -Ta -L 2 --group-directories-first ~/.gemini
```

### Directory itself, not contents

```bash
eza -ld ~/.gemini ~/.gemini-vanilla ~/.ai-platforms
```

### Git-aware listing

```bash
eza -lah --git --group-directories-first ~/.ai-platforms
```

### Size audit

```bash
eza -lah --sort=size --reverse ~/.gemini
```

### Recent files first

```bash
eza -lah --sort=modified --reverse ~/.gemini/docs
```

## Useful Display Options

### `-l`, `--long`

Extended metadata table.

```bash
eza -l /path
```

### `-a`, `--all`

Show hidden dotfiles.

```bash
eza -la /path
```

### `-T`, `--tree`

Tree view.

```bash
eza -T /path
```

### `-L`, `--level`

Limit recursion depth. Very useful to avoid huge output.

```bash
eza -T -L 3 /path
```

### `--group-directories-first`

Keeps directories above files.

```bash
eza -la --group-directories-first /path
```

### `--icons=auto`

Show icons when supported.

```bash
eza -la --icons=auto /path
```

### `--absolute=on`

Display absolute paths.

```bash
eza -1 --absolute=on /path
```

### `--show-symlinks`

Explicitly display symlink information.

```bash
eza -la --show-symlinks /path
```

### `-O`, `--flags`

Show file flags on macOS/BSD.

```bash
eza -laO /path
```

### `-@`, `--extended`

Show extended attributes.

```bash
eza -la@ /path
```

## Sorting

Valid sort fields from local help include:

```text
name, Name, extension, Extension, size, type, created, modified, accessed, changed, inode, none
```

Examples:

```bash
eza -la --sort=size --reverse /path

eza -la --sort=modified --reverse /path

eza -la --sort=extension /path

eza -la --sort=type /path
```

## Filtering

### Only directories

```bash
eza -laD /path
```

### Only files

```bash
eza -laf /path
```

### Ignore globs

```bash
eza -la --ignore-glob='node_modules|.git|tmp|logs' /path
```

### Git ignored files hidden

```bash
eza -la --git-ignore /path
```

## Git Integration

### Show Git status next to files

```bash
eza -la --git ~/.ai-platforms
```

### Show Git repo info

```bash
eza -la --git-repos ~
```

### Faster repo branch-only view

```bash
eza -la --git-repos-no-status ~
```

## Time Formatting

### Created time

```bash
eza -la --created /path
```

### Accessed time

```bash
eza -la --accessed /path
```

### Modified time with ISO style

```bash
eza -la --time-style=long-iso /path
```

### Custom time format

```bash
eza -la --time-style='+%Y-%m-%d %H:%M' /path
```

## Recommended Commands for This Workspace

### Review Gemini docs

```bash
eza -lah --sort=modified --reverse ~/.gemini/docs
```

### Review Gemini top level safely

```bash
eza -lah --group-directories-first ~/.gemini
```

### Review hidden Gemini runtime folders

```bash
eza -lah --group-directories-first ~/.gemini/.history ~/.gemini/logs ~/.gemini/tmp
```

### Review `.ai-platforms` without expanding everything

```bash
eza -lah --git --group-directories-first ~/.ai-platforms
```

### Tree view of `.ai-platforms`, depth 2

```bash
eza -Ta -L 2 --group-directories-first ~/.ai-platforms
```

### Inspect backup sizes visually

```bash
eza -lah --sort=size --reverse ~/.ai-platforms/backups
```

### Inspect iTerm2 Gemini findings

```bash
eza -lah --sort=modified --reverse ~/.gemini/docs/ITERM2_GEMINI_EXPLORATION.md
```

## Safe Patterns for Large Directories

Avoid unconstrained recursive listings on huge trees. Prefer depth limits:

```bash
eza -T -L 2 ~/iterm2
```

or use `find` for targeted searches:

```bash
find ~/iterm2 -iname '*gemini*' -print
```

## Notes

`eza` is for presentation/listing. For scripting and exact existence checks, still use tools like:

```bash
test -e /path
stat /path
find /path -maxdepth 1 -print
du -sh /path
file /path
readlink /path
```

## Local Help Reference Excerpt

```text
Version:
eza - A modern, maintained replacement for ls
v0.23.4 [+git]
https://github.com/eza-community/eza

Help full:
Usage:
  eza [options] [files...]

META OPTIONS
  -?, --help                 show list of command-line options
  -v, --version              show version of eza

DISPLAY OPTIONS
  -1, --oneline              display one entry per line
  -l, --long                 display extended file metadata as a table
  -G, --grid                 display entries as a grid (default)
  -x, --across               sort the grid across, rather than downwards
  -R, --recurse              recurse into directories
  -T, --tree                 recurse into directories as a tree
  -X, --dereference          dereference symbolic links when displaying information
  -F, --classify=WHEN        display type indicator by file names (always, auto, never)
  --colo[u]r=WHEN            when to use terminal colours (always, auto, never)
  --colo[u]r-scale           highlight levels of 'field' distinctly(all, age, size)
  --colo[u]r-scale-mode      use gradient or fixed colors in --color-scale (fixed, gradient)
  --icons=WHEN               when to display icons (always, auto, never)
  --no-quotes                don't quote file names with spaces
  --hyperlink                display entries as hyperlinks
  --absolute                 display entries with their absolute path (on, follow, off)
  --follow-symlinks          drill down into symbolic links that point to directories
  -w, --width COLS           set screen width in columns


FILTERING AND SORTING OPTIONS
  -a, --all                  show hidden and 'dot' files. Use this twice to also
                             show the '.' and '..' directories
  -A, --almost-all           equivalent to --all; included for compatibility with `ls -A`
  -d, --treat-dirs-as-files  list directories as files; don't list their contents
  -D, --only-dirs            list only directories
  -f, --only-files           list only files
  --show-symlinks            explicitly show symbolic links (for use with --only-dirs | --only-files)
  --no-symlinks              do not show symbolic links
  -L, --level DEPTH          limit the depth of recursion
  -r, --reverse              reverse the sort order
  -s, --sort SORT_FIELD      which field to sort by
  --group-directories-first  list directories before other files
  --group-directories-last   list directories after other files
  -I, --ignore-glob GLOBS    glob patterns (pipe-separated) of files to ignore
  --git-ignore               ignore files mentioned in '.gitignore'
  Valid sort fields:         name, Name, extension, Extension, size, type,
                             created, modified, accessed, changed, inode, and none.
                             date, time, old, and new all refer to modified.

LONG VIEW OPTIONS
  -b, --binary               list file sizes with binary prefixes
  -B, --bytes                list file sizes in bytes, without any prefixes
  -g, --group                list each file's group
  --smart-group              only show group if it has a different name from owner
  -h, --header               add a header row to each column
  -H, --links                list each file's number of hard links
  -i, --inode                list each file's inode number
  -M, --mounts               show mount details (Linux and Mac only)
  -n, --numeric              list numeric user and group IDs
  -O, --flags                list file flags (Mac, BSD, and Windows only)
  -S, --blocksize            show size of allocated file system blocks
  -t, --time FIELD           which timestamp field to list (modified, accessed, created)
  -m, --modified             use the modified timestamp field
  -u, --accessed             use the accessed timestamp field
  -U, --created              use the created timestamp field
  --changed                  use the changed timestamp field
  --time-style               how to format timestamps (default, iso, long-iso,
                             full-iso, relative, or a custom style '+<FORMAT>'
                             like '+%Y-%m-%d %H:%M')
  --total-size               show the size of a directory as the size of all
                             files and directories inside (unix only)
  -o, --octal-permissions    list each file's permission in octal format
  --no-permissions           suppress the permissions field
  --no-filesize              suppress the filesize field
  --no-user                  suppress the user field
  --no-time                  suppress the time field
  --stdin                    read file names from stdin, one per line or other separator 
                             specified in environment
  --git                      list each file's Git status, if tracked or ignored
  --no-git                   suppress Git status (always overrides --git,
                             --git-repos, --git-repos-no-status)
  --git-repos                list root of git-tree status
  --git-repos-no-status      list each git-repos branch name (much faster)
    
  -@, --extended             list each file's extended attributes and sizes
  -Z, --context              list each file's security context

Man availability:
eza(1)			    General Commands Manual			eza(1)

NAME
       eza — a modern replacement for ls

SYNOPSIS
       eza [options] [files...]

       eza is a modern replacement for ls.  It uses colours for information by
       default, helping you distinguish between many types of files, such as
       whether you are the owner, or in the owning group.

       It also has extra features not present in the original ls, such as
       viewing the Git status for a directory, or recursing into directories
       with a tree view.

EXAMPLES
       eza    Lists the contents of the current directory in a grid.

       eza --oneline --reverse --sort=size
	      Displays a list of files with the largest at the top.

       eza --long --header --inode --git
	      Displays a table of files with a header, showing each file’s
	      metadata, inode, and Git status.

       eza --long --tree --level=3
	      Displays a tree of files, three levels deep, as well as each
	      file’s metadata.

META OPTIONS
       --help Show list of command-line options.

       -v, --version
	      Show version of eza.

DISPLAY OPTIONS
       -1, --oneline
	      Display one entry per line.

       --absolute=WHEN
	      Display entries with their absolute path.

       Valid settings are `on', `follow', and `off'.  When used without a
       value, defaults to `on'.

       `on': Show absolute paths for all entries.  `follow': Show absolute
       paths and resolve symbolic links to their targets.  `off': Show
       relative paths (default behavior).

       -F, --classify=WHEN
	      Display file kind indicators next to file names.

       Valid settings are ‘always’, ‘automatic’ (or ‘auto’ for short), and
       ‘never’.  When used without a value, defaults to ‘automatic’.

       automatic or auto will display file kind indicators only when the
       standard output is connected to a real terminal.  If eza is ran while
       in a tty, or the output of eza is either redirected to a file or piped
       into another program, file kind indicators will not be used.  Setting
       this option to ‘always’ causes eza to always display file kind
       indicators, while ‘never’ disables the use of file kind indicators.

       -G, --grid
	      Display entries as a grid (default).

       -l, --long
	      Display extended file metadata as a table.

       -R, --recurse
	      Recurse into directories.

       -T, --tree
	      Recurse into directories as a tree.

       --follow-symlinks
	      Drill down into symbolic links that point to directories.

       -X, --dereference
	      Dereference symbolic links when displaying information.

       -x, --across
	      Sort the grid across, rather than downwards.

       --color=WHEN, --colour=WHEN
	      When to use terminal colours (using ANSI escape code to colorize
	      the output).

       Valid settings are ‘always’, ‘automatic’ (or ‘auto’ for short), and
       ‘never’.  When used without a value, defaults to ‘automatic’.

       The default behavior (‘automatic’ or ‘auto’) is to colorize the output
       only when the standard output is connected to a real terminal.  If the
       output of eza is redirected to a file or piped into another program,
       terminal colors will not be used.  Setting this option to ‘always’
       causes eza to always output terminal color, while ‘never’ disables the
       use of terminal color.

       Manually setting this option overrides NO_COLOR environment.

       --color-scale, --colour-scale
	      highlight levels of field distinctly.  Use comma(,) separated
	      list of all, age, size

       --color-scale-mode=MODE, --colour-scale-mode=MODE
	      Use gradient or fixed colors in --color-scale.

       Valid options are fixed or gradient.  When used without a value,
       defaults to gradient.

       --icons=WHEN
	      Display icons next to file names.

       Valid settings are ‘always’, ‘automatic’ (‘auto’ for short), and
       ‘never’.  When used without a value, defaults to ‘automatic’.

       automatic or auto will display icons only when the standard output is
       connected to a real terminal.  If eza is ran while in a tty, or the
       output of eza is either redirected to a file or piped into another
       program, icons will not be used.  Setting this option to ‘always’
       causes eza to always display icons, while ‘never’ disables the use of
       icons.

       --no-quotes
	      Don’t quote file names with spaces.

       --hyperlink
	      Display entries as hyperlinks

       -w, --width=COLS
	      Set screen width in columns.

FILTERING AND SORTING OPTIONS
       -a, --all
	      Show hidden and “dot” files.  Use this twice to also show the
	      ‘.’ and ‘..’ directories.

       -A, --almost-all
	      Equivalent to –all; included for compatibility with ls -A.

       -d, --treat-dirs-as-files
	      This flag, inherited from ls, changes how eza handles directory
	      arguments.  Instead of recursing into directories and listing
	      their contents (the default behavior), it treats directories as
	      regular files and lists information about the directory entry
	      itself.  This is useful when you want to see metadata about the
	      directory (e.g., permissions, size, modification time) rather
	      than its contents.  For simply listing only directories and not
	      files, consider using the --only-dirs (-D) option as an
	      alternative.

       -L, --level=DEPTH
	      Limit the depth of recursion.

       -r, --reverse
	      Reverse the sort order.

       -s, --sort=SORT_FIELD
	      Which field to sort by.

       Valid sort fields are ‘name’, ‘Name’, ‘extension’, ‘Extension’, ‘size’,
       ‘modified’, ‘changed’, ‘accessed’, ‘created’, ‘inode’, ‘type’, and
       ‘none’.

       The modified sort field has the aliases ‘date’, ‘time’, and ‘newest’,
       and its reverse order has the aliases ‘age’ and ‘oldest’.

       Sort fields starting with a capital letter will sort uppercase before
       lowercase: ‘A’ then ‘B’ then ‘a’ then ‘b’.  Fields starting with a
       lowercase letter will mix them: ‘A’ then ‘a’ then ‘B’ then ‘b’.

       -I, --ignore-glob=GLOBS
	      Glob patterns, pipe-separated, of files to ignore.

       --git-ignore [if eza was built with git support]
	      Do not list files that are ignored by Git.

       --group-directories-first
	      List directories before other files.

       --group-directories-last
	      List directories after other files.

       -D, --only-dirs
	      List only directories, not files.

       -f, --only-files
	      List only files, not directories.

       --show-symlinks
	      Explicitly show symbolic links (when used with --only-files |
	      --only-dirs)

       --no-syml
```
