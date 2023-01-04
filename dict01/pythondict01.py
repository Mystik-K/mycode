#! /usr/bin/env python3

"""Understanding Dictionaries
    {key: value, key:value, ...} """

def main():
    """runtime function"""

    ##dict with 4 key / value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    #display dict
    print(switch)

    #prove switch is indeed dict
    print(type(switch))

    # display parts of dictionary
    print( switch["hostname"] )
    print( switch["ip"] )

    # request fake key
    print( switch["lynx"])



# call func

if __name__ == "__main__":
    main()
