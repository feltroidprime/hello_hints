import grpc
import service_pb2
import service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:3000") as channel:
        stub = service_pb2_grpc.SqrtOracleStub(channel)
        value = 100
        print(f"Client sends: {value}")
        response = stub.Sqrt(service_pb2.Request(n=value))
        print(f"Client received: {response.value}")


if __name__ == "__main__":
    run()
