# Drug Dealer Simulator Assistant

This Python script is designed to assist in the efficient packaging of orders in the context of a Drug Dealer Simulator game. It simplifies the process of managing client orders, calculating optimal packaging configurations, and maintaining an order history.

## Features

- **Client Management**: Add new clients and view a list of all clients.
- **New Order Processing**: Input orders for each client and calculate the most efficient packaging options.
- **Order History**: View a detailed list of past orders, including client names, amounts requested, and the packaging options provided.

## How It Works

The script offers a simple menu-driven interface to navigate through its features:

1. **Clients**: Add new clients or list all existing clients.
2. **New Order**: For each client, input the amount requested. The script then calculates and displays the optimal packaging options.
3. **Order History**: Displays a detailed history of all orders, including timestamps, client names, amounts requested, and packaging details.

### Packaging Calculation

The packaging options are based on predefined bag sizes (1g, 2g, 3g, 5g, 10g, 20g, 50g, 100g, 500g, 1kg). The script calculates the minimum number of bags needed to fulfill an order.

## Getting Started

To run this script, **YOU NEED [PYTHON](https://www.python.org/downloads/) INSTALLED** on your machine. Follow these steps:

1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Run the script using Python:
```sh
python ddsAssistantv0-0-2.py
```
