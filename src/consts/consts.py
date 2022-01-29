class Constants:
    random_state = 101
    # priority_news = [
    #     'CNN', 'MSNBC', 'NBCNews', 'FoxNews', 'ABC', # US
    #     'CTVNews', 'CBCNews', 'globalnews', # Canada
    #     'inquirerdotnet', 'ABSCBNNews', 'gmanews', # Phillippines
    #     'ndtv', 'timesofindia', 'TimesNow', 'republic', # India
    #     'malaysiakini', 'staronline', # Malaysia
    #     'BBCNews', 'itvnews', 'SkyNews', 'guardian', 'MailOnline', # UK
    #     'rtenews', 'Independent_ie', 'thejournal_ie', # Ireland
    #     'News24', 'eNCA', 'SABCNews', # South Africa
    #     'MobilePunch', 'vanguardngrnews', 'PulseNigeria247', # Nigeria
    #     'citizentvkenya', 'ntvkenya', 'NationAfrica', # Kenya
    #     'ntvuganda', 'nbstv', 'DailyMonitor', # Uganda (not in reuters report)
    #     '9NewsAUS', 'abcnews', 'newscomauHQ', # Australia
    #     'NewshubNZ', 'nzherald' # New Zealand (not in reuters report)
    # ]

    priority_news = [
        'CNN', 'MSNBC', 'NBCNews', 'FoxNews', 'ABC', 'nytimes', 'washingtonpost', 'CBSNews', 'NPR', 'newsmax', #US (10)
        'CTVNews', 'CBCNews', 'globalnews', 'globeandmail', 'TorontoStar', 'CP24', 'nationalpost', 'GlobalNational', 'TheTorontoSun', 'calgaryherald', # Canada (10)
        'inquirerdotnet', 'ABSCBNNews', 'gmanews', 'rapplerdotcom', 'PhilippineStar', 'cnnphilippines', 'manilabulletin', # Phillippines (7)
        'ndtv', 'timesofindia', 'TimesNow', 'republic', 'htTweets', 'IndiaToday', 'EconomicTimes', 'the_hindu', 'CNNnews18', 'IndianExpress', # India (10)
        'malaysiakini', 'staronline', 'NST_Online', 'msianinsight', # Malaysia (4)
        'BBCNews', 'itvnews', 'SkyNews', 'guardian', 'MailOnline', 'Independent', 'DailyMailUK', 'TheSun', 'Telegraph', 'DailyMirror', 'Channel4News', # UK (10)
        'rtenews', 'Independent_ie', 'thejournal_ie', 'IrishTimes', 'irishexaminer', 'breakingnewsie', 'IrishMirror', 'VirginMediaNews', 'NewstalkFM', 'irish_news', # Ireland (10)
        'News24', 'eNCA', 'SABCNews', 'TimesLIVE', 'IOL', 'ewnupdates', 'SowetanLIVE', 'City_Press', 'dailymaverick', 'SAfmRadio', # South Africa (10)
        'MobilePunch', 'vanguardngrnews', 'PulseNigeria247', 'Naija_PR', 'thecableng', 'PremiumTimesng', 'DailyPostNGR', 'TheNationNews', 'daily_trust', 'nigeriantribune', # Nigeria (10)
        'citizentvkenya', 'ntvkenya', 'NationAfrica', 'StandardKenya', 'K24Tv', 'Kenyans', 'KBCChannel1', # Kenya (7)
        'ntvuganda', 'nbstv', 'DailyMonitor', 'newvisionwire', 'ChimpReports', # Uganda (not in reuters report) (5)
        '9NewsAUS', 'abcnews', 'newscomauHQ', 'SkyNewsAust', 'theage', 'smh', 'SBSNews', 'theheraldsun', 'GuardianAus', '7NewsAustralia', # Australia (10)
        'NewshubNZ', 'nzherald' , 'NZStuff', 'rnz_news', 'NewstalkZB', 'radionz', '1NewsNZ' # New Zealand (not in reuters report) (7)
    ]
