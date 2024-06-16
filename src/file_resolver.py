import re
import os
import pickle
from pathlib import Path 


class FileResolver:
    """
    relative_path
    absolute_path
    """

    def __init__(self, name: str, encoding = "utf-8" , prefix = "./cache.kaif"):
        """
        {prefix} Is a relative path by default, must specify the absolute location overriding the prefix param
        {name} Name of the file or folder, with only allowed symbols by the OS
        """

        self.encoding = encoding

        if(len(name) == 0):
            print("[ERR]: Name of the file is an empty string")

        # Sanitize input
        result = self._sanitize(path=name)

        # DEBUG Resolve folder: prefix
        print(f"The prefix is: {prefix}")

        self._resolve_folder(folder_name=prefix)

        full_name:str = f"{prefix}/{result}"

        # Create the file
        self._resolve_file(file_name=full_name)


        self.relative_path:str = full_name

        # Save different route versions
        self.absolute_path:str = os.path.abspath(full_name)


    def _sanitize(self, path:str) -> str:
        """
        Cleans the path to avoid bugs
        {path}
        """
        # Separete the extension
        [neutral_name, extension] = os.path.splitext(path)

        neutral_name = repr(neutral_name)

        # Clean any troublesome symbol in the name

        result = re.sub(r"[\\/']", "", neutral_name)

        return f"{result}{extension}"

    def _resolve_folder(self,folder_name: str) -> str:
        """
        Resolves to create the folder
        {folder_name}
        """

        Path(folder_name).mkdir(parents=True, exist_ok=True)

        return folder_name

    def _resolve_file(self, file_name: str) -> None:
        """
        Resolves the creation of the file
        {file_name} 
        """
        with open(file_name, "a", encoding = self.encoding) as file:
            return

