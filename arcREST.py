#-------------------------------------------------------------------------------
# Name:        arcREST
# Purpose:     update AGOL features
#
# Author:      mostynl
#
# Created:     24/08/2015
# Copyright:   (c) mostynl 2015
# Licence:     NZ Creative Commons 3.0
#-------------------------------------------------------------------------------

from arcrest.security import AGOLTokenSecurityHandler
from arcrest.manageorg import Administration
if __name__ == "__main__":
    username = "username"
    password = "password"
    proxy_port = None
    proxy_url = None    
    securityHandler = AGOLTokenSecurityHandler(username, password,
                                               proxy_url=proxy_url,
                                               proxy_port=proxy_port)
    siteObject = Administration(securityHandler=securityHandler,
                                proxy_url=proxy_url,
                                proxy_port=proxy_port)
    results = siteObject.query(q="< some query string >")