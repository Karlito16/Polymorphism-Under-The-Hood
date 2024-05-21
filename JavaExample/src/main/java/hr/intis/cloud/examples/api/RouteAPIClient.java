package hr.intis.cloud.examples.api;

public class RouteAPIClient implements BasicAPIClient {

    public RouteAPIClient() {
    }

    @Override
    public String getServiceName() {
        return "Route";
    }

    @Override
    public int connect() {
        System.out.printf("Connecting to %s...\n", getServiceName());
        System.out.println("Connected!");
        return 0;
    }

    @Override
    public int get(String url) {
        System.out.printf("Sending HTTP-GET request to %s: %s\n", getServiceName(), url);
        return 200;
    }

    @Override
    public int disconnect() {
        System.out.printf("Disconnecting from %s...\n", getServiceName());
        System.out.println("Disconnected!");
        return 0;
    }
}
