import ctypes
import math

path = 'src/subcommands/_math/c/'
rt   = ctypes.cdll.LoadLibrary(f'{path}rate.so')
rt.argtypes = (ctypes.c_char_p, ctypes.c_int)
rt.restype  = ctypes.c_double

async def rateBlog(ctx):
    link = ctx.msg.content.split(" ")
    if len(link) == 1: return "Debe poner el link de un blog"

    try:
        blogId = await ctx.client.get_info_link(link=link[1])
        blogId = blogId.linkInfo.objectId
    except:
        return ctx.send("Se ha producido un error c")

    blog = await ctx.client.get_blog_info(blogId)

    content = blog.content
    text = content.encode("utf-8")
    l    = len(content)

    score = rt.rate(text, l)
    
    score = math.sin(score)
    score = (2/((math.e ** score) + (math.e ** -score)))**2
    print(score)

    if score < 0.5:
        await ctx.send(f"A Nati no le ha gustado tu blog. Lo ha calificado con:\n[b]{(score*10):.2}/10")
    else         :
        await ctx.send(f"A Nati le ha gustado tu blog. Lo ha calificado con:\n[b]{(score*10):.2}/10\n\nAdemás, le ha dado like.")
        await ctx.client.like_blog(blog_id=blogId)

    return
