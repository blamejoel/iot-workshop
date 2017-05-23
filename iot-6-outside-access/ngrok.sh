#!/usr/bin/env bash
# NGROK_PATH=$HOME/Downloads/ngrok
# $($NGROK_PATH http 5000 &)
NGROK_URL=$(curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh)
if [[ $NGROK_URL != *"http"* ]]; then
    echo "ngrok isn't running!"
    curl https://dweet.io/dweet/for/jgome043?ngrokurl=n/a
    # exit 1
else
    echo "$NGROK_URL"
    curl https://dweet.io/dweet/for/jgome043?ngrokurl=$NGROK_URL
fi
# curl https://dweet.io/dweet/for/jgome043?ngrokurl=$NGROK_URL
