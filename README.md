# Khel AI - Over Summary API

## Objective

The Over Summary API provides an over-by-over summary of a cricket innings. It groups ball events by over and returns runs, wickets, extras, and ball-level labels in a structure suitable for timeline and chart visualizations.

## Endpoint

GET /innings/{innings_id}/overs

## Example

GET /innings/1/overs

## Response

The API returns:

- Over number
- Total runs in the over
- Wickets in the over
- Extras in the over
- Ball-by-ball summaries
- Human-friendly ball labels

## Run locally

uvicorn main:app --reload

## Swagger documentation

/docs