import pandas as pd
import requests
import time


# -------------------- COMMON HELPERS --------------------

def load_countries():
    url = "https://api.worldbank.org/countries?format=json&per_page=300"
    data = requests.get(url).json()

    countries = pd.DataFrame(data[1])
    countries["region"] = countries["region"].apply(lambda x: x["value"])
    countries["incomeLevel"] = countries["incomeLevel"].apply(lambda x: x["value"])
    countries["lendingType"] = countries["lendingType"].apply(lambda x: x["value"])
    countries = countries.rename(columns={"iso2Code": "country_id"})
    countries.drop(columns=["adminregion", "capitalCity"], inplace=True)

    return countries


def fetch_indicators(indicators):
    base_url = "https://api.worldbank.org/countries/all/indicators/{}?format=json&per_page=1000&page={}"
    all_df = []

    for indicator in indicators:
        page = 1
        while True:
            url = base_url.format(indicator, page)
            r = requests.get(url)

            if r.status_code != 200:
                break

            data = r.json()
            if not data or len(data) < 2 or not data[1]:
                break

            total_pages = data[0]["pages"]

            df = pd.json_normalize(data[1])
            df = df.rename(columns={
                "indicator.value": "indicators",
                "country.id": "country_id",
                "country.value": "country",
                "date": "year"
            })

            df["year"] = pd.to_numeric(df["year"], errors="coerce")
            df = df[df["year"] > 2015]

            if not df.empty:
                all_df.append(df)

            if page >= total_pages:
                break

            page += 1
            time.sleep(0.3)

    return pd.concat(all_df, ignore_index=True) if all_df else pd.DataFrame()

"""
def finalize_schema(df):
    df["longitude"] = pd.NA
    df["latitude"] = pd.NA
    df["unit"] = ""
    df["obs_status"] = ""
    df["decimal"] = 0
    df["countryiso3code"] = ""
    return df
"""

# -------------------- DATASET FUNCTIONS --------------------

def get_economic():
    from world_bank_data import load_countries
    indicators = [
        "NY.GDP.MKTP.KD.ZG",
        "NY.GDP.PCAP.CD"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_labour_market():
    from world_bank_data import load_countries
    indicators = [
        "SL.UEM.TOTL.ZS",
        "SL.UEM.1524.ZS",
        "SL.TLF.TOTL.IN"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_trade():
    from world_bank_data import load_countries
    indicators = [
        "NE.EXP.GNFS.CD",
        "NE.IMP.GNFS.CD"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_poverty():
    from world_bank_data import load_countries
    indicators = [
        "SI.POV.NAHC",
        "SI.POV.GINI"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_environment():
    from world_bank_data import load_countries
    indicators = [
        "EG.FEC.RNEW.ZS",
        "AG.LND.FRST.ZS"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_health():
    from world_bank_data import load_countries
    indicators = [
        "SP.DYN.LE00.IN",
        "SP.DYN.IMRT.IN",
        "SH.H2O.BASW.ZS",
        "SH.XPD.CHEX.GD.ZS",
        "SH.IMM.IDPT",
        "SH.IMM.MEAS",
        "SH.MMR.RISK.ZS",
        "SH.DTH.COMM.ZS",
        "SH.TBS.INCD",
        "SH.STA.BRTC.ZS",
        "SH.STA.MMRT",
        "SP.POP.65UP.TO.ZS",
        "SH.HIV.INCD.ZS"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df


def get_technology():
    from world_bank_data import load_countries
    indicators = [
        "IT.NET.USER.ZS",
        "IT.CEL.SETS.P2"
    ]
    df = fetch_indicators(indicators)
    df = pd.merge(df, load_countries(), on="country_id", how="inner")
    df.drop(columns=["indicator.id","name","id"], inplace=True)
    return df
