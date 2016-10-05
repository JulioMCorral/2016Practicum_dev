#!/bin/bash
# ENVIRONMENT=$(mongoimport --db timeline --collection keypress --drop --file keypressData.json) #formated json
ENVIRONMENT=$(mongoimport --db timeline --collection keypress --drop --file keypressData.json --jsonArray) #raw json