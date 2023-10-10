import grpc
from concurrent import futures
import googlemap_pb2
import googlemap_pb2_grpc
from geopy.geocoders import GoogleV3

class ValidateAddressService(googlemap_pb2_grpc.ValidateAddressServiceServicer):
    
    def __init__(self):
        self.geocoder = GoogleV3(api_key="AIzaSyARl-FlrLz2vhDPPejk8B4XS9eix5sm5K0")

    def ValidateAddress(self, request, context):
        
        address = request.address
        try:
            
            location = self.geocoder.geocode(address)

            if location:
                
                validated_address = location.address
                return googlemap_pb2.ValidateAddressResponse(
                    is_valid=True,
                    validated_address=validated_address
                )
            else:
                
                return googlemap_pb2.ValidateAddressResponse(
                    is_valid=False,
                    validated_address=""
                )
        except Exception as e:
            
            print(f"Error while geocoding: {e}")
            return googlemap_pb2.ValidateAddressResponse(
                is_valid=False,
                validated_address=""
            )
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    googlemap_pb2_grpc.add_ValidateAddressServiceServicer_to_server(ValidateAddressService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server terminated by user.")
    except Exception as e:
        print(f"Error in server: {e}")
   


if __name__ == '__main__':
    serve()
