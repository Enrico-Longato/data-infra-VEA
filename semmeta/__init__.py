# Core imports
from .metadata_extractor_module import SEMMetaData
from .json_cleaner_module import JsonCleaner
from .visualizer_module import SEMVisualizer

# Instantiate reusable objects (optional)
SEMMeta = SEMMetaData()
CLEANER = JsonCleaner()

# Allow users to cleanly import these classes and objects directly
__all__ = ['SEMMetaData', 'JsonCleaner', 'SEMVisualizer', 'SEMMeta', 'CLEANER']