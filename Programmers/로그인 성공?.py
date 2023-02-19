def solution(id_pw, db):
    db = dict(db)
    
    if id_pw[0] not in db.keys():
        return "fail"
    elif id_pw[1] != str(db[id_pw[0]]):
        return "wrong pw"
    else:
        return "login"
