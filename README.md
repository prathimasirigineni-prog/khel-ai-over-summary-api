# Khel AI - Over Summary API

## Phase 2 - Integration-Ready Version

## Objective

The Over Summary API provides an integration-ready, over-by-over summary of a cricket innings. It accepts an innings identifier together with raw ball-event data and dynamically groups those events by over, calculating runs, wickets, and extras while preserving the individual ball details. The response is structured for direct use by Khel AI frontend components, Django orchestration, live timelines, and chart-based visualizations.

## Phase 1 to Phase 2 Changes

The Phase 1 implementation used hardcoded innings and over data inside the service layer.

The Phase 2 implementation removes that hardcoded demo dependency and accepts ball-event data through a validated request payload.

The over summaries are now calculated dynamically from the supplied events.

## Integration Flow

Django / Khel AI Backend
        |
        v
Over Summary API
        |
        v
Service Layer
        |
        v
Over-by-Over Summary
        |
        v
Frontend / Timeline / Charts

## Endpoint

POST /innings/{innings_id}/overs

## Example

POST /innings/1/overs

## Request Data

The request contains:

- innings_id
- ball_events
- over_ball
- striker
- bowler
- runs
- extras
- is_legal
- extra_type
- wicket
- label

## Response

The API returns:

- Over number
- Total runs in the over
- Wickets in the over
- Extras in the over
- Ball-by-ball information
- Human-friendly ball labels

## Business Logic

The service layer:

1. Groups ball events by over number.
2. Calculates total runs for each over.
3. Counts wickets for each over.
4. Calculates extras for each over.
5. Preserves the ball-level event information.
6. Returns the over summaries in chronological order.

## Integration Readiness

The API does not depend on a hardcoded innings dictionary.

Incoming data is validated through Pydantic schemas, making the API suitable for structured data supplied by the Khel AI backend or Django integration layer.

The response structure can be consumed directly by frontend timeline and chart components without requiring the frontend to perform the over calculations.

## Error Handling

The API returns HTTP 400 when the URL innings ID does not match the innings ID in the supplied payload.

The API returns HTTP 404 when no ball-event data is available for the requested innings.

## Run Locally

uvicorn main:app --reload

## Swagger Documentation

/docs

## Version

2.0.0