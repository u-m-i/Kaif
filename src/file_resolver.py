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

        # Sanitize input
        result = self._sanitize(path=name)

        # DEBUG Resolve folder: prefix
        print(f"The prefix is: {prefix}")

        self._resolve_folder(folder_name=prefix)

        # Create the file
        full_path:str = f"{prefix}/{result}"

        self._resolve_file(file_name=full_path)

        # Save different route versions
        self.absolute_path:str = full_path

        self.relative_path:str = result
        

    def _sanitize(self, path:str) -> str:
        """
        Cleans the path to avoid bugs
        {path}
        """
        # Separete the extension
        [neutral_name, extension] = os.path.splitext(path)

        # Clean any troublesome symbol in the name

        #index = re.search("", neutral_name).start()

        return f"{neutral_name}{extension}"
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
        # TEST => DO NOT WORK
        with open(file_name, "a", encoding="utf-8") as file:
            return

    def read_inner_file(self, encoding = "utf-8"):
        """
        Return the data from the file dispatched and returns its value
        {encoding} The default value for encoding is utf-8
        """

        # Gets the content and return it
        with open(self.absolute_path, "r", encoding = encoding) as data:
            return data
