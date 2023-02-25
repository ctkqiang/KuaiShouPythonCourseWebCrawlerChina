try:
    import os
    import random
    import requests
    from models.KuaiShouUrl import KuaiShouUrl
except:
    raise "Some packages unable to be installed (n_n)"


class KuaiShouCrawler:
    """
    @author: John Melody Me
    Using #class for a better view of Object-Oriented Programming.
    Pardon me please LaoShi, I am used to Object-Oriented Programming.
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
        self.token: str = 'BMjAyMjEwMDIxMTM0MjFfMjQzNzA2NTQxNF84NTQ4MTY2MTQ0MF8yXzM=_hd15_B7bdf92b6d808feb21eb0501f9eb02ee8.mp4'
        self.filename: str = 'kuai_shou_video_download.mp4'

    @classmethod
    def download(cls, preview: bool, writeable: object) -> None:
        """
            :rtype: None [void]
        """
        # Set current directory
        current_dir: os = os.getcwd()

        def get_open_cmd() -> str:
            if os.name == "posix":
                return "open"
            elif os.name == "nt":
                return "start"
            else:
                return "echo"

        def setname() -> str:
            if os.path.exists("{current}/{file}".format(current=current_dir, file=KuaiShouCrawler().filename)):
                char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                return char[random.randint(0, 25)] + ".mp4"
            return KuaiShouCrawler().filename

        # Write Content into file
        file: object = open(setname(), 'wb')
        file.write(writeable)
        file.close()

        print("Done")

        if preview:
            os.system(
                "{command} {current_location}/{filename}".format(
                    command=get_open_cmd(),
                    current_location=current_dir,
                    filename=KuaiShouCrawler().filename
                )
            )
        else:
            return
        return None

    @classmethod
    def crawl(cls) -> None:
        try:
            crawler: object = KuaiShouCrawler()

            url: str = KuaiShouUrl(
                url=crawler.kuai_shou_url,
                pKey=crawler.pKey,
                tag=crawler.tag,
                clientCacheKey=crawler.clientCacheKey,
                token=crawler.token
            ).tostr()

            if url is None:
                raise "The url is Empty. (u_u)"

            # HTTP/2 [Get] request
            res: requests = requests.get(url)

            if res.status_code == 0xC8:  # Status code [200]
                body: object = res.content
                # If the return data are different DataType, then you are doing something wrong
                assert type(body) == bytes

                # Download Content and preview it if set to `True`, default set to `False`
                KuaiShouCrawler.download(preview=False, writeable=body)

            elif res.status_code == 0x190:  # Status code [400]
                raise "Failed to request URL"
            elif res.status_code == 0x193:  # Status code [403]
                raise "You don't have permission to access to {}".format(url)
            elif res.status_code == 0x194:  # Status code [404]
                raise "Do you have the correct URL?"
            elif res.status_code == 0x1F4:  # Status code [500]
                raise "Server is down? "
            else:  # Status code [100 - 500] or the rest
                raise "something is Wrong with the [get] Http/2 request"
        except:
            raise "Can't crawl (n_n)"


if __name__ == "__main__":
    ks = KuaiShouCrawler()
    ks.crawl()
