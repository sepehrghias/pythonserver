from concurrent import futures
import json
import grpc

from test import ad_pb2
from test import ad_pb2_grpc


class AdWithCpc:
    def get_ad_by_cpc(self, request, context):
        with open("data.json", "r") as f:
            data = json.load(f)
        data.sort(key=lambda x: x["cpc"], reverse=True)
        if request.min_cpc > data[0]["cpc"]:
            return ad_pb2.Ad_Reply()
        return ad_pb2.Ad_Reply(title=data[0]["title"], image=data[0]["image"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ad_pb2_grpc.add_AdsWithCpcServicer_to_server(AdWithCpc(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
