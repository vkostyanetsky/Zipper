# Zipper

[![mypy](https://github.com/vkostyanetsky/Zipper/actions/workflows/mypy.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/mypy.yml) [![pylint](https://github.com/vkostyanetsky/Zipper/actions/workflows/pylint.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/pylint.yml) [![black](https://github.com/vkostyanetsky/Zipper/actions/workflows/black.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/black.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   

A primitive CLI tool intended to archive a given directory to another directory.

## Usage

```
py zipper.py MySource MyTarget
```

The MySource directory will be copied to the MyTarget directory as a ZIP archive, which name is includes the current date and time (`2023_02_23 09_23_46.zip`, for example).