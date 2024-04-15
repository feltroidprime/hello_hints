from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
import math
from hints.utils import felt252_to_uint64


# Implement the ExampleService
class ExampleService(service_pb2_grpc.SqrtOracleServicer):
    def Sqrt(self, request, context):
        if request.n < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Negative numbers cannot have a square root.")
            return service_pb2.Response()
        sqrt_value = math.sqrt(request.n)
        return service_pb2.Response(value=felt252_to_uint64(int(sqrt_value)))


# Create a function to serve the service
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SqrtOracleServicer_to_server(ExampleService(), server)
    server.add_insecure_port("[::]:3000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
