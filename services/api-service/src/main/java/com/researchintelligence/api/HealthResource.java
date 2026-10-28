package com.researchintelligence.api;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/api")
public class HealthResource {

    @GET
    @Path("/health")
    @Produces(MediaType.APPLICATION_JSON)
    public HealthStatus health() {
        return new HealthStatus("ok", "research-intelligence-api");
    }

    public record HealthStatus(String status, String service) {
    }
}
