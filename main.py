try:
    import requests
    from models.KuaiShouUrl import KuaiShouUrl
except:
    raise "Some packages unable to be installed (n_n)"


class KuaiShouCrawler:
    """
    Using #class for a better view of Object oriented Programming.
    Pardon me please LaoShi, I am used to OOP.
    The packages are required to be installed by execute command as following

        ```bash
            pip3 install -r requirements.txt
        ```
    """

    def __init__(self):
        # The given {url} from KuaiShou assigned to variable #self.kuai_shou_url as [String]
        self.kuai_shou_url: str = 'https://v1.kwaicdn.com/upic/2022/10/02/11/'
        self.pKey: str = 'AAWZKPBsY51B5gLywAZDOkLfQNVGwaADkGn_FMgEt0ymqbiSyjJrPFWSoktg5XZ4swyBNa3z-3wgvu2lJTRCvyzUn7PmWPZJEuJhlxqIzjAzP4_KPMQ2ky_wDSj52Kp9bYA'
        self.tag: str = '1-1677314739-unknown-0-o8geqc9oab-44b3760dd68550bd'
        self.clientCacheKey: str = '3x7is626qs3fjg4_hd15.mp4&di=b7ab66dd&bp=14944&tt=hd15&ss=vp'
        self.token: str = 'BMjAyMjEwMDIxMTM0MjFfMjQzNzA2NTQxNF84NTQ4MTY2MTQ0MF8yXzM=_hd15_B7bdf92b6d808feb21eb0501f9eb02ee8.mp4?'

    @classmethod
    def crawl(cls):

        pass


if __name__ == "__main__":
    ks = KuaiShouCrawler()
    ks.crawl()
