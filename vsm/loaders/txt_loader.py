from pathlib import Path

from vsm.exceptions import EmptyDocumentsError


def load_txt_file(path: str | Path, *, encoding: str = "utf-8") -> str:
    file_path = Path(path)

    if not file_path.is_file():
        raise FileNotFoundError(f"Text file not found: {file_path}")

    return file_path.read_text(encoding=encoding)


def load_txt_directory(
    directory: str | Path,
    *,
    encoding: str = "utf-8",
) -> dict[str, str]:
    directory_path = Path(directory)

    if not directory_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    if not directory_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")

    txt_files = sorted(
        path
        for path in directory_path.iterdir()
        if path.is_file() and path.suffix == ".txt"
    )

    if not txt_files:
        raise EmptyDocumentsError(f"No .txt files found in directory: {directory_path}")

    return {
        file_path.stem: load_txt_file(file_path, encoding=encoding)
        for file_path in txt_files
    }
