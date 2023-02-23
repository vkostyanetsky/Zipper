"""
Archives a directory to another directory.
"""

import os
import time
import zipfile

import click


@click.command()
@click.argument("source_path", type=click.Path(exists=True))
@click.argument("target_path", type=click.Path(exists=True))
def make_backup(source_path: str, target_path: str) -> None:
    """
    Archives a source directory to a target directory.
    """

    target_file_name = time.strftime("%Y_%m_%d %H_%M_%S.zip")
    target_file_path = os.path.join(target_path, target_file_name)

    with zipfile.ZipFile(target_file_path, "w") as target_zip_file:
        for folder, _, files in os.walk(source_path):
            for file in files:
                src_file_path = os.path.join(folder, file)
                rel_file_path = os.path.relpath(src_file_path, source_path)
                target_zip_file.write(
                    src_file_path,
                    rel_file_path,
                    compress_type=zipfile.ZIP_DEFLATED,
                )


if __name__ == "__main__":
    make_backup()  # pylint: disable=no-value-for-parameter
