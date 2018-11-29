from configbd import conn

bd = conn()


out = bd.posts.find_one()

print(out)
