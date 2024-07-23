from concurrent import futures
import json
import grpc

from protos import ad_pb2
from protos import ad_pb2_grpc


class AdRetriever:
    def get_ads(self, request, context):
        with open("data.json", "r") as f:
            data = json.load(f)
        data.sort(key=lambda x: x["cpc"], reverse=True)
        if request.min_cpc > data[0]["cpc"]:
            return ad_pb2.TargetingResponse()
        return ad_pb2.TargetingResponse(title=data[0]["title"], image=data[0]["image"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ad_pb2_grpc.add_AdRetrieverServicer_to_server(AdRetriever(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
