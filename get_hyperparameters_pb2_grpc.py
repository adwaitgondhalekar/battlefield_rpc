# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import get_hyperparameters_pb2 as get__hyperparameters__pb2


class Get_HyperParamsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_hyperparams = channel.unary_unary(
                '/Get_HyperParams/get_hyperparams',
                request_serializer=get__hyperparameters__pb2.param_request.SerializeToString,
                response_deserializer=get__hyperparameters__pb2.hyperparams.FromString,
                )


class Get_HyperParamsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_hyperparams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Get_HyperParamsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_hyperparams': grpc.unary_unary_rpc_method_handler(
                    servicer.get_hyperparams,
                    request_deserializer=get__hyperparameters__pb2.param_request.FromString,
                    response_serializer=get__hyperparameters__pb2.hyperparams.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Get_HyperParams', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Get_HyperParams(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_hyperparams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Get_HyperParams/get_hyperparams',
            get__hyperparameters__pb2.param_request.SerializeToString,
            get__hyperparameters__pb2.hyperparams.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
