import rpy2.robjects as robjects

def runScripts():
    robjects.r.source("SpotySuggestions/src/r/regressione.r", encoding="utf-8")
    robjects.r.source("SpotySuggestions/src/r/classificazione.r", encoding="utf-8")