import re
def patterns():
    season_epi = r"(S|s|season|Season)\s?([0-9]{1,})\s?(E|e|EP|Ep|Episode|episode)\s?([0-9]{1,})"

    episode = r"(e|E|EP|Ep|Episode|episode)\s?([0-9]{1,})"

    season = r"(S|s|season|Season)\s?([0-9]{1,})"

    year = r"([1][9][9][0-9]|[2][0][1][0-9]|[2][0][2][0-9]|[2][0][3][0-9])"

    resolution = r"([0-9]{3,4}[p])"
    
    pattern = season_epi,episode,season,year,resolution
    return pattern

if __name__ == "__main__":
    text = "names is Goegy and the year me was born was 2020 in 720p movie name was JJJ S1E4"
    season_epi,episode,season,year,resolution = patterns()
    a = re.search(year,text)
    b = re.search(season_epi,text)
    c = re.search(resolution,text)
    print(a.group())
    print(b.group())
    print(c)
