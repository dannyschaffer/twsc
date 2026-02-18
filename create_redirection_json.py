import csv
import json

csv_path = 'redirects.csv'

json_path = 'redirection-fixes-import.json'

redirects = []

with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        source = row['source']
        target = row['target']
        
        # Ensure target is absolute path if it's relative
        if not target.startswith('http') and not target.startswith('/'):
            target = '/' + target

        item = {
            "url": source,
            "match_url": source,
            "match_data": {
                "source": {
                    "flag_query": "pass",
                    "flag_case": True,
                    "flag_trailing": True,
                    "flag_regex": False
                }
            },
            "action_code": 301,
            "action_type": "url",
            "action_data": {
                "url": target
            },
            "match_type": "url",
            "title": "Manual Fix - Feb 18",
            "hits": 0,
            "regex": False,
            "group_id": 1,
            "position": 0,
            "enabled": True
        }
        redirects.append(item)

# Create the full JSON structure required by Redirection plugin
output = {
    "plugin": {
        "version": "5.5.0",
        "date": "2026-02-18 10:00:00"
    },
    "groups": [
        {
            "id": 1,
            "name": "Redirections",
            "redirects": len(redirects),
            "module_id": 1,
            "moduleName": "WordPress",
            "enabled": True
        }
    ],
    "redirects": redirects
}

with open(json_path, 'w') as f:
    json.dump(output, f, indent=4)

print(f"Created {json_path} with {len(redirects)} rules.")
