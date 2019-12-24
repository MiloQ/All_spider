import requests
url = "https://www.ctic.org/crm?tdsourcetag=s_pctim_aiomsg"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',

}
data = {"_csrf": "mJDcAJmrX2cF8zPx25R9hv1pMQu8rTCwRn7ffm2Z1l1NYgisD-VoXIgRueSeYalInlThqMNdqRXAoDOYnRBHog==",
        "CRMSearchForm[year]": "2011", "CRMSearchForm[format]": ["", "Hectares"],
        "CRMSearchForm[area]": ["", "National"], "CRMSearchForm[region]": "Midwest", "CRMSearchForm[state]": "IL",
        "CRMSearchForm[county]": "Adams", "CRMSearchForm[crop_type]": ["", "Custom"], "CropType22[]": "3",
        "summary": "national"}
s = requests.Session()
s.get(url = url)
print(s.cookies)
s = requests.post(url=url,data = data ,headers = headers)
print(s.status_code)


