while read dom ;
	do
echo $dom
		python ~/tools/github-search/github-subdomains.py -t <token> -d $dom
        
done < $1
