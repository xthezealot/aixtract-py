from importlib.metadata import version

try:
    __version__ = version("aixtract")
except Exception:
    __version__ = "unknown"
