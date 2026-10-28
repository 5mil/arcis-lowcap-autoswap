# Arcis Lowcap Autoswap

Technical reference for the low-cap PoW coin monitoring, local-wallet send, and exchange autoswap system.

Version: 2026-10-27
Default mode: dry-run
Mining marker: Mining-Dutch default pool (europe.mining-dutch.nl:9996)

## Overview

Watches registered addresses for low-cap coins, optionally sends funds from local wallets to exchange deposit addresses, and places swaps to a base coin (BTC, USDT, or USDC).

Supported exchanges: NonKYC, XeggeX, AltQuick, TradeOgre, CoinEx.

Local wallet RPC:
- ARRR (Pirate Chain) - port 45453, method z_sendmany
- FLO (Florincoin) - port 7313, method sendtoaddress

## Quick Start

```
python3 arcis_lowcap_autoswap.py
python3 arcis_console.py
```

Console: http://127.0.0.1:8080

## Files

- arcis_lowcap_autoswap.py - core module
- arcis_console.py - Flask console on port 8080
- Arcis_Lowcap_Autoswap_Manual.md - this document

## Safety

Dry-run is the default. Live operations require dry_run=False and valid credentials.
