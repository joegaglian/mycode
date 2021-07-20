#!/usr/bin/env python3
# create a list of strings

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list called vendors
for x in farms:
    print("The Farm name is ", x.get("name"), " and we have ",  x.get("agriculture"))

