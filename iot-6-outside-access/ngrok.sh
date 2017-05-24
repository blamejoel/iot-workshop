#!/usr/bin/env bash
TMP_FILE="/tmp/ngrok.dat"
DWEET_ID="jgome043"
NGROK_URL=""
UPDATE=$(date)

if [ -e "$TMP_FILE" ]; then
    NGROK_URL=$(cat $TMP_FILE)
else
    touch $TMP_FILE
fi

NEW_URL=$(curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh) 

if [[ $(cat $TMP_FILE) != $NEW_URL ]]; then
    NGROK_URL=$NEW_URL
    echo "${NGROK_URL}" > $TMP_FILE
    if [[ $NGROK_URL != *"http"* ]]; then
        curl https://dweet.io/dweet/for/$DWEET_ID?ngrokurl=n/a
    else
        curl https://dweet.io/dweet/for/$DWEET_ID?ngrokurl=$NGROK_URL&last_contact=$(date)
    fi
else
    exit 0
fi
