﻿
init:
    define M = Character("MARCHAND", what_prefix='"', what_suffix='"', color="#c8a2c8")
    define MC = Character("VOUS" , what_prefix='"', what_suffix='"', color="#a2c8a2")
    define O = Character("OUVRIER", what_prefix='"', what_suffix='"', color="#c2c8a2")
    define P = Character("PEINTRE", what_prefix='"', what_suffix='"', color="#a2a2c8")

image empty:
    "images/empty_1.png"
    pause 0.4
    "images/empty_2.png"
    pause 0.4
    "images/empty_3.png"
    pause 0.4
    "images/empty_4.png"
    pause 0.4
    repeat

label start:
    scene empty
    "Où suis-je ?"
    "Qui suis-je ?"
    "J’étais pourtant aux pyramides d’Égyptes..."
    "Comment est-ce poss-{nw}"
    scene bg_1 with fade
    M "Vous allez bien mademoiselle ?"
    M "Vous semblez toute pâle."

    menu:
        "Qui êtes-vous ?":
            jump qui_etes_vous

        "Où sommes-nous ?":
            jump ou_sommes_nous

label qui_etes_vous:
    MC "Qui êtes-vous ?"
    M "Je ne suis qu’un humble marchand."
    M "Je reviens tout juste d’un périple en Chine."
    M "J’y ai goûté le plus savoureux des thés !"
    "Mais{w=0.3} qu’est-ce que je fais ici ?"
    MC "Et où allons-nous ?"
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    "Ça ne me dit vraiment rien..."
    jump dialogue_apres_choix

label ou_sommes_nous:
    MC "Où sommes-nous ?"
    M "À bord du navire le plus éminent marchand d’Europe !"
    M "Je reviens tout juste d’un voyage en Chine."
    M "J’y ai goûté le plus savoureux des thés !"
    MC "Mais qu’est-ce que je fais ici ?"
    MC "Et où allons-nous ?"
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    "Ça ne me dit vraiment rien..."
    jump dialogue_apres_choix

label dialogue_apres_choix:
    MC "Connaissez-vous un moyen d’aller aux pyramides d’égypte ?"
    M "Je ne connais pas assez les lieux pour vous aider."
    M "Cependant,{w=0.3} je pense que l’homme au haut-de-forme appuyé sur la balustrade pourra vous aider."
    M "C’est un peintre connu qui connaît la ville comme sa poche."
    M "Il a même fondé un tout nouveau musée,{w=0.4} le musée des Beaux-Arts !"
    "Ces informations ne m’aident franchement pas."
    "Mais il semble savoir de quoi il parle, ça ne coûte rien d’essayer."
    jump ouvrier

label ouvrier:
    scene bg_ouvrier with fade
    MC "Je le vois,{w=0.3} ça doit être lui le fameux peint-{nw}"
    O "HO LÀ,{w=0.3} MADAME !"
    O "C’est quoi cet accoutrement ?"
    MC "Mais,{w=0.3} c’est qui lui ?"

    menu:
        "Répondre":
            jump repondre

        "Ne rien dire":
            jump ne_rien_dire

label repondre:
    MC "Ce sont des vêtements nobles sale malôtru !"
    O "Faites attention à vous, y’en a qui travaillent ici."
    O "Ici vous ne trouverez que de simples ouvriers acharnés."
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    MC "Je vous remercie."
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Allez-vous-en avant de salir vos beaux habits."
    jump peintre

label ne_rien_dire:
    MC "…"
    O "Ici vous ne trouverez que de simples ouvriers acharnés."
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    MC "…"
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Ravi d’avoir parlé avec vous !"
    "Parlé ?{w=0.3} Qu’est-ce qu’il raconte ?"
    jump peintre

label peintre:
    scene bg_peintre with fade
    MC "Excusez-moi Monsieur,{w=0.3} seriez-vous peintre ?"
    P "En effet,{w=0.3} que me voulez-vous ?"
    MC "J’ai été transporté ici contre mon gré et je souhaiterai rentrer d’où je viens."
    MC "J’ai ouïe dire que vous sauriez peut-être m’aider."
    P "C’est peut-être le cas mais,{w=0.3} qu’est-ce que j’y gagnerai ?"
    MC "Eh bien,{w=0.3} je pourrais vous donner le Sceptre Papyrus."
    P "Je n’ai pas la moindre idée de ce que c’est."
    P "Mais soit,{w=0.3} j’accepte."
    P "Je connais peut-être des gens selon votre provenance."
    P "Mais ils n’arriveront que d’ici demain."
    MC "Auriez-vous un lieu où loger la nuit ?"
    P "Mon ami Louis Combes ici présent m’a dit le plus grand bien de l’Hôtel derrière moi."
    P "Il est dit que l'hôtel Fenwick était un lieu où les espions se rencontraient secrètement pour planifier leurs missions."
    P "Cocasse,{w=0.3} pas vrai ?"
    "C'est un drôle d'hôtel."
    P "Je connais le propriétaire,{w=0.3} je pourrais peut-être vous trouver une chambre à l’étage des domestiques."
    MC "Ne voyez-vous pas que je n’ai aucune monnaie adéquate pour résider dans l’hôtel ?"
    MC "Auriez-vous une alternative ?"
    P "Eh bien,{w=0.3} permettez-moi de vous proposer ceci,"
    P "Vous avez un profil tout à fait singulier que j’aimerais grandement immortaliser."
    P "Alors,{w=0.3} vous me laissez vous peindre,{w=0.3} et je vous offre la nuitée."
    P "Qu’en dites-vous ?"

    menu:
        "C’est d’accord.":
            jump peinture_accord

        "Euh…":
            jump peinture_hesitation

label peinture_accord:
    P "Parfait !{w=0.3} Pourriez-vous vous placez ici ?"
    P "Où désirez-vous être peint ?"
    MC "Faites-moi donc aux pyramides d'égypte."
    P "Je commence."
    MC "Je me sens étrange…"
    # Transition ou effet pour montrer le passage du temps
    P "Vous avez un air vraiment très particulier."
    MC "Comme si je partais…"
    # Encore une transition ou effet
    P "J’approche de la fin."
    P "Voilà qui est fait !"
    P "Bon voyage !"
    MC "La chaleur, le sable, pas de doute, je suis de retour aux pyramides."

    return

label peinture_hesitation:
    MC "Euh, je sais pas trop…"
    P "Laissez-moi vous convaincre !"
    P "Voici une de mes récentes peintures, vous m’en direz des nouvelles."
    # Insérer l'image avec un fondu
    show peinture with Dissolve(1.0)
    # Attendre un clic de l'utilisateur
    pause
    MC "Il a un certain talent, c’est indéniable."
    MC "Ce n’est peut-être pas une mauvaise idée au final."
    MC "Bon, c’est d’accord."
    P "Super !{w=0.3} Pourriez-vous vous mettre ici ?"
    P "Dans quel endroit vous voudriez je vous peigne ?"
    MC "Faites-moi donc aux pyramides d'égypte."
    P "Je commence."
    $ renpy.pause()
    scene defor_1
    # Transition ou effet + Attendre un peu
    MC "Je me sens bizarre…"
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "Vous dégagez un air vraiment très particulier."
    MC "Comme si je partais…"
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "J’approche de la fin."
    $ renpy.pause(1.5)
    # Attendre un peu
    P "Voilà qui est fait !"
    P "Bon voyage !"
    MC "La chaleur, le sable, pas de doute, je suis de retour aux pyramides."

    return
