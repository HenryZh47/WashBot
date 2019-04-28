This is a guide to show how to connect to Washbot.
Author: Henry Zhang <hzhang0407@gmail.com>

# Connect to robot through ethernet cable with internet sharing
This method shares the wifi network on the host PC through ethernet cable. It provides both Internet connection and SSH capabilities. It is recommended to use this method duriong development phase when you need to download packages from the Internet.

## Preparation
* A keyboard and a mouse (for first-time setup)
* An external monitor (for first-time setup)
* A host PC running Ubuntu
* An ethernet cable (and necessary converters if host PC does not have ethernet port)

## Procedures
### Setup on the host PC
1. Type `nm-connection-editor` in a terminal.
2. Add a shared network connection by pressing `Add` button.
3. Choose `Ethernet` in the list and create new connection.
4. Click `IPv4 Settings` tab.
5. Choose `Shared to other computers` in the method drop down menu.
6. Connect the TX2 and host PC with ethernet cable.
7. Enter a new name for the connection (Something like `TX2_share`).
8. Check the IP address and network mask of the new connection (should be `10.42.0.1` and `255.255.255.0`)

### Setup on the TX2
1. Go to `edit connections` in the network selection menu and select the new ethernet connection.
2. Select `Manual` in the method drop down menu.
3. Click `Add` in the addresses to add a static IP.
4. Put `10.42.0.165` for IP; `255.255.255.0` for network mask; `10.42.0.1` for gateway.
5. Put `10.42.0.1` for DNS server.
6. Save and reconnect to the ethernet network.

### Test
Now you should be able to SSH to the TX2 though `ssh nvidia@10.42.0.165`. You can test Internet connection by running `apt-get update`.
You only need to plugin the ethernet cable and SSH for the next time.

# Connect to robot through router network
This method gives SSH capabilities but does not provide Internet connection. Use this method for demos and code test.

## Procedure
1. Plug the Asus router to power.
2. Connect host PC to `washbot_2G` wifi.
3. You should now be able to SSH to TX2 using `ssh nvidia@192.168.50.165`

## Washbot WIFI
* SSID: washbot_2G
* Password: washbot00

## Router Info
* Username: admin
* Password: washbot00

