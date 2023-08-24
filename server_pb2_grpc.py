# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class ServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/colbert.Server/Search',
                request_serializer=server__pb2.Query.SerializeToString,
                response_deserializer=server__pb2.QueryResult.FromString,
                )
        self.Rerank = channel.unary_unary(
                '/colbert.Server/Rerank',
                request_serializer=server__pb2.Query.SerializeToString,
                response_deserializer=server__pb2.QueryResult.FromString,
                )


class ServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rerank(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=server__pb2.Query.FromString,
                    response_serializer=server__pb2.QueryResult.SerializeToString,
            ),
            'Rerank': grpc.unary_unary_rpc_method_handler(
                    servicer.Rerank,
                    request_deserializer=server__pb2.Query.FromString,
                    response_serializer=server__pb2.QueryResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'colbert.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/colbert.Server/Search',
            server__pb2.Query.SerializeToString,
            server__pb2.QueryResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Rerank(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/colbert.Server/Rerank',
            server__pb2.Query.SerializeToString,
            server__pb2.QueryResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)