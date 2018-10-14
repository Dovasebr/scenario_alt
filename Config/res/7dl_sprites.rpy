init 9999 python:
    alt_images = default_7dl_path + "Pics/sprites/"
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        bl_images = "images/1080/sprites/"
    else:
        bl_images = "images/sprites/"
        
    alt_body_dict = {
                    'dv':{'1':['body','body2'],
                          '2':['body','body2'],
                          '3':['body','body2'],
                          '4':['body','body2'],
                          '5':['body','body2']}
        }
    alt_clothes_dict = {
                    'dv':{'1':['pioneer','pioneer2','swim','dress','sport','body'],
                          '2':['pioneer','pioneer2','swim','sport','body'],
                          '3':['pioneer','pioneer2','dress','sport','body'],
                          '4':['pioneer','pioneer2','swim','dress','sport','dress_pregnant','winter','body'],
                          '5':['pioneer','pioneer2','sport','body']}
        }
    alt_emo_dict = {
                    'dv':{'1':['cry','scared','shocked','surprise'],
                          '2':['grin'],
                          '3':['guilty','sad','shy'],
                          '4':['laugh','normal','smile','soft_smile'],
                          '5':['angry','rage']}
        }
    alt_acc_dict = {
                    'dv':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':[''],
                          '5':['']}
        }
    
    alt_dist = ['normal/','far/']
    for dist in alt_dist:
        if dist == "normal/":
            for who in alt_body_dict.keys():
                for pose in alt_body_dict[who]:
                    for body in alt_body_dict[who][pose]:
                        for clothes in alt_clothes_dict[who][pose]:
                            for emo in alt_emo_dict[who][pose]:
                                for acc in alt_acc_dict[who][pose]:
                                    if body != '':
                                        if 'body2' in body:
                                            who_num = who + '2'
                                        elif 'body' in body:
                                            who_num = who
                                        if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        if clothes != 'body':
                                            if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            if emo != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), ), 
                                                                        close_sprites)
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), ), 
                                                                        close_sprites)
                                                                        )
                                        else:
                                            if emo != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), ), 
                                                                        close_sprites)
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), ), 
                                                                        close_sprites)
                                                                        )
                                    else:
                                        who_num = who
                                        if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        if emo != '':
                                            if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            if acc != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc,
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), )
                                                                    )
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close',
                                                                    At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), ), 
                                                                    close_sprites)
                                                                    )
                                            else:
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes,
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), )
                                                                    )
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' close',
                                                                    At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), ), 
                                                                    close_sprites)
                                                                    )
        elif dist == "far/":
            for who in alt_body_far_dict.keys():
                for pose in alt_body_far_dict[who]:
                    for body in alt_body_far_dict[who][pose]:
                        for clothes in alt_clothes_far_dict[who][pose]:
                            for emo in alt_emo_far_dict[who][pose]:
                                for acc in alt_acc_far_dict[who][pose]:
                                    if body != '':
                                        if 'body2' in body:
                                            who_num = who + '2'
                                        elif 'body' in body:
                                            who_num = who
                                        if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        if clothes != 'body':
                                            if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            if emo != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                        else:
                                            if emo != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                    else:
                                        who_num = who
                                        if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        if emo != '':
                                            if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            if acc != '':
                                                if renpy.loadable(bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = bl_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                elif renpy.loadable(alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = alt_images + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far',
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), )
                                                                    )
                                            else:
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' far',
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), )
                                                                    )
                                                        
transform close_sprites:
    zoom 1.25
    yoffset 238
    xoffset 38
    
                                    
                                    
                                    
                                    
                                    
                                    