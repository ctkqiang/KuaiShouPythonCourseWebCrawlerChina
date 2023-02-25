class KuaiShouUrl:
    def __init__(self, url, pKey, tag, clientCacheKey, token):
        self.url = url
        self.pKey = pKey
        self.tag = tag
        self.clientCache = clientCacheKey
        self.token = token

    def tostr(self=None) -> str:
        try:
            return '{url}{token}?pkey={pKey}&tag={tag}&clientCacheKey={clientCacheKey}'.format(
                url=self.url,
                token=self.token,
                pKey=self.pKey,
                tag=self.tag,
                clientCacheKey=self.clientCache
            )
        except:
            raise "Something is not working [UNABLE_TO_CONVERT_TO_STRING] (n_n)"
