/^Encoding started/ {
	start = $2
}
/^Encoding ended/ {
	print "Encoding: ", $2-start
}
/^Decoding started/ {
	start = $2
}
/^Decoding ended/ {
	print "Decoding: ", $2-start
}


