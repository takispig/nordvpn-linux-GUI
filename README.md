# nordvpn-linux-GUI
This is a small GUI app i created to make my life a bit easier while using the Nord VPN. Since there is no official app from them a tried to implement a simplified GUI version with the basic functions. Please expect that the app is far from perfect and not widely tested under various circumstances. It has been tested under Ubuntu 20.04 System and a Raspberry Pi 4 (4Gb RAM) and seem to run flawless.

## Resources
The app is written in Python, and specifically the GUI is with tkinter package. So expect that the app is lightweight.
**Notice:** In order to work this app, you have to already have installed the Nord VPN service in your System. 

## Installation
How to run the app:
1. download the project to a local repository
2. open the terminal and make the python file and the script executables by typing:
    ```bash
    chmod +x ./path/to/nordvpn-linux-GUI/NordVPN.py && chmod +x ./path/to/nordvpn-linux-GUI/script.sh
    ```
    please change the /path/to/ with your own directory
3. run the NordVPN.py (by clicking the file, or by typing it in terminal) and the app will launch
4. OPTIONAL: you can create a Link/Shortcut of NordVPN.py and open it from your Desktop just like any other app

## Screenshots
<p style="text-align: center">
    <img src="https://github.com/takispig/nordvpn-linux-GUI/blob/media/App_connected.png" width="32%"               alt="State when the app is connected">
    <img src="https://github.com/takispig/nordvpn-linux-GUI/blob/media/App_disconnected.png" width="32%" alt ="State when the app is disconnected">
    <img src="https://github.com/takispig/nordvpn-linux-GUI/blob/media/App_terminal.png" width="32%" alt="Example of the terminal use build in app">
    <img src="https://github.com/takispig/nordvpn-linux-GUI/blob/media/App_connect_country.png" width="48%" alt="Connect to a country just by typing a Country or a Country-Code">
    <img src="https://github.com/takispig/nordvpn-linux-GUI/blob/media/App_connect_country_server.png" width="48%" alt="Connection example by typing a country & a specific server number">
</p>

## How to use
- **Quick-connect:**  connects to the nearest server
- **Status:**         displays the current connection state
- **Disconnect:**     disconnects from Nord VPN's server
- **Flags:**          by clicking on the flag buttons you can connect to this country
- **Terminal:**       In app there is a build-in Terminal, just your regular terminal, for convenience reasons
- **Input-Box:**      In there you can type a country to connect (i.e. Sweden) or specify it by typing a server number (i.e. US 6200)


## Feedback
If you experience any trouble, please let me know, there is already a button in the app to navigate you here to file an issue or contact me.

## License:
[MIT](https://github.com/takispig/nordvpn-linux-GUI/blob/main/LICENSE) License
