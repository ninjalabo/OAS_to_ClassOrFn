# OAS -> Class
```shell
	wget https://tie.digitraffic.fi/swagger/openapi.json
	docker run --rm -v $PWD:/local openapitools/openapi-generator-cli generate -i /local/openapi.json -g python -o /local/out/python
```
# OAS -> Fn
```shell
	openapi-python-generator https://tie.digitraffic.fi/swagger/openapi.json Fn
```
