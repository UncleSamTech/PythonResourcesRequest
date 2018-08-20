import urllib.request
def getResponseCodeMessage(url_addr):
	web_request = urllib.request.urlopen(url_addr)
	web_request  = web_request.getcode()
	if web_request == 100:
		return 'response code  = continue'
	elif web_request == 101:
		return 'response code  = switching protocol'
	elif web_request == 102:
		return 'response code  = processing'
	elif web_request == 200:
		return 'response code  = ok'
	elif web_request == 201:
		return 'response code  = created'
	elif web_request == 202:
		return 'response code  = accepted'
	elif web_request == 203:
		return 'response code  = non-authoritive information'
	elif web_request == 204:
		return 'response code  = no content'
	elif web_request == 206:
		return 'response code  = partial content'
	elif web_request == 207:
		return 'response code  = multi status'
	elif web_request == 208:
		return 'response code  = multi status'
	elif web_request == 226:
		return 'response code  = im used'
	elif web_request == 300:
		return 'response code  = multiple choice'
	elif web_request == 301:
		return 'response code  = moved permanently'
	elif web_request == 302:
		return 'response code  = found'
	elif web_request == 303:
		return 'response code  = see other'
	elif web_request == 304:
		return 'response code  = not found'
	elif web_request == 305:
		return 'response code  = use proxy'
	elif web_request == 306:
		return 'response code  = unused'
	elif web_request == 307:
		return 'response code  = temporary redirect'
	elif web_request == 308:
		return 'response code  = permanent redirect'
	elif web_request == 400:
		return 'response code  = bad request'
	elif web_request == 401:
		return 'response code  = unauthorized'
	elif web_request == 402:
		return 'response code  = payment required'
	elif web_request == 403:
		return 'response code  = forbidden'
	elif web_request == 404:
		return 'response code  = not found'
	elif web_request == 405:
		return 'response code  = method not allowed'
	elif web_request == 406:
		return 'response code  = not acceptable'
	elif web_request == 407:
		return 'response code  = proxy authentication'
	elif web_request == 408:
		return 'response code  = request timeout'
	elif web_request == 409:
		return 'response code  = conflict'
	elif web_request == 410:
		return 'response code  = gone'
	elif web_request == 411:
		return 'response code  = length required'
	elif web_request == 412:
		return 'response code  = precondition failed '
	elif web_request == 413:
		return 'response code  = payload too large'
	elif web_request == 414:
		return 'response code  = uri too long'
	elif web_request == 416:
		return 'response code  = requested range not satisfiable'
	elif web_request == 417:
		return 'response code  = execution failed'
	elif web_request == 418:
		return 'response code  = im a teapot'
	elif web_request == 421:
		return 'response code  = misdirected report'
	elif web_request == 422:
		return 'response code  = unprocessable entity'
	elif web_request == 423:
		return 'response code  = locked'
	elif web_request == 424:
		return 'response code  = failed dependency'
	elif web_request == 426:
		return 'response code  = upgrade required '
	elif web_request == 428:
		return 'response code  = precondition required '
	elif web_request == 429:
		return 'response code  = too many requests '
	elif web_request == 431:
		return 'response code  = requests header field too large'
	elif web_request == 451:
		return 'response code  = unavailable for legal reasons'
	elif web_request == 500:
		return 'response code  = internal server error'
	elif web_request == 501:
		return 'response code  = not implemented'
	elif web_request == 502:
		return 'response code  = bad gateway'
	elif web_request == 503:
		return 'response code  = service unavailable'
	elif web_request == 504:
		return 'response code  = gateway timeout'
	elif web_request == 505:
		return 'response code  = http version not supported'
	elif web_request == 506:
		return 'response code  = variants also negotiates '
	elif web_request == 507:
		return 'response code  = insuficient storage '
	elif web_request == 508:
		return 'response code  = loop detected '
	elif web_request == 510:
		return 'response code  = not extended'
	elif web_request == 511:
		return 'response code  = network authentication required'
