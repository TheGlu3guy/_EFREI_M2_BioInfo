import pandas as pd
import pycountry

def getCountryCode(x):
    try:
        return pycountry.countries.get(name=x).alpha_3
    except:
        return None

from geopy.geocoders import Nominatim
import numpy as np

geolocator = Nominatim(user_agent="chickungunyalocation")
def geolocate(country):
    try:
        loc = geolocator.geocode(country)
        return (loc.latitude, loc.longitude)
    except:
        return np.nan
europe = pd.read_csv("cleaned/TotalCasesEurope.csv")
america = pd.read_csv("cleaned/TotalCasesEurope.csv")
europe["Location"] = europe["CountryCode"].apply(geolocate)
america["Location"] = america["CountryCode"].apply(geolocate)

# -- Format the data for the European countries --
df = pd.read_csv("data/TotalCaseEurope.csv")
df = df[['Time', 'RegionName', 'NumValue']]
df["CountryCode"] = df["RegionName"].apply(getCountryCode)
df = df[df["CountryCode"].notna()]
df["Location"] = df["CountryCode"].apply(geolocate)
df.to_csv("cleaned/TotalCasesEurope.csv", index=False)


# -- Format the data for the American countries --
def formalizeAmericanDf(year):
    df = pd.read_csv("data/TotalCaseAmerica"+str(year)+".csv")

    #Keep only interesting rows
    df = df[['Country or Subregion', 'Measure Values']]
    #Rename for consistency
    df = df.rename(columns={"Country or Subregion": "RegionName", "Measure Values": "NumValue"}, errors="raise")
    #Add row for the year
    df["Time"]=[str(year)]*len(df)
    #Correct the name of the United States
    df.loc[df["RegionName"] == "United States of America", 'RegionName'] = "United States"
    #Add the country code
    df["CountryCode"] = df["RegionName"].apply(getCountryCode)
    #Remove Weird countries or agglomerations
    df = df[df["CountryCode"].notna()]
    df["Location"] = df["CountryCode"].apply(geolocate)

    return df

tmp = []
for year in range(2019, 2023):
    tmp.append(formalizeAmericanDf(year))
pd.concat(tmp).to_csv("cleaned/TotalCasesAmerica.csv", index=False)