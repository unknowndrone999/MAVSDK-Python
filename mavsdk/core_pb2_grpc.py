# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import core_pb2 as core_dot_core__pb2


class CoreServiceStub(object):
    """Access to the connection state and running plugins.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeConnectionState = channel.unary_stream(
                '/mavsdk.rpc.core.CoreService/SubscribeConnectionState',
                request_serializer=core_dot_core__pb2.SubscribeConnectionStateRequest.SerializeToString,
                response_deserializer=core_dot_core__pb2.ConnectionStateResponse.FromString,
                )
        self.ListRunningPlugins = channel.unary_unary(
                '/mavsdk.rpc.core.CoreService/ListRunningPlugins',
                request_serializer=core_dot_core__pb2.ListRunningPluginsRequest.SerializeToString,
                response_deserializer=core_dot_core__pb2.ListRunningPluginsResponse.FromString,
                )


class CoreServiceServicer(object):
    """Access to the connection state and running plugins.
    """

    def SubscribeConnectionState(self, request, context):
        """Subscribe to 'connection state' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRunningPlugins(self, request, context):
        """Get a list of currently running plugins.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeConnectionState': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeConnectionState,
                    request_deserializer=core_dot_core__pb2.SubscribeConnectionStateRequest.FromString,
                    response_serializer=core_dot_core__pb2.ConnectionStateResponse.SerializeToString,
            ),
            'ListRunningPlugins': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRunningPlugins,
                    request_deserializer=core_dot_core__pb2.ListRunningPluginsRequest.FromString,
                    response_serializer=core_dot_core__pb2.ListRunningPluginsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.core.CoreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CoreService(object):
    """Access to the connection state and running plugins.
    """

    @staticmethod
    def SubscribeConnectionState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.core.CoreService/SubscribeConnectionState',
            core_dot_core__pb2.SubscribeConnectionStateRequest.SerializeToString,
            core_dot_core__pb2.ConnectionStateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRunningPlugins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.core.CoreService/ListRunningPlugins',
            core_dot_core__pb2.ListRunningPluginsRequest.SerializeToString,
            core_dot_core__pb2.ListRunningPluginsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
