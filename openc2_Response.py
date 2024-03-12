import json


class OpenC2Response:
    # Enumerate status codes and descriptions
    STATUS_CODES = {
        102: "Processing command - the Consumer has accepted the Command but has not yet completed it",
        200: "OK - the Command has succeeded",
        400: "Bad Request - the Consumer cannot process the Command",
        401: "Unauthorized - invalid authentication credentials",
        403: "Forbidden - Command understood but refused",
        404: "Not Found - Nothing matching the Command",
        500: "Internal Error - unexpected condition encountered",
        501: "Not Implemented - functionality not supported",
        503: "Service Unavailable - temporary overloading or maintenance"
    }

    def __init__(self, status_code, data=None, versions="1.0", profiles=None, pairs=None, rate_limit=None, slpf=None):
        if status_code not in self.STATUS_CODES:
            raise ValueError("Invalid status code from Consumer")
        self.status_code = status_code
        self.status_text = self.STATUS_CODES[status_code]
        self.data = data
        self.results = {
            "versions": versions,
            "profiles": profiles,
            "pairs": pairs,
            "rate_limit": rate_limit,
            "slpf": slpf
        }

   # result part still need modify
    
    def response_to_json(self):
        # Convert the OpenC2 response to a JSON format.
        response = {
            "status": self.status_code,
            "status_text": self.status_text,
             "results": self.results
        }
        if self.data is not None:
            response["data"] = self.data
        return json.dumps(response, indent=4)


    def __str__(self):
        return f"OpenC2 Response: Status " \
               f"{self.status_code} - " \
               f"{self.status_text}," \
               f" Data: {self.data}"





response = OpenC2Response(
    status_code=500,
)

response_json = response.response_to_json()
print("OpenC2 Command Response (JSON):")
print(response_json)
print("\nString Representation:")
print(response)
