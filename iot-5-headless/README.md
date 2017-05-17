# Internet of Things workshop Spring 2017
### Workshop 5 - *Headless* Raspberry Pi
## Pre-setup
1. [Download Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/)
2. [Write the downloaded image to your SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
3. "Mount" the SD card to your system 
  * (you should see a partition called `boot`)
4. Create an empty file called `ssh` in your SD card's boot partition
5. Eject your card and insert it into the Pi
6. Connect an Ethernet cable to your Pi and connect the other end to your
   router
7. Boot your Pi! (connect power to it)
8. Wait a few seconds, then try and ping the client `raspberrypi.local`
  * On \*nix systems, this is just `ping raspberrypi.local` from a terminal
    window
  * On Windows systems, you can open up PowerShell or cmd and run the same
    command, as shown for *nix systems
9. Once you can ping the Pi, you should be able to ssh into it with 
`ssh pi@raspberrypi.local`, the password will be the default Raspberry Pi
password, `raspberry`
10. Congratulations, you are now connected to your Pi, *headless*!

## Setup locale info and configure keyboard!
Once you're ssh'd into your Pi, run `sudo raspi-config` from your Raspberry Pi
shell
#### Locale
* Use the arrow keys to highlight option "4. Localisation Options" and select it
  with the "enter/return" key on your keyboard
* Select "Change Locale"
* Scroll down the list and find "en_GB.UTF-8 UTF-8"
  * Press the "space bar" on your keyboard to unselect that option
* Continue scrolling down the list and find "en_US.UTF-8 UTF-8"
  * Press the "space bar" on your keyboard to select that option
* Press the "enter/return" key on your keyboard to confirm your choices
* Scroll down to en_US.UTF-8 and select it

#### Timezone
* Use the arrow keys to highlight option "4. Localisation Options" and select it
  with the "enter/return" key on your keyboard
* Select "Change Timezone"
* Scroll to "America" and select it
* Scroll to "Los_Angeles" and select it (you can also type "L" to get there
  faster...)

#### Wi-fi Country
* Use the arrow keys to highlight option "4. Localisation Options" and select it
  with the "enter/return" key on your keyboard
* Select "Change Wi-fi Country"
* Scroll to "US United States" and select it

#### Keyboard (if available)
* Use the arrow keys to highlight option "4. Localisation Options" and select it
  with the "enter/return" key on your keyboard
* Select "Change Keyboard Layout"
* Scroll to a Generic n-key PC keyboard option, if you're unsure just select the
  default once selected, "Generic 105-key (Intl) PC"
* Scroll to "Other" and select it
* Scroll to "English (US) and select it"
* Scroll up to "English (US) and select it"
* Scroll down to "No AltGr key" and select it
* Select "No compose key"

#### Other settings of interest
1. Change User Password (you should probably do this, asap)
2. Hostname (changes the "hostname" for the Pi, your hostname is what shows up
     in the terminal along with your currently logged in user in the format 
     `$ user@hostname`, e.g. `$ pi@raspberry`). Changing this will also change
     your `raspberrypi.local` name, specifically the `raspberrypi` part.
3. Boot Options (should be self-explanatory, no need to change anything here
     for headless operation)
4. Localisation Options (we already covered this above)
5. Interfacing Options (configure various GPIO settings)
6. Overclock (meh, Google, but probably don't touch this unless you *really*
     know what you're doing)
7. Advanced Options
  * Expand Filesystem (on older versions of Raspbian, you needed to do this to
    use the full space on your SD card, but newer versions of Raspbian do this
    automatically on first boot)
  * Overscan (if your Pi HDMI output doesn't fit your display, you may need to
    play with this setting)
  * Memory Split (see 6. Overclock, above)
  * Audio (select whether you want audio out of HDMI or 3.5mm jack)
  * Resolution (self-explanatory)
  * GL Driver (see 6. Overclock, above)
8. Update (update the raspi-config tool)

## Wi-Fi setup
#### Verify your wireless interface is working
Type the following into your Pi's shell:
```
ip a
```
You should see a line with `wlan0` if your wireless interface is detected.
#### Scan for available networks
```
sudo iwlist wlan0 scan | grep ESSID
```
You should see a list of available wireless networks, hopefully the one you want
to connect to is in the list!
#### Connect to a WPA-encrypted wireless network
```
wpa_passphrase "[SSID]" "[passphrase]" | sed -r '/#/d' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
```
example...
```
wpa_passphrase "ucrwpa" "mynetidpassword" | sed -r '/#/d' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
```

## Other stuff
Once you have network connectivity, you might want to update and upgrade your 
existing packages...
```
sudo apt update && sudo apt upgrade -y
```
Reboot your Pi!


## Other tools
* Pi Bakery - a "Scratch/Blocks" tool for Windows and Mac for creating Raspberry
  Pi images, customized to run specific scripts or options on first or every
  boot, you can also create an image with ssh or Wi-fi credentials entered for 
  you so your Pi is ready to go from first boot.

## Troubleshooting
* `ping raspberrypi.local` doesn't work!
  If this doesn't work, try to login to your router and look for the router's
  DHCP client lease table to find out your Raspberry Pi's IP address. If you can
  find it, use that address instead of `raspberrypi.local`
  * I can't login to my router because I don't know the admin password
    If this is the case, you can scan your network with `nmap`. `nmap` is easily
    installable from a package manager on *nix systems. On Windows systems, I
    recommend installing [Cygwin](https://www.cygwin.com/), and then installing
    `nmap` for Cygwin (this involves downloading a zip with binaries and 
    unzipping it to your Cygwin directory)  
      
    Next you'll need to find your network ID, this can be found by finding the
    IP address of another client on your network (like your laptop), and in
    *most* cases, changing the last number to a `0`. So let's say your laptop's
    IP address is 192.168.1.45, your network ID would most likely be 
    192.168.1.0 if your subnet mask is 255.255.255.0, if your subnet mask is
    different, and you're unsure how to derive the info you need, consult a more
    experienced user or ask the internet!  
      
    Once you have `nmap` installed (confirm by running `which nmap` in your 
    \*nix or Cygwin terminal), use the command `nmap -sn [your network id]/24`. 
    This could take a LONG time depending on what your network configuration
    turned out to be based on your network ID and your subnet mask.
    **DO NOT run `nmap` on ANY UC network or any network that you don't have the
    explicit right to scan!**, srsly, this could get you in legal trouble.  
      
    When the scan finishes, you should see all of the available clients found on
    the network. Look for the one with "Raspberry Pi Foundation" next to the MAC
    address, that's your Pi and it's IP! Take note of this, there's a good
    chance it won't change unless another technical stuff that's outside of the
    scope of this walkthrough.

* I'm getting an error message when I try to ssh into my Raspberry Pi
  Did you use your PC to create the empty ssh file in the boot partition of the 
  SD card?
