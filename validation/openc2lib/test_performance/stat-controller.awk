BEGIN {
	print "\tEncoding+headers\tSend-to-Receive\t\tDecoding\tTot. Transaction"
	for (i = 1; i <= 4; i++) {
		tot[i] = 0
		count = 0
		min[i] = 3 #9999999999
		max[i] = 0
	}

	# This is necessary to read microseconds with the necessary precision
	CONVFMT = "%2.6f"

}

/^[0-9]/ {
	for (i = 1; i <= 4; i++) {
		if ( i != 4 )
			diff = $(i+1) - $i
		else
			diff = $4 - $1
		tot[i] += diff
		if ( diff < min[i] ) 
			min[i] = diff
		if ( diff > max[i] )
			max[i] = diff
	}
	count++
}

END {
	printf("Count:\t")
	for (i = 1; i <= 4; i++) 
		printf("%d\t\t", count)
	printf("\n")
	printf("Total:\t")
	for (i = 1; i <= 4; i++) 
		printf("%f\t\t", tot[i])
	printf("\n")
	printf("Mean:\t")
	for (i = 1; i <= 4; i++) 
		printf("%f\t\t", tot[i]/count)
	printf("\n")
	printf("Min:\t")
	for (i = 1; i <= 4; i++) 
		printf("%f\t\t", min[i])
	printf("\n")
	printf("Max:\t")
	for (i = 1; i <= 4; i++) 
		printf("%f\t\t", max[i])
	printf("\n")
}
	
