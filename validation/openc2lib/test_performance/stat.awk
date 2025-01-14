BEGIN {
	print "\tEncoding\t\tDecoding"
	for (i = 1; i <= 2; i++) {
		tot[i] = 0
		count[i] = 0
		min[i] = 3 #9999999999
		max[i] = 0
	}

	# This is necessary to read microseconds with the necessary precision
	CONVFMT = "%2.6f"

}

/^Encoding/ {
	diff = $2
	tot[1] += diff
	if ( diff < min[1] ) 
		min[1] = diff
	if ( diff > max[1] )
		max[1] = diff
	count[1]++
}

/^Decoding/ {
	diff = $2
	tot[2] += diff
	if ( diff < min[2] ) 
		min[2] = diff
	if ( diff > max[2] )
		max[2] = diff
	count[2]++
}

END {
	printf("Count:\t")
	for (i = 1; i <= 2; i++) 
		printf("%d\t\t\t", count[i])
	printf("\n")
	printf("Total:\t")
	for (i = 1; i <= 2; i++) 
		printf("%f\t\t", tot[i])
	printf("\n")
	printf("Mean:\t")
	for (i = 1; i <= 2; i++) 
		printf("%f\t\t", tot[i]/count[i])
	printf("\n")
	printf("Min:\t")
	for (i = 1; i <= 2; i++) 
		printf("%f\t\t", min[i])
	printf("\n")
	printf("Max:\t")
	for (i = 1; i <= 2; i++) 
		printf("%f\t\t", max[i])
	printf("\n")
}
	
