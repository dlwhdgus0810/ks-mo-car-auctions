"""Tag the Facebook Marketplace listings added on 2026-09-28 so the site can show them on their own (marketplace.html#fb-new).

They are the 185 rows appended by scripts/add-marketplace-5k-8k-sep28.py, the only rows posted within 4 days of 9/28.
"""
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'dist' / 'marketplace-2026-09-23.json'
d = json.loads(path.read_text())
new = [x for x in d['listings'] if x['days'] <= 4]
assert len(new) == 185 and new == d['listings'][-185:] and not any('added' in x for x in d['listings']), 'One-time migration'
for x in new:
    x['added'] = '2026-09-28'
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f'tagged {len(new)}')
