import rpy2.robjects as robjects

def runScripts():
    robjects.r.source("SpotySuggestions/src/r/Finale.r")
