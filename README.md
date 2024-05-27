# Idle Network

Idle Network is a simulation game built with Python where you manage your own virtual network infrastructure. You'll be responsible for optimizing server performance, expanding your network, and researching new technologies to increase your revenue.

## Gameplay Overview

In Idle Network, you start with a server and a PC connected by a cable. The server generates data matrices, initially 1 bit each, at a certain speed. These data matrices are then transmitted through the cable to the PC for processing. For each successfully transmitted data matrix, you earn datapoints, the in-game currency.

However, there's a catch - at the beginning, there's a percentage chance of data corruption during transmission. Corrupted data still reaches the PC but results in processing errors, yielding 0 datapoints and wasting you processing time.

## Features

- **Upgrade Servers:** Improve server performance by upgrading hardware components and increasing processing speed.
- **Expand Network:** Add more PCs and cables to extend the reach of your network and increase data transmission efficiency.
- **Research Technologies:** Invest in research to develop advanced error detection and correction algorithms, reducing data corruption rates and increasing overall revenue.
- **Unlock Upgrades:** Unlock new types of cables, servers, and research options as you progress, allowing for further optimization and expansion.

## Research Options

- **Error Detection Algorithms:** Implement algorithms to identify corrupted data during transmission, and don't waste time trying to decode it.
- **Error Correction Algorithms:** Develop algorithms to correct errors in transmitted data, increasing the likelihood of successful processing.
- **Advanced Upgrades:** Unlock upgrades such as faster servers and pcs. You will also be able to add servers and pcs to get more data transmitted.
- **Enhanced Cables:** Research better cables with higher bandwidth and lower error rates for improved data transmission.

## Getting Started

1. **Install Python:** Make sure you have Python 3.x installed on your system.
2. **Clone the repository:** git clone https://github.com/leonardig08/Idle-Network
3. **Install Dependencies:** pip install -r requirements.txt
4. **Run the game:** python game.py

## Credits

- Thanks to [Pygame WIKI](http://www.pygame.org/wiki/GradientCode) for the code to generate the gradient background
- Thanks to (Will add when itch.io returns online) for the devices assets

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

