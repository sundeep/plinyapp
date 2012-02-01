# Function: fuck around with pliny

import tracking_helper as th


def main():
	# get email  	
	em = th.Email("sun@s.com","delivery@fedex.com","Hello friend, tracking number : 1Z18X70Y0400635812 From, fedex.com")
	
	# try shit out
	th.parseEmailforTrackingFlow(em)


if __name__ == "__main__":
	main()
