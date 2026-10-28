# Arcis Lowcap Autoswap

Technical reference for the low-cap PoW coin monitoring, local-wallet send, and exchange autoswap system.

Version: 2026-10-27  
Default mode: dry-run  
Mining marker: Mining-Dutch default pool (europe.mining-dutch.nl:9996)

## Contents

1. Overview
2. Files
3. Installation
4. Configuration
5. Local wallets
6. Console
7. API
8. Safety

## Overview

Watches registered addresses for low-cap coins, optionally sends funds from local wallets to exchange deposit addresses, and places swaps to a base coin (BTC, USDT, or USDC).

Supported exchanges: NonKYC, XeggeX, AltQuick, TradeOgre, CoinEx.

Local wallet RPC:
- ARRR (Pirate Chain) - port 45453, method z_sendmany
- FLO (Florincoin) - port 7313, method sendtoaddress

## Files

- arcis_lowcap_autoswap.py - core module
- arcis_console.py - Flask console on port 8080
- Arcis_Lowcap_Autoswap_Manual.md - this document

## Installation

```
pip install requests flask
python3 arcis_lowcap_autoswap.py
python3 arcis_console.py
```

Console: http://127.0.0.1:8080

## Configuration

Dry-run is the default. Set dry_run=False and provide API keys for live operation.

## Local wallets

RPC configuration for ARRR and FLO is supported. Explorer fallback is used when RPC is not configured.

## Console

The console provides status, market browser, manual swap, local wallet controls, and scan history.

## API

Endpoints include /api/status, /api/scan, /api/swap, /local_wallet, /send_to_exchange.

## Safety

Dry-run is the default. Live operations require dry_run=False and valid credentials. API secrets are masked in the UI. Test with small amounts before production use.
