# LAL
Lazy Asset Lunchmoney

LAL is a small script, that will automatically update your LunchMoney Asset's balance based on your excel input file.
This is specially helpful for records which do not get automatically updated with transactions through the PLAID integration.


## Installation

Download the 'main.py' file and place it in a folder together with your excel input file.

## Usage

Make sure you have python installed and all the required clients:

```python
pip install lunchable
pip install pandas
pip install python-csv
```
Execute the script directly from your file explorer

A developer access token is required. Go to https://my.lunchmoney.app/developers to generate one and paste it within the code.

The excel input file template can be downloaded from this repo. It should only contain the name of your asset and the amount you want to update.
Please be certain you use the exact name and that there are no empty characters.

## Limitations
This script has been created by a Python newbie.
Tested only under windows.

## Contributing
Happy to hear all the input you might. Still learning how to code!

## License
[MIT] (https://choosealicense.com/licenses/mit/)
