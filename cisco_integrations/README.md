

# SPACES
These examples highlight how a user might phrase the request in natural language, prompting your ChatGPT-based assistant to call the relevant new Cisco Spaces function. You can adapt them exactly to your function names, parameter structure, and environment.

---

### 1) **Get Location Hierarchy**  
**User Query**:  
> "Please show me the entire location hierarchy structure (campuses, buildings, floors) from Cisco Spaces. I'd like to see the tenant ID for the root as well."

*(This would correspond to something like a `get_location_hierarchy` function, which calls `/v2/map/locationhierarchy?tenantId=XXXXXX` in the Cisco Spaces API.  If you store the `tenantId` in your environment or function arguments, the user might only need to say "show me the entire location hierarchy.")*

---

### 2) **Get Floor Details**  
**User Query**:  
> "Fetch the details for the floor ID `4cdac97a-5b9b-43ff-a82c-e4a2f1d6efed` in Cisco Spaces."

*(Matches your existing function `get_spaces_floor_details`, which calls `/v2/map/floor/{floorId}`.)*

---

### 3) **Retrieve Floor Image**  
**User Query**:  
> "Get me the floor image for tenant ID `12345`, with imagePath `myMapStore/floor394.png` and imageType `png` from Cisco Spaces. I'd like to see the raw image or a direct link if possible."

*(This could correspond to a new function, e.g. `get_floor_image`, hitting `/v2/map/floor/image?tenantId=...&imagePath=...&imageType=...`.)*

---

### 4) **List Devices**  
**User Query**:  
> "Show me all CLIENT devices associated with floor ID `abc123-floor-99` in Cisco Spaces. Limit to 500 records on page 1."

*(This might call something like `get_devices`, or `get_spaces_devices`, that queries `/v2/devices?deviceType=CLIENT&floorId=abc123-floor-99&page=1&limit=500`.)*

---

### 5) **Get Devices Count**  
**User Query**:  
> "How many BLE tags do we have in building ID `bld-1002`? Could you give me a breakdown by floor as well?"

*(You might call a function like `get_devices_count` that hits `/v2/devices/count?deviceType=TAG&buildingId=bld-1002&groupBy=floorId` for the grouped results.)*

---

### 6) **Get Floors That Have Devices**  
**User Query**:  
> "Which floors currently have any active devices? I'd like a list of all such floor IDs."

*(This might map to a function like `get_devices_floors` that calls `/v2/devices/floors` to retrieve the set of floor IDs that have devices.  Possibly you then show that list to the user.)*

---

### 7) **Export Device History (CSV)**  
**User Query**:  
> "Export the last 4 hours of history for deviceType=CLIENT, in CSV format, from floor ID `floor-a1b2c3`. Let's do a time range from 1684828800000 to 1684843200000."

*(This might call a function like `export_device_history_csv`, which requests `/v2/history/record/export?formatType=csv&deviceType=CLIENT&floorId=floor-a1b2c3&startTime=1684828800000&endTime=1684843200000`, etc. Then you'd handle the resulting file or link.)*

---

### 8) **Export Device History (GZIP)**  
**User Query**:  
> "Could you download the last 24 hours of tag history in gzipped format? The building ID is `bld-123`, deviceType=TAG, and we want the data from 1685164800000 to 1685251200000."

*(Corresponds to a function like `export_device_history_gz`, which hits `/v2/history/record/export?deviceType=TAG&...` but without `formatType=csv`. This variant can return a large gzipped file with up to 5 million records.)*

---

### 9) **Count History Records**  
**User Query**:  
> "How many historical records exist for floor `xyz-floor-777` in the last 8 hours for deviceType=CLIENT? Please do not exceed a 1-day range."

*(A function like `get_history_record_count` might call `/v2/history/record/count?deviceType=CLIENT&floorId=xyz-floor-777&startTime=...&endTime=...` to retrieve the count of records within that time.)*

---

### 10) **Get List of Historical Devices**  
**User Query**:  
> "Show me all the client MAC addresses that have been on campus `campus-55` during the last day. I'd also like to see any associated AP MAC if available."

*(This might call `get_history_devices` hitting `/v2/history/devices?campusId=campus-55&deviceType=CLIENT&startTime=...&endTime=...&includeDetails=true`, etc.)*

---

### 11) **Get Single Device's History**  
**User Query**:  
> "Give me the 24-hour history for device ID `00:12:b8:0a:c6:20` in Cisco Spaces. If possible, show me the x,y coordinates and floor transitions."

*(That would be a function like `get_single_device_history`, making a request to `/v2/history/device/{deviceId}?startTime=...&endTime=...&includeDetails=true` or similarly specifying query parameters for associated, floor, SSID, etc.)*

---



# Meraki 
Below is sample documentation that describes the natural‐language queries a user might ask—and how those queries map to each of the new functions you added. You can adjust the wording to match your exact API parameter names and expected behavior.

### How These Queries Map to Functions

- **Queries #1–#3**: revolve around location hierarchy or retrieving a specific floor/floor image.  
- **Queries #4–#6**: revolve around `devices` resources.  
- **Queries #7–#11**: revolve around `history` resources (CSV exports, GZIP exports, counting records, listing historical devices, or fetching a single device’s detailed history).
---

### 1) **Get Organization Details**  
**User Query**:  
> "Show me the details for organization ID `ORG123`."  

**Description**:  
This query maps to the `get_organization` function. The assistant will call this function with the provided organization ID (for example, `ORG123`) to fetch a detailed overview (using the Meraki organizations API).

---

### 2) **List Organization Networks**  
**User Query**:  
> "List all the networks in my organization."  

**Description**:  
This query maps to the `get_organization_networks` function. The function retrieves a list of all networks configured in your Meraki environment.

---

### 3) **List Inventory Devices**  
**User Query**:  
> "What devices do we have in our inventory?"  

**Description**:  
This maps to the `get_organization_inventory_devices` function. It will return a list of all devices (from the Catalyst inventory) assigned to your organization.

---

### 4) **Search for a Client**  
**User Query**:  
> "Find the client details for 'John Doe'."  
>  
> or  
>  
> "Search for the client with MAC address `00:11:22:33:44:55`."  

**Description**:  
This query maps to the `get_organization_clients_search` function. It accepts a search term (a name or a MAC address) and returns matching client records.

---

### 5) **License Overview**  
**User Query**:  
> "Give me an overview of our license usage and status."  

**Description**:  
This query maps to the `get_organization_licenses_overview` function. Although currently a stub, it is meant to return the total number of licenses, the number of active licenses, expired licenses, and those expiring soon.

---

### 6) **Get Network Alerts History**  
**User Query**:  
> "Show me the alert history for network `NET456`."  

**Description**:  
This maps to the `get_network_alerts_history` function. It accepts a network ID (here, `NET456`) and returns the historical alert events for that network. (Currently a stub that you can later integrate with a real alert history API.)

---

### 7) **List Network Clients**  
**User Query**:  
> "List all clients connected to network `NET456`."  

**Description**:  
This maps to the `get_network_clients` function. It filters client records (from Catalyst) by the given network ID so that you see only those connected to that specific network.

---

### 8) **Summarize Network Health**  
**User Query**:  
> "What’s the overall health of my networks? How many are online versus offline?"  

**Description**:  
This query maps to the `get_organization_summary_top_networks_by_status` function. The assistant will return an aggregated view (for example, counts of online and offline networks) to give you an overall network health overview.

---

### 9) **List Wireless SSIDs**  
**User Query**:  
> "What wireless SSIDs are configured in our environment?"  

**Description**:  
This maps to the `get_organization_wireless_ssids` function. It returns a list of all wireless SSID configurations (for example, by delegating to the Catalyst client’s `get_all_ssids` method).

---

### 10) **Get Inventory Device Details**  
**User Query**:  
> "Show me the inventory details for device ID `DEV789`."  

**Description**:  
This query maps to the `get_organization_inventory_device` function. It returns detailed information for the specified device using its unique device ID.

---

### 11) **Summarize Device Statuses**  
**User Query**:  
> "Provide a summary of all our device statuses – how many are online and how many are offline?"  

**Description**:  
This maps to the `get_organization_devices_statuses_overview` function. The function aggregates data from all inventory devices (e.g., from the Catalyst client) and returns counts of devices by status.

---

### 12) **Wireless Clients Overview by AP**  
**User Query**:  
> "How many clients are connected to access point `AP123`?"  

**Description**:  
This maps to the `get_organization_wireless_clients_overview_by_device` function. It returns client counts or summary information for a specified wireless device (AP).  
*(Currently a stub that you can later implement to call the actual wireless controller API.)*

---

### 13) **SSID Status on an AP**  
**User Query**:  
> "What is the status of the SSIDs on AP `AP123`?"  

**Description**:  
This maps to the `get_organization_wireless_ssids_statuses_by_device` function. The assistant will return details about each SSID (such as whether it is enabled or broadcasting) on that particular access point.

---

### 14) **Wireless Controller Overview**  
**User Query**:  
> "Show me a performance summary for the wireless controller with ID `CTRL01`."  

**Description**:  
This query maps to the `get_organization_wireless_controller_overview_by_device` function. It returns key performance metrics (e.g., CPU usage, memory usage, uptime) for the specified controller device.

---

### 15) **Top Clients by Usage**  
**User Query**:  
> "Which clients are using the most bandwidth?"  

**Description**:  
This maps to the `get_organization_summary_top_clients_by_usage` function. It returns a list of top clients sorted by data usage. *(Stub: later integrate with real usage analytics.)*

---

### 16) **Top Devices by Usage**  
**User Query**:  
> "List the devices that are consuming the most network traffic."  

**Description**:  
This maps to the `get_organization_summary_top_devices_by_usage` function. The assistant will return usage data for the top devices by traffic consumption. *(Stub.)*

---

### 17) **Top Applications by Usage**  
**User Query**:  
> "What applications are using the most data in our network?"  

**Description**:  
This maps to the `get_organization_summary_top_applications_by_usage` function. It returns a summary of application usage, highlighting the top data-consuming applications. *(Stub.)*

---

### 18) **Assurance Alerts Overview**  
**User Query**:  
> "What active assurance alerts do we have right now?"  

**Description**:  
This maps to the `get_organization_assurance_alerts_overview` function. It returns a high-level overview of current health or assurance alerts in your organization. *(Stub.)*

---

### 19) **Login Security Settings**  
**User Query**:  
> "What are our current login security settings? Do we enforce two-factor authentication?"  

**Description**:  
This query maps to the `get_organization_login_security` function. It retrieves the organization’s login security configuration (for example, two‐factor enforcement, password expiration, allowed IP ranges, etc.). *(Stub.)*

---

### How to Use These Queries

When a user types one of these queries into your chat interface, your AI assistant will analyze the text and—using the LLM with function definitions—determine which function to call. For example, if a user says, "List all networks in my organization," the assistant will call `get_organization_networks` without needing any extra parameters. Similarly, more specific queries (such as searching for a client or retrieving alerts) will trigger the corresponding function with parameters extracted from the natural language input.

You can update or expand these examples as you add more functions or refine the parameters for each endpoint. This documentation helps both developers and users understand how natural language maps to backend API calls in your Cisco Data Bridge AI Agent project.

 