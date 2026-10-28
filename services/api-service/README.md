# API service (Quarkus)

This Java service is the HTTP API layer for the project. It runs alongside the existing Python AI service; `AI_SERVICE_URL` is the configured base URL for connecting them when AI endpoints are defined.

## Requirements

- JDK 17 or newer
- Maven 3.9.16 or newer

## Run locally

From this directory:

```powershell
$env:QUARKUS_HTTP_PORT = "8081"
$env:AI_SERVICE_URL = "http://localhost:8000"
mvn quarkus:dev
```

The API responds at `http://localhost:8081/api/health`. Quarkus SmallRye Health provides readiness and liveness endpoints under `http://localhost:8081/q/health`.

`AI_SERVICE_URL` currently records the intended AI-service address. The Python service has no application endpoints yet, so no API-to-AI calls are made until those contracts exist.
