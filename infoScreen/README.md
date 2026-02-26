# Room availability board

A single-file Python web server that displays free/busy status for meeting rooms in Microsoft Exchange Online, using the Microsoft Graph API.

## Requirements

- Python 3.9+
- **Windows only:** `pip install tzdata`

## Azure setup

1. In the Azure portal, open the **"Room information"** App Registration
2. Go to **API permissions → Add a permission → Microsoft Graph → Application permissions**
3. Add `Calendars.ReadBasic.All`
4. Click **Grant admin consent for [your organisation]**

## Configuration

The server reads credentials from environment variables:

| Variable | Description |
|---|---|
| `AZURE_TENANT_ID` | Your Azure tenant ID |
| `AZURE_CLIENT_ID` | App registration client ID |
| `AZURE_CLIENT_SECRET` | App registration client secret value |

## Running

**macOS / Linux**
```bash
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
python3 server.py
```

**Windows (PowerShell)**
```powershell
$env:AZURE_TENANT_ID="your-tenant-id"
$env:AZURE_CLIENT_ID="your-client-id"
$env:AZURE_CLIENT_SECRET="your-client-secret"
python3 server.py
```

Then open [http://localhost:8888](http://localhost:8888) in a browser.

## Rooms

Rooms are defined in the `GROUPS` list at the top of `server.py`. Each room needs a display name and its Exchange email address. Rooms are organised into named groups which appear as separate sections on the page.
