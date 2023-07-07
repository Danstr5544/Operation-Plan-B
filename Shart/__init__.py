from .planb import dmmail


async def setup(bot):
    await bot.add_cog(MyCog(bot))
