import os
import pickle
from pathlib import Path 


class FileResolver:
    """
    relative_path
    absolute_path
    """

    def __init__(self, name: str, prefix = "./cache.kaif"):
        """
        {prefix} Is a relative path by default, must specify the absolute location overriding the prefix param
        {name} Name of the file or folder, with only allowed symbols by the OS
        """

        # Sanitize input
        result = self.sanitize(path=name)

        # Resolve folder: prefix
        print(f"The prefix is: {prefix}")

        self.resolve_folder(folder_name=prefix)

        # Create the file
        full_path: str = f"{prefix}/{result}"

        self.absolute_path = full_path
        

    def resolve_folder(self,folder_name: str) -> str:

        Path(folder_name).mkdir(parents=True, exist_ok=True)

        return folder_name

    def read_inner_file(self):
        pass

    def sanitize(self, path:str) -> str:
        """
        Cleans the path to avoid bugs
        """
        # Separete the extension
        [neutral_name, extension] = os.path.splitext(path)

        # Clean any troublesome symbol in the name

        #index = re.search("", neutral_name).start()

        return f"{neutral_name}{extension}"
