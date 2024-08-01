BEGIN {
	print "Command ready\t\tSending\t\t\tGot response\t\tResponse decoded"
}

/root: Sending command/ {
	sending = $1
}

/http_transfer: Sending to/ {
	transfering = $1
}

/http_transfer: HTTP got response/ {
	gotresponse = $1
}

/root: Got response/ {
	response = $1
	dump(sending, transfering, gotresponse, response)
}


	
function dump(sending, transfering, gotresponse, response)
{
	print sending "\t" transfering "\t" gotresponse "\t" response 
}
