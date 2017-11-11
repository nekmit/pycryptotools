# Make Crypto API Nicer (MCAN)
***

MCAN uses the Flask library and the CoinMarketCap API to make a new API that makes things simpler and easier to use.

Path: `/<coin>`

### Parameters

- `coin_used`, what coin was put in the directory
- `price_cad`, coin's value in Canadian dollars
- `price_usd`, coin's value in American dollars
- `coins_left`, the amount of coins not mined left
- `latest_change`, latest change in an hour (in %)
