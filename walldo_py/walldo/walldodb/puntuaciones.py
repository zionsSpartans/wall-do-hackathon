from configbd import conn
import pymongo

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

## TEEEEEESTIIIING
try:
    for insert_change in score.watch(
            [{'$match': {'operationType': 'update'}}]):
        print(insert_change)

except pymongo.errors.PyMongoError:

    # We know it's unrecoverable:
    print('...')