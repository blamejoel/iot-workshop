### Connecting your Pi to Eduroam @ UCR
Copy the `wpa_supplicant.conf` file to your Pi's
`/etc/wpa_supplicant/` directory.
```
curl https://github.com/jgome043/iot-workshop/blob/master/iot-6-outside-access/wpa_supplicant.conf -O
sudo cp wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf
```

Next, edit the file (you will need to be `root`) so that it contains your
information (netID pretty much)

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Lastly, we'll fill in your netID password, but hashed because plain-text
passwords are bad mmkay!
```
echo -n 'YOUR_NETID_PASSWORD' | iconv -t utf16le | openssl md4 | awk '{print $2}' > hash.txt
```

Now the file `hash.txt` should have a hash of your netID password, copy that
into the `/etc/wpa_supplicant/wpa_supplicant.conf` file, in the "password"
field.  
  
For security reasons, clear your terminal history now! (since your password is
in plain-text there!)
```
history -c
history -w
```

Reboot your Pi and enjoy wireless connectivity on eduroam!
