import commons
import sys
import logging
from login import login_to_captive_portal

logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
)

# make sure connected to campus-wifi
conn_status = commons.is_ssid_connected("CAMPUS WI-FI-1")
if not conn_status:
    logger.error("Not Connected to CAMPUS WI-FI-1")
    sys.exit("Not connected to CAMPUS WI-FI-1. Please try again after connecting")

logger.info("Connected to CAMPUS WI-FI")

if not commons.is_logged_in():
    logger.info('Attempting login')
    portal_address = commons.get_captive_portal_address()
    logger.info(f'Portal address: {portal_address}')

    try:
        login_to_captive_portal(portal_address=portal_address)
    except Exception as e:
        logger.error(f'Error while logging to campus wifi: ')
        sys.exit(1)
    
    finally:
        # check if logged in
        if commons.is_logged_in():
            logger.info("Successfully logged in")
        else:
            print("Could not login successfully")
            sys.exit(1)

logger.info("Already Logged in")
print("Logged in already")