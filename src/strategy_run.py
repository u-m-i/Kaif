
class StrategyRun:
    """
    <<Compose>> Client
    """

    def __init__(self, parser: Parser):
        """
        """

        self._inner_parser = parser


    def preprocess(self, trj_file: FileResolver) -> Evidence:
        """
        """
        
        self._inner_parser.parse_trajectory(trj_file=trj_file)
