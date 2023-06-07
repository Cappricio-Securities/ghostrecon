while read dom ;
	do
echo $dom
		curl -s https://crt.sh/\?q\=$dom\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u 
        
done < $1
