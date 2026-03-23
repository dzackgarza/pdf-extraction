# Zotero API Reference

Local Zotero instance for managing PDF extraction workflow.

## Base URL

```
https://zotero.dzackgarza.com/api/users/1049732
```

## Core Endpoints

### List Items

```bash
# All items (paginated)
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items?limit=100'

# Just keys (faster for enumeration)
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items?limit=500&format=keys'

# Filter by item type
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items?itemType=journalArticle&limit=100'

# Search by query
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items?q=quasi&limit=50'
```

### Get Specific Item

```bash
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items/{KEY}'
```

### Get Item Children (Attachments/Notes)

```bash
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/items/{KEY}/children'
```

### Collections

```bash
# List all collections
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/collections'

# Items in a collection
curl -s 'https://zotero.dzackgarza.com/api/users/1049732/collections/{KEY}/items?limit=500'
```

## Pagination

**Headers to check:**

```bash
curl -sI 'https://zotero.dzackgarza.com/api/users/1049732/items?limit=100'
```

- `Total-Results: N` - Total items available
- `Link: <...>; rel="next"` - Next page URL
- `Link: <...>; rel="last"` - Last page URL

**Parameters:**

- `limit=N` - Items per page (max 1000)
- `start=N` - Offset for pagination

**Fetch all items:**

```bash
for start in $(seq 0 500 5000); do
    curl -s "BASE/items?limit=500&start=$start" | jq -c '.[]'
done
```

## Query Parameters

| Parameter     | Example                        | Description                          |
| ------------- | ------------------------------ | ------------------------------------ |
| `limit`       | `limit=100`                    | Items per page                       |
| `start`       | `start=500`                    | Offset                               |
| `format`      | `format=keys`                  | Return just keys (newline-separated) |
| `itemType`    | `itemType=journalArticle,book` | Filter by type                       |
| `contentType` | `contentType=application/pdf`  | Filter attachments                   |
| `q`           | `q=search+term`                | Search query                         |
| `collection`  | `collection=KEY`               | Filter by collection                 |

## Common Workflows

### Find All Papers with PDF Attachments

```bash
# Get all items with PDF attachments
curl -s 'BASE/items?itemType=attachment&contentType=application/pdf&limit=1000' | \
  jq '[.[] | .data.parentItem] | unique'
```

### Find Items Missing Markdown Sidecars

```bash
# Parents with PDFs
curl -s 'BASE/items?itemType=attachment&contentType=application/pdf&limit=1000' | \
  jq -r '[.[] | .data.parentItem] | unique | sort' > /tmp/pdf-parents.txt

# Parents with markdowns
curl -s 'BASE/items?itemType=attachment&contentType=text/markdown&limit=1000' | \
  jq -r '[.[] | .data.parentItem] | unique | sort' > /tmp/md-parents.txt

# Find gaps
diff /tmp/pdf-parents.txt /tmp/md-parents.txt
```

### Get All Items in a Collection

```bash
# PDFs collection key: JEJSXB2N
> /tmp/collection-items.jsonl
for start in $(seq 0 500 5000); do
    items=$(curl -s "BASE/collections/JEJSXB2N/items?limit=500&start=$start")
    echo "$items" | jq -c '.[]' >> /tmp/collection-items.jsonl
    count=$(echo "$items" | jq 'length')
    [ "$count" -lt 500 ] && break
done

# Extract papers (not attachments)
jq -r 'select(.data.itemType != "attachment") | .data.key' /tmp/collection-items.jsonl
```

### Check Item Attachments

```bash
KEY="QWDFJHVD"
curl -s "BASE/items/$KEY/children" | jq '.[] | {
  type: .data.itemType,
  contentType: .data.contentType,
  filename: .data.filename,
  title: .data.title
}'
```

## Server File Locations

**SSH:** `dzack@ssh.dzackgarza.com`

| Location                         | Description                           |
| -------------------------------- | ------------------------------------- |
| `~/Zotero/storage/{KEY}/`        | PDF files organized by attachment key |
| `~/pdf-inputs/`                  | Input PDFs for extraction             |
| `~/pdf-outputs/{PDF-STEM}/auto/` | Extraction outputs                    |
| `~/pdf-extraction/`              | This repository                       |

**Find PDFs on server:**

```bash
ssh dzack@ssh.dzackgarza.com "find ~/Zotero/storage -name '*.pdf' | wc -l"
```

## Library Statistics

**As of 2026-03-23:**

| Metric                       | Count |
| ---------------------------- | ----- |
| Total items in library       | ~2860 |
| Items in "PDFs" collection   | 433   |
| Items with PDF attachments   | 338   |
| Items with markdown sidecars | 338   |
| PDFs synced to server        | 113   |
| Extractions completed        | 1     |

**Coverage:** 100% of PDFs have markdown sidecars (338/338)

## Item Types

Common types in the library:

- `journalArticle`
- `book`
- `preprint`
- `conferencePaper`
- `bookSection`
- `report`
- `thesis`
- `attachment` (PDFs, markdowns, etc.)
- `note`

## Attachment Content Types

- `application/pdf` - PDF files
- `text/markdown` - Extraction outputs
- `application/json` - Extraction metadata

## Rate Limiting

- Add `sleep 0.1-0.2` between requests when fetching children
- Batch requests where possible
- Use `format=keys` for fast enumeration

## Example: Full Extraction Queue

```bash
#!/bin/bash
BASE="https://zotero.dzackgarza.com/api/users/1049732"

# Get all papers in PDFs collection
curl -s "$BASE/collections/JEJSXB2N/items?limit=500" | \
  jq -r '.[] | select(.data.itemType != "attachment") | "\(.data.key)\t\(.data.title)"'

# For each, check if markdown exists
for key in $(curl -s "$BASE/collections/JEJSXB2N/items?limit=500&format=keys"); do
    children=$(curl -s "$BASE/items/$key/children")
    has_md=$(echo "$children" | jq '[.[] | select(.data.contentType == "text/markdown")] | length')

    if [ "$has_md" -eq 0 ]; then
        echo "MISSING: $key"
    fi
done
```
