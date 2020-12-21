# Unity Version Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/educup/uvm/workflows/CI/badge.svg)](https://github.com/educup/uvm/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/educup/uvm/branch/main/graph/badge.svg?token=Z1MEEL3EAB)](https://codecov.io/gh/educup/uvm)
[![Version](https://img.shields.io/pypi/v/uvm?color=%2334D058&label=Version)](https://pypi.org/project/uvm)
[![Last commit](https://img.shields.io/github/last-commit/educup/uvm.svg?style=flat)](https://github.com/educup/uvm/commits)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/educup/uvm)](https://github.com/educup/uvm/commits)
[![Github Stars](https://img.shields.io/github/stars/educup/uvm?style=flat&logo=github)](https://github.com/educup/uvm/stargazers)
[![Github Forks](https://img.shields.io/github/forks/educup/uvm?style=flat&logo=github)](https://github.com/educup/uvm/network/members)
[![Github Watchers](https://img.shields.io/github/watchers/educup/uvm?style=flat&logo=github)](https://github.com/educup/uvm)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Feducup.github.io/uvm)](https://educup.github.io/uvm)
[![GitHub contributors](https://img.shields.io/github/contributors/educup/uvm)](https://github.com/educup/uvm/graphs/contributors)

[Unity](https://unity.com) Version Manager CLI implemented with [Python](https://www.python.org) and [Typer](https://typer.tiangolo.com).

**Usage**:

```console
$ uvm [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `build`: Command to manage the version build
* `code`: Command to manage the version code
* `get`: Get the version
* `major`: Command to manage the version major
* `minor`: Command to manage the version minor
* `patch`: Command to manage the version patch
* `set`: Set the version

## `uvm build`

Command to manage the version build

**Usage**:

```console
$ uvm build [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the version build
* `set`: Set the version build
* `setup`: Increase the version build to the next

### `uvm build get`

Get the version build

**Usage**:

```console
$ uvm build get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm build set`

Set the version build

**Usage**:

```console
$ uvm build set [OPTIONS] NUMBER [FILENAME]
```

**Arguments**:

* `NUMBER`: Version build  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm build setup`

Increase the version build to the next

**Usage**:

```console
$ uvm build setup [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm code`

Command to manage the version code

**Usage**:

```console
$ uvm code [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the version code
* `set`: Set the version code
* `setup`: Increase the version code to the next

### `uvm code get`

Get the version code

**Usage**:

```console
$ uvm code get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm code set`

Set the version code

**Usage**:

```console
$ uvm code set [OPTIONS] NUMBER [FILENAME]
```

**Arguments**:

* `NUMBER`: Version code  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm code setup`

Increase the version code to the next

**Usage**:

```console
$ uvm code setup [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm get`

Get the version

**Usage**:

```console
$ uvm get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm major`

Command to manage the version major

**Usage**:

```console
$ uvm major [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the version major
* `set`: Set the version major
* `setup`: Increase the version major to the next

### `uvm major get`

Get the version major

**Usage**:

```console
$ uvm major get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm major set`

Set the version major

**Usage**:

```console
$ uvm major set [OPTIONS] NUMBER [FILENAME]
```

**Arguments**:

* `NUMBER`: Version major  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm major setup`

Increase the version major to the next

**Usage**:

```console
$ uvm major setup [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm minor`

Command to manage the version minor

**Usage**:

```console
$ uvm minor [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the version minor
* `set`: Set the version minor
* `setup`: Increase the version minor to the next

### `uvm minor get`

Get the version minor

**Usage**:

```console
$ uvm minor get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm minor set`

Set the version minor

**Usage**:

```console
$ uvm minor set [OPTIONS] NUMBER [FILENAME]
```

**Arguments**:

* `NUMBER`: Version minor  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm minor setup`

Increase the version minor to the next

**Usage**:

```console
$ uvm minor setup [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm patch`

Command to manage the version patch

**Usage**:

```console
$ uvm patch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the version patch
* `set`: Set the version patch
* `setup`: Increase the version patch to the next

### `uvm patch get`

Get the version patch

**Usage**:

```console
$ uvm patch get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm patch set`

Set the version patch

**Usage**:

```console
$ uvm patch set [OPTIONS] NUMBER [FILENAME]
```

**Arguments**:

* `NUMBER`: Version patch  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

### `uvm patch setup`

Increase the version patch to the next

**Usage**:

```console
$ uvm patch setup [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.

## `uvm set`

Set the version

**Usage**:

```console
$ uvm set [OPTIONS] ARG [FILENAME]
```

**Arguments**:

* `ARG`: The format must be `"*.*.*b*(*)"` where * is the major, minor, patch, build and code respectively and all integers.  [required]
* `[FILENAME]`: Path of ProjectSettings.asset file of the Unity project  [envvar: UVM_FILENAME;default: ./ProjectSettings/ProjectSettings.asset]

**Options**:

* `--help`: Show this message and exit.
