import asyncio
from utils import async_get, change_ip

class Scrapper:
	def __init__(self, proxy):
		self.proxy = proxy

	async def parse(self, wallet:str):
		url = f'https://phosphor.xyz/api/foxy/allow-list-status/{wallet}'

		for i in range(5):
			try:
				res = await async_get(url=url, proxy=self.proxy)
				return {wallet: res}

			except Exception as e:
				print(e)
				await asyncio.sleep(1)


