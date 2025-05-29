from otupy.types.base import Enumerated

class PeerRole(Enumerated):

	client = 1 #The consumer operates as a client in the client-server model in this link
	server = 2 #The consumer operates as a server in the client-server model in this link
	guest = 3 #The service is hosted within another service.
	host = 4 #The service hosts another service
	ingress = 5 #ingress communication    
	egress = 6 #egress communication
	both = 7 #Both ingress and egress communication
	control = 8 #the service controls another service
	controlled = 9 #the service is controlled by another service

	

