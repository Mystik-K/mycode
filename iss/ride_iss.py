#!/usr/bin/python3

"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main ():
    """reading json from api"""

    #call api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    #call the api
    helmet = groundctrl.read()

    #show that at this point, our data is str
    #want to convert to list/dict
    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    #this should say bytes
    print(type(helmet))

    #this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    #this returns list of the people on iss
    print(helmetson["people"])

    #first astro on list
    print(helmetson["people"][0])

    for astro in helmetson["people"]:
        print(astro)

    #display every item in a list
    for astro in helmetson["people"]:
        print(astro["name"])


if __name__ == "__main__":
    main()
