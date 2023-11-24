while read dom ;
	do
echo $dom
		python ~/tools/github-search/github-subdomains.py -t $2 -d $dom
        
done < $1
