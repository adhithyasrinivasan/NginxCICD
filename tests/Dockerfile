FROM gcr.io/gcp-runtimes/container-structure-test:latest

FROM ubuntu:20.04
COPY --from=0 /container-structure-test /container-structure-test
CMD ["/container-structure-test"]