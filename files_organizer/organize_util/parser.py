import re
from .patterns import patterns

def parser(f_name=None):
    season_epi,episode,season,year,resolution = patterns()
    
    season_epi = re.compile(season_epi)
    s_e = season_epi.search(f_name)
    
    episode = re.compile(episode)
    e = episode.search(f_name)
    
    season = re.compile(season)
    s = season.search(f_name)
    
    year = re.compile(year)
    y = year.search(f_name)
    
    resolution = re.compile(resolution)
    r = resolution.search(f_name)
    
    metadata = {"season" : None,
                "episode" : None,
                "year" : None,
                "resolution" : None}
    
    if s_e:
        metadata["season"] = int(s_e.group(2))
        metadata["episode"] = int(s_e.group(4))
        
    
    else:
        if e:
            metadata["episode"] = int(e.group(2))
        if s:
            metadata["season"] = int(s.group(2))
        
    if y:
        metadata["year"] = int(y.group(1))
        
    if r:
        metadata["resolution"] = r.group(1)
    
    return metadata
    
if __name__ == "__main__":
    print(parser("AnimePahe_Ryoumin_0-nin_Start_no_Henkyou_Ryoushu-sama_-_09_720p_SubsPlease"))
