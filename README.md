# Research Intelligence

Research Intelligence is split into two services:

- `services/api-service`: Java 17+ HTTP API built with Quarkus. It exposes `/api/health` and Quarkus health checks at `/q/health`.
- `services/ai-service`: Python service for AI functionality (API integration will be added when its endpoints are defined).

## API service

The API service uses Maven and Quarkus. From `services/api-service`, run:

```powershell
$env:QUARKUS_HTTP_PORT = "8081"
$env:AI_SERVICE_URL = "http://localhost:8000"
mvn quarkus:dev
```

The API listens on `http://localhost:8081`. `AI_SERVICE_URL` configures the Quarkus REST client base URL for future AI-service calls. The Python service does not expose application endpoints yet, so the API currently does not call it.

Requirements: JDK 17 or newer and Maven 3.9.16 or newer.

See [the API service README](services/api-service/README.md) for service-specific details.
