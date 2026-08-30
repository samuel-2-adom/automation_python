import re
import os
from .parser import parser
from pathlib import Path

p = parser("Star Trek Strange New Worlds S04E6 (SeriezLoaded.tv).mkv")


def formatter(series_name, metadata, source_path):
    episode = metadata["episode"]
    season = metadata["season"]
    source_path = Path(source_path)
    
    if season is not None:
        name = f"{series_name}_S{season:02}E{episode:02}"
    else:
        name = f"{series_name}_E{episode:02}"
    return f"{name}{source_path.suffix}"

if __name__ == "__main__":
    #print(formatter("Long Star",p,"C:hshush.mp4"))