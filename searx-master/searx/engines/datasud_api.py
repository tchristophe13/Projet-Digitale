#DataSud
#
# @website     https://www.datasud.fr/
# @provide-api yes (http://trouver.datasud.fr/api/3/action/)
#
# @using-api   yes
# @results     JSON
# @stable      yes

#search-url
api_key=None

from searx.url_utils import urlencode

search_url = 'http://trouver.datasud.fr/api/3/action/resource_search?{query}'

# do search-request
def request(query, params):
    params['url'] = search_url.format(query=urlencode({'q': query}),
                                      api_key=api_key)
    return params

# get response from search-request
def response(resp):
    results = []

    search_results = resp["results"]
    if not(resp["count"]):
        return []
    else:
        results.append(search_results)
        return results