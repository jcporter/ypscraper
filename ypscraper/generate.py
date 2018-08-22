import json
import pprint

searches = [{'city' : 'brooklyn'  , 'state' : 'NY'  , 'search_term' : 'dentists'},
            {'city' : 'greenwood' , 'state' : 'SC'  , 'search_term' : 'lawyers'},
            {'city' : 'anderson'  , 'state' : 'SC'  , 'search_term' : 'restaurants'},
            {'city' : 'clemson'   , 'state' : 'SC'  , 'search_term' : 'bars'},
            {'city' : 'las vegas' , 'state' : 'NV'  , 'search_term' : 'casinos'}
           ]

with open('searches.json', 'w') as f:
    f.write(json.dumps(searches))
    
