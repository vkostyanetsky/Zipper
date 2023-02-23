import os
import time
import zipfile
import click


@click.command()
@click.argument('source_path', type=click.Path(exists=True))
@click.argument('target_path', type=click.Path(exists=True))
def make_backup(source_path: str, target_path: str):
    target_file_name = time.strftime("%Y_%m_%d %H_%M_%S.zip")
    target_file_path = os.path.join(target_path, target_file_name)

    fantasy_zip = zipfile.ZipFile(target_file_path, "w")

    for folder, _, files in os.walk(source_path):
        for file in files:
            fantasy_zip.write(
                os.path.join(folder, file),
                os.path.relpath(os.path.join(folder, file), source_path),
                compress_type=zipfile.ZIP_DEFLATED,
            )

    fantasy_zip.close()


if __name__ == '__main__':
    make_backup()
