package hr.intis.cloud.examples.api;

public interface BasicAPIClient {

    String getServiceName();

    int connect();

    int get(String url);

    int disconnect();
}
