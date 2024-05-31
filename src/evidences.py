
class Evidences:
    """
    <<Composite-Component>>
    """

    def __init__(self):
        pass

    def getEvidences(self):
        pass

    def loadEvidences(self, EvidencesDirSource):
        pass


class LeafEvidences(Evidences):
    """
    <<Composite-Leaf>>
    """
    def __init__(self):
        super().__init__()

    def getEvidences(self):
        super().getEvidences()

    def loadEvidences(self, EvidencesDirSource):
        super().loadEvidences(EvidencesDirSource)


class CompositeEvidences(Evidences):
    """
    <<Composite-Composite>>
    """
    def __init__(self):
        super().__init__()
        self.children = []

    def getEvidences(self):
        super().getEvidences()

    def loadEvidences(self, EvidencesDirSource):
        super().loadEvidences(EvidencesDirSource)

    def add(self, item: Evidences):
        self.children.append(item)

    def remove(self, item: Evidences):
        self.children.remove(item)
