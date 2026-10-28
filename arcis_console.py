#!/usr/bin/env python3
"""
Arcis Lowcap Autoswap Console
Local web UI for controlling the LowcapAutoswapper module.
Serves on 0.0.0.0:8080 for local network access.
"""

import json
import os
from decimal import Decimal
from flask import Flask, request, jsonify, render_template_string
from arcis_lowcap_autoswap import LowcapAutoswapper

app = Flask(__name__)
bot = LowcapAutoswapper(dry_run=True, base_coin="BTC")

HTML = """
<!DOCTYPE html>
<html><head><title>Arcis Lowcap Autoswap</title>
<style>body{font-family:sans-serif;background:#0d1117;color:#c9d1d9;padding:20px}button{background:#58a6ff;color:#fff;border:none;padding:8px 14px;border-radius:4px;cursor:pointer}input,select{background:#0d1117;color:#c9d1d9;border:1px solid #30363d;padding:6px;border-radius:4px}</style>
</head><body>
<h1>Arcis Lowcap Autoswap Console</h1>
<p>Dry-run mode. Local network console.</p>
<button onclick="fetch('/api/status').then(r=>r.json()).then(d=>alert(JSON.stringify(d,null,2)))">Status</button>
<button onclick="fetch('/api/scan',{method:'POST',headers:{'Content-Type':'application/json'},body:'{\"threshold\":1.0}'}).then(r=>r.json()).then(d=>alert(JSON.stringify(d,null,2)))">Scan</button>
<script>console.log('Arcis console ready')</script>
</body></html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/api/status")
def status():
    return jsonify({"dry_run": bot.dry_run, "base_coin": bot.base_coin, "mining_connected": bot.mining_connected})

@app.route("/api/scan", methods=["POST"])
def scan():
    results = bot.scan_and_autoswap(Decimal("1.0"))
    return jsonify({"results": results})

if __name__ == "__main__":
    print("Console on http://0.0.0.0:8080")
    app.run(host="0.0.0.0", port=8080, debug=False)
