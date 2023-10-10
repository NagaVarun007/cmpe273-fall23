import grpc
import googlemap_pb2
import googlemap_pb2_grpc

def clientdumy():
    channel = grpc.insecure_channel('localhost:50051')
    stub = googlemap_pb2_grpc.ValidateAddressServiceStub(channel)
    address = "1326, The Alameda, San Jose"  
    response = stub.ValidateAddress(googlemap_pb2.ValidateAddressRequest(address=address))
    if response.is_valid:
        print(f" '{address}' is valid.")
    else:
        print(f" '{address}' is not valid.")

if __name__ == '__main__':
    clientdumy()