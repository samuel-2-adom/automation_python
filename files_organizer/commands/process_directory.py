from pathlib import Path
from organize_util import parser
from organize_util import formatter


def process_directory(directory):
    directory = Path(directory)

    # 1. Get the files
    files = [file for file in directory.iterdir() if file.is_file()]

    parsed_files = []

    # 2. Parse every file
    for file in files:
        metadata = parser(file.name)

        # Only keep files where we successfully detected an episode
        if metadata["episode"] is not None:
            parsed_files.append({
                "path": file,
                "metadata": metadata
            })

    # 3. Sort using the detected episode number
    parsed_files.sort(
        key=lambda item: item["metadata"]["episode"]
    )

    # 4. Ask the user for the series name
    series_name = input("Series name: ")

    # 5. Show what is about to happen
    print("\nRename Preview:")
    
    for item in parsed_files:
        old_path = item["path"]
        metadata = item["metadata"]

        new_name = formatter(
            series_name,
            metadata,
            old_path
        )

        print(f"{old_path.name}  ->  {new_name}")

    # 6. Confirm before actually renaming
    confirm = input("\nRename files? [y/N]: ")

    if confirm.lower() != "y":
        print("Cancelled.")
        return

    # 7. Rename
    for item in parsed_files:
        old_path = item["path"]
        metadata = item["metadata"]

        new_name = formatter(
            series_name,
            metadata,
            old_path
        )

        new_path = old_path.parent / new_name

        old_path.rename(new_path)

        print(f"Renamed: {old_path.name} -> {new_name}")


if __name__=="__main__":
    #rename(dest,source)