import os
from file_resolver import FileResolver

class Parser:
    """
    This class allows splitting an evidence file frame by frame.
    """
    def __init__(self, output_path: str):
        """
        Args:
            output_path (str): Complete absolute path where the parsed files will be stored.
        """
        self.output_dir = FileResolver(output_path)  # Create dir for the parser trajectory

    def parse_trajectory(self, trj_file: FileResolver):
        """
        Parses the trajectory file and splits it into individual frames.

        Args:
            trj_file (FileResolver): The trajectory file to be parsed.
        """
        new_evd_file = None

        try:
            for i, line in enumerate(trj_file.read()):
                if "Frame" in line:  # If it's a new frame
                    if new_evd_file:  # If a new evidence file is open, close it
                        new_evd_file.close()
                    
                    # Generate frame file name
                    file_name = f"Frame-{i:07d}.txt"
                    new_evd_file_path = os.path.join(self.output_dir, file_name)
                    new_evd_file = open(new_evd_file_path, 'w')
                if new_evd_file:  # Write the line to the current evidence file
                    new_evd_file.write(line)
        finally:
            # Ensure the last evidence file is closed
            if new_evd_file:
                new_evd_file.close()
            trj_file.close()

# Usage example:
# output_path = "path/to/output"
# trj_file_path = "path/to/trajectory/file"
# parser = Parser(output_path)
# trj_file = FileResolver(trj_file_path)
# parser.parse_trajectory(trj_file)
