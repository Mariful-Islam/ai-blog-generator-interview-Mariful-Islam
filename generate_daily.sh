#!/bin/bash
curl "http://localhost:5000/generate?keyword=wireless%20earbuds" -o "./posts/wireless_earbuds_$(date +\%F).json"
