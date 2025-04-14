/http_transfer: Received HTTP body/ {
	received = $1
}

/http_transfer: Received command/ {
	gotcommand = $1
}

# In case of bad request, an error is returned
/http_transfer: Unable to understand/ {
	gotcommand = $1
}

/http_transfer: Got response/ {
	gotresponse = $1
}

/http_transfer: Sending response/ {
	sending = $1
	dump(received, gotcommand, gotresponse, sending)
}


	
function dump(received, gotcommand, gotresponse, sending)
{
	print received "\t" gotcommand "\t" gotresponse "\t" sending
}
