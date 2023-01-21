curl -XPOST -u 'master-mohi:Master@123@Mohi' 'domain-endpoint/_bulk' --data-binary @bulk_movies.json -H 'Content-Type: application/json'

curl -XPUT -u 'master-mohi:Master@123@Mohi' 'https://search-movies-opensearch-775j5ozskq7zwp4nqmfqtyi2ue.us-east-1.es.amazonaws.com/movies/_doc/1' -d '{"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}' -H 'Content-Type: application/json'

curl -XPOST -u 'master-mohi:Master@123@Mohi' 'https://search-movies-opensearch-775j5ozskq7zwp4nqmfqtyi2ue.us-east-1.es.amazonaws.com/_bulk' --data-binary @bulk_movies.json -H 'Content-Type: application/json'

curl -XGET -u 'master-mohi:Master@123@Mohi' 'https://search-movies-opensearch-775j5ozskq7zwp4nqmfqtyi2ue.us-east-1.es.amazonaws.com/_bulk/movies/_search?q=mars&pretty=true'

curl -XGET -u 'master-mohi:Master@123@Mohi' 'https://search-movies-opensearch-775j5ozskq7zwp4nqmfqtyi2ue.us-east-1.es.amazonaws.com/_bulk/movies/_search?q=rebel&pretty=true'


