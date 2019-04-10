#!/bin/bash

# Wait the server responds 

while ! httping -qc1 http://localhost:8080 ; do sleep 1 ; done

# Run the guide

jupyter nbconvert --to markdown --execute Wordpress.ipynb


