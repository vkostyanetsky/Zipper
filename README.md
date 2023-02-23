# Zipper

[![mypy](https://github.com/vkostyanetsky/Zipper/actions/workflows/mypy.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/mypy.yml) [![pylint](https://github.com/vkostyanetsky/Zipper/actions/workflows/pylint.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/pylint.yml) [![black](https://github.com/vkostyanetsky/Zipper/actions/workflows/black.yml/badge.svg)](https://github.com/vkostyanetsky/Zipper/actions/workflows/black.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   

A primitive CLI tool intended to archive a given directory to another directory.

## Usage

```
zipper.py SourceFolder TargetFolder
```

The SourceFolder directory will be copied to the TargetFolder directory as a ZIP archive, which name is current date and time (2023_02_23 09_23_46.zip, for example).