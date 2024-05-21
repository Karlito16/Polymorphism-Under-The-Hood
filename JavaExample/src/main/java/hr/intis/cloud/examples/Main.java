package hr.intis.cloud.examples;

import hr.intis.cloud.examples.api.BasicAPIClient;
import hr.intis.cloud.examples.api.CWAAPIClient;
import hr.intis.cloud.examples.api.RouteAPIClient;


public class Main {

    public static void action(BasicAPIClient client, String url) {
        System.out.println();
        client.connect();
        int statusCode = client.get(url);
        System.out.printf("Action completed with status code: %d\n", statusCode);
        client.disconnect();
    }

    public static void main(String[] args) {
        BasicAPIClient cwa = new CWAAPIClient();
        BasicAPIClient route = new RouteAPIClient();

        action(cwa, "/api/v1/machines");
        action(route, "/api/v1/routes");
    }
}
